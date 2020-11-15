#codec=utf-8
import pages
import sqlite3
from bottle import route, run, static_file, abort, post, response, request, redirect, error
from random import choice
from json import load, dump
from sys import argv
from os import path, mkdir, listdir, remove, rmdir
from zipfile import ZipFile, BadZipFile
from hashlib import sha3_256 as sha3


ADMIN_KEY = ''
MAIN_TYPE = 0


db = ''
sql_search = ('chars', 'genres', 'series', 'comands')


def hash(text):
	return sha3(str(text).encode('utf-8')).hexdigest()


def get_path(file):
	return path.join(path.dirname(path.abspath(__file__)), argv[1], file)


def _optimize(text):
	return text.replace('\n', '').replace('\t', '')


def prepare_main(text, header=''):
	return _optimize(pages.main_page.format(header+text))


def prepare_err(text, ico):
	return _optimize(pages.main_page.format(pages.error.format(text, ico)))


def db_work(func):
	def wrap(*a, **ka):
		cursor = db.cursor()
		ret = func(*a, cursor=cursor, **ka)
		cursor.close()
		return ret
	return wrap


def login(func):
	def wrap(*a, **ka):
		session = get_session(request)
		if session:
			return func(*a, session=session, **ka)
		redirect('/')
	return wrap


def red(cursor, redir):
	cursor.close()
	redirect(redir)


def ab(cursor, ab):
	cursor.close()
	abort(ab)


@db_work
def get_session(request, cursor):
	"""
	return session data or None
	"""
	if request.get_cookie('auth') and request.get_cookie('id_auth'):
		cursor.execute('select * from session where id=?;', (request.get_cookie('id_auth'), ))
		res = cursor.fetchone()
		if res is not None:
			ip = request['REMOTE_ADDR']
			agent = request.headers.get('User-Agent')
			if ip == res[2] and agent == res[3] and request.get_cookie('auth') == res[4]:
				return res
	return None


@db_work
def is_admin(session, cursor):
	if session is None:
		return False
	cursor.execute('select * from admin where id_user=?;', (session[1], ))
	return cursor.fetchone() is not None


@db_work
def is_access(manga_id, session, cursor):
	return is_admin(session) or cursor.execute('select * from hentai_user where id_hentai=? and id_user=?;', (manga_id, session[1])).fetchone() is not None


def get_header(c_request):
	"""
	Check admin mode status and generate header

	:param c_request: gotted request
	"""
	session = get_session(c_request)
	if session:
		if is_admin(session):###
			header = pages.header.format(pages.add_manga_button + pages.admin_button + pages.exit_button)
			header += pages.admin_yes.format(choice(listdir('static/admin')))
		else:
			header = pages.header.format(pages.add_manga_button + pages.exit_button)
	else:
		header = pages.header.format('')#Дописати кнопку увійти
	return header


def get_flag(id):
	cursor = db.cursor()
	flag = ''
	if cursor.execute('select * from lang where id_hentai=?;', (id, )).fetchone() is not None:
		flag = pages.flag_ua
	cursor.close()
	return flag


def get_wall(dir):
	try:
		return '/hentai/{}/{}'.format(dir, sorted(listdir(path.join(get_path('hentai'), dir)))[0])
	except (IndexError, FileNotFoundError):
		return '/static/ico/U_logo.svg'


@route('/sitemap.xml')
def sitemap():
	return static_file("sitemap.xml", argv[1])


@route('/robots.txt')
def sitemap():
	return static_file("robots.txt", argv[1])


@route('/static/css/<file:re:.*css>')
def load_static(file):
	with open(path.join(path.dirname(path.abspath(__file__)), 'static', 'css', file), encoding='utf-8') as fd:
		return _optimize(fd.read())
	abort(404)


@route('/static/<file:path>')
def load_static(file):
	return static_file(file, 'static')


@route('/hentai/<file:path>')
def load_hentai(file):
	return static_file(file, get_path('hentai'), 'image/jpg')


@db_work
def get_manga(sql, param='', cursor=''):
	"""
	:param sql: sql query to get id, name, dir
	:param param: tuple param to sql
	"""
	if cursor == '':
		abort(500)
	ind = cursor.execute(sql, param).fetchall()
	content = '<div class="wrap container">'
	if len(ind) > 0:
		for row in ind:
			content += '''<div class="block">
			{}<a href=/manga/{}>
			<img class="block__img" src="{}">
			<div class="font block__title">{}</div></a>
			</div>'''.format(get_flag(row[0]), row[0], get_wall(row[2]), row[1])
	else:
		content += '<img src="/static/ico/MNF.png"><br><div class="font">Схоже, що мальописи відсутні</div>'
	content += '</div>'
	return content


@route('/')
def index():
	if MAIN_TYPE == 0:
		return prepare_main(get_manga('select * from last_series;'), get_header(request))
	else:
		return prepare_main(get_manga('select * from last_hentai;'), get_header(request))


@route('/all')
def all():
	return prepare_main(get_manga('select * from last_hentai;'), get_header(request))


@route('/search/series/<id:int>')
@db_work
def search_engine(id, cursor):
	cursor.execute('select id_hentai from hentai_series where id_series=? order by id_hentai;', (id,))
	red(cursor, '/manga/{}'.format(cursor.fetchone()[0]))


@route('/search/<type>/<id:int>')
def search_engine(type, id):
	if type in sql_search:
		return prepare_main(
		get_manga(
			'select id,name,dir from hentai,hentai_' + type + ' where id_hentai=id and id_' + type + '=?;',
			(id, )),
		get_header(request))
	else:
		abort(404)

@route('/list/<type>')
@db_work
def genres_list(type, cursor):
	if type in sql_search:
		genres = cursor.execute('SELECT * from ' + type + ';').fetchall()
		genres.sort(key = lambda el: el[1])

		content = '<div class="search wrap container">'
		current_symbol = genres[0][1][0]
		content += pages.genre_group.format(current_symbol, current_symbol.upper())
		symbols = [current_symbol]
		for g_id, name in genres:
			if name[0] != current_symbol:
				current_symbol = name[0]
				content += '</div>' + pages.genre_group.format(current_symbol, current_symbol.upper())
				symbols += current_symbol
			content += pages.genre_button.format(type, g_id, name)

		content += '</div></div><div class="bottom-bar">'
		for i in symbols:
			content += pages.bottom_bar_symbol.format(i, i.upper())
		content += '</div>'

		return prepare_main(content, get_header(request))
	else:
		ab(cursor, 404)


@route('/lang/<id:int>')
def lang(id):
	return prepare_main(
		get_manga('select id, name, dir from hentai, lang where id_hentai = id;'),
		get_header(request))


@route('/manga/<id:int>')
@db_work
def manga(id, cursor):
	cursor.execute('select name, dir from hentai where id=?;', (id,))
	res = cursor.fetchone()
	if res is not None:
		disc_content = ''

		info = ('Персонажі', 'Жанри', 'Серія мальописів', 'Переклали')
		for i in range(len(info)):
			genres = cursor.execute(
				'select id_{0} from hentai_{0} where id_hentai=?;'.format(sql_search[i]), (id,)
			).fetchall()
			if len(genres) > 0:
				disc_content += '<div class="font manga__font">{}</div>'.format(info[i])
			for genre in genres:
				cursor.execute('select id,name from {} where id=?;'.format(sql_search[i]), (genre[0],))
				genre_info = cursor.fetchone()
				disc_content += pages.genre_button.format(sql_search[i], genre_info[0], genre_info[1])

		controler = '<div class="manga__bottom-button"><a class="font big-font button manga__button" href="/show/{0}/0">Читати немов книгу</a>'\
					'<a class="font big-font button manga__button" href="/show/{0}">Читати немов сувій</a></div>'.format(id)

		cursor.execute('select id_series from hentai_series where id_hentai=?;', (id,))
		id_series = cursor.fetchone()
		if id_series:
			cursor.execute('select id_hentai, name, dir from hentai_series,hentai where id_series=? and id_hentai=id;', id_series)
			controler += '<ul class="font manga-list list">'
			mangas = cursor.fetchall()
			for i in mangas:
				controler += '<li><a class="list__link" href="/manga/{}">{}</a></li>'.format(i[0], i[1])
			controler += '</ul>'

		content = pages.manga.format(res[0], get_flag(id), id,
			get_wall(res[1]),
			disc_content, controler)

		#ADMIN MENU
	session = get_session(request)
	if session:
		if is_access(id, session):
			content += '<div>'
			for type, type_name in zip(sql_search, ('персонажа', 'жанр', 'серію', 'команду')):
				content += '<div class="list-block">' \
					'<form class="list" method="post" action="/a_add/' + type + '">' \
					'<input type="hidden" name="id" value={}>' \
					'<div class="font">Додати {}</div>' \
					'<select multiple class="font list__select" name="'.format(id, type_name) + type + '">'

				genres = cursor.execute('select id_' + type + ' from hentai_' + type + ' where id_hentai={};'.format(id)).fetchall()
				genres_full = cursor.execute('select id, name from ' + type + ' order by name;').fetchall()
				genres_exclude = [i for i in genres_full if (i[0],) not in genres]
				genres_x = [i for i in genres_full if (i[0],) in genres]

				for genre_i in genres_exclude:
					content += '<option value="{}">{}</option>'.format(genre_i[0], genre_i[1])
				content += '</select><br><button class="font button"' \
					'type="submit">Додати</button></form>' \
					'<form class="list" method="post" action="/a_del/' + type + '">' \
					'<input type="hidden" name=id value={}>' \
					'<div class="font">Видалити {}</div>' \
					'<select multiple class="font list__select" name="'.format(id, type_name) + type + '">'

				for genre_i in genres_x:
					content += '<option value="{}">{}</option>'.format(genre_i[0], genre_i[1])

				content += '</select><br><button class="font button"'\
					' type="submit">Видалити</button></form></div>'
			content += pages.u_manga_edit.format(id)
			content += '</div>'
	content += '</div>'
	return prepare_main(content, get_header(request))


@route('/show/<id:int>')
@db_work
def show(id, cursor):
	dir = cursor.execute('select dir from hentai where id=?;', (id, )).fetchone()[0]
	content = ''
	for img in sorted(listdir(path.join(get_path('hentai'), dir))):
		content += '<img class="show__img" src="/hentai/' + dir + '/' + img + '"><br>'
	return prepare_main(pages.show.format(id, content))


@route('/show/<id:int>/<page:int>')
@db_work
def show(id, page, cursor):
	dir = cursor.execute('select dir from hentai where id=?;', (id, )).fetchone()[0]
	l_manga = len(listdir(path.join(get_path('hentai'), dir)))
	if l_manga <= page or 0 > page:
		ab(cursor, 404)
	elif l_manga <= page+1:
		content = pages.show_book.format('/manga/'+str(id), dir, sorted(listdir(path.join(get_path('hentai'), dir)))[page])
	else:
		content = pages.show_book.format('/show/'+str(id)+'/'+str(page+1), dir, sorted(listdir(path.join(get_path('hentai'), dir)))[page])

	args = [id, '', '/show/'+str(id)+'/0', '/show/'+str(id)+'/'+str(page-1), page + 1, l_manga, '',
		'/show/'+str(id)+'/'+str(l_manga - 1), '/show/'+str(id)+'/'+str(page+1)]
	if page == 0:
		args[1], args[6] = 'hidden', 'visible'
	elif page == l_manga - 1:
		args[1], args[6] = 'visible', 'hidden'
	else:
		args[1], args[6] = 'visible', 'visible'
	content += pages.page_scroll.format(*args)
	return prepare_main(content)


@route('/a')
@db_work
@login
def admin(cursor, session):
	if is_admin(session):###
		el_list = ''
		for el, eln in zip(sql_search, ('персонажа', 'жанр', 'серію', 'команду')):
			op_list = ''
			for op in cursor.execute('select * from ' + el + ' order by name;').fetchall():
				op_list += '<option class="font" value="{}">{}</option>'.format(op[0], op[1])
			el_list += pages.admin_mode_el.format(el, eln, op_list)
		return prepare_main(pages.admin_mode.format(el_list), get_header(request))
	else:
		ab(cursor, 401)


def admin_test(func):
	def wrap(*a, **ka):
		if is_admin(get_session(request)):
			try:
				return func(*a, **ka)
			except KeyError:
				abort(404)
		else:
			abort(401)
	return wrap


@route('/a_manga')
def add_manga():
	if get_session(request):
		return prepare_main(pages.add_manga, get_header(request))
	else:
		return prepare_main(pages.admin_mode.format('Для заливання манґи, будь ласка, зареєструйтесь'), get_header(request))


@post('/a_manga')
@db_work
@login
def p_add_manga(cursor, session):
	name = request.forms.get('dir')
	dir = name.replace('.', '').replace('/', '').replace('\\', '')
	if path.exists(get_path(path.join('hentai/', dir))):
		suffix=0
		while path.exists(get_path(path.join('hentai/', dir + '-' + str(suffix)))):
			suffix += 1
		dir += '-' + str(suffix)
	zip = request.files.get('zip')
	file, ext = path.splitext(zip.filename)
	if ext.lower() != '.zip':
		return 'То людина чи компутор? Я тобі кажу zip мені кидай'

	real_dir = get_path(path.join('hentai/', dir))
	mkdir(real_dir)
	zip.save(real_dir)
	try:
		with ZipFile(path.join(real_dir, zip.filename)) as file:
			file.extractall(real_dir)
	except BadZipFile:
		remove(path.join(real_dir, zip.filename))
		rmdir(real_dir)
		return 'Поганий файл, йолопе'
	remove(path.join(real_dir, zip.filename))

	cursor.execute('insert into hentai values (null, ?, ?);', (name, dir))
	hentai_id = cursor.execute('select id from hentai where dir=?;', (dir, )).fetchone()[0]
	cursor.execute('insert into hentai_user values (?, ?);', (hentai_id, session[1]))
	db.commit()
	red(cursor, '/all')


@post('/c_file/<id:int>')
@login
@db_work
def c_file(id, cursor, session):
	if is_access(id, session):
		zip = request.files.zip
		file, ext = path.splitext(zip.filename)
		if ext.lower() != '.zip':
			return 'То людина чи компутор? Я тобі кажу zip мені кидай'

		dir = cursor.execute('select dir from hentai where id=?;', (id,)).fetchone()[0]
		dir = path.join(get_path('hentai'), dir)
		for i in listdir(dir):
			remove(path.join(dir, i))

		zip.save(dir)
		try:
			with ZipFile(path.join(dir, zip.filename)) as file:
				file.extractall(dir)
		except BadZipFile:
			remove(path.join(dir, zip.filename))
			rmdir(dir)
			return 'Поганий файл, йолопе'
		remove(path.join(dir, zip.filename))

		red(cursor, '/manga/' + str(id))
	else:
		ab(cursor, 401)


@post('/c_name/<id:int>')
@login
@db_work
def c_name(id, cursor, session):
	if is_access(id, session):
		name = request.forms.name
		cursor.execute('update hentai set name=? where id=?;', (name, id))
		db.commit()
	red(cursor, '/manga/' + str(id))


@post('/show/<id:int>/<page:int>')
@db_work
def show_post(id, page, cursor):
	dir = cursor.execute('select dir from hentai where id=?;', (id, )).fetchone()[0]
	cursor.close()
	hentai = len(listdir(path.join(get_path('hentai'), dir)))
	try:
		new_page = int(request.forms.page) - 1
		if new_page < 0 or new_page >= hentai:
			redirect(request.url)
		else: redirect('/show/{}/{}'.format(dict(request.url_args)['id'], new_page))
	except ValueError: redirect(request.url)


@post('/a_add/<type>')
@db_work
@login
def admin_add(type, cursor, session):
	if is_access(request.POST['id'], session):
		if type in sql_search:
			for genre in request.forms.getall(type):
				cursor.execute('insert into hentai_' + type + ' values(?, ?);',
						(request.POST['id'], genre))
			db.commit()
		red(cursor, '/manga/{}'.format(request.POST['id']))
	else:
		ab(cursor, 401)


@post('/a_del/<type>')
@db_work
@login
def admin_del(cursor, type, session):
	if is_access(request.POST['id'], session):
		if type in sql_search:
			for genre in request.forms.getall(type):
				cursor.execute('delete from hentai_' + type + ' where id_hentai=? '
							'and id_' + type + '=?;', (request.POST['id'], genre))
			db.commit()
		red(cursor, '/manga/{}'.format(request.POST['id']))
	else:
		cursor.close()
		ab(cursor, 401)


@post('/a_a/<type>')
@db_work
@admin_test
def admin_add_tag(type, cursor):
	if type in sql_search:
		cursor.execute('insert into ' + type + ' values(null, ?);',
			(request.forms.name, ))
		db.commit()
	red(cursor, '/a')


@post('/a_d/<type>')
@db_work
@admin_test
def admin_add_tag(type, cursor):
	if type in sql_search:
		for i in request.forms.getall('el'):
			cursor.execute('delete from ' + type + ' where id=?;', (i, ))
		db.commit()
	red(cursor, '/a')


@route('/about')
def about():
	return prepare_main(pages.about, get_header(request))


@route('/friend')
def friend():
	return prepare_main(pages.friend, get_header(request))


@route('/login')
def g_login():
	session = get_session(request)
	if session:
		redirect('/')
	else:
		err = ('Немає такого користувача', 'Неправильний пароль')
		try:
			err_num = int(request.query.err)
			if err_num >= 0 and err_num < len(err):
				return prepare_main(pages.login.format(pages.error_head.format(err[err_num])), get_header(request))
		except ValueError:
			pass
		return prepare_main(pages.login.format(''), get_header(request))


@post('/login')
@db_work
def p_index(cursor):
	cursor.execute('select pass from user where id=?;', (request.forms.get('login'),))
	res = cursor.fetchone()
	if res is None:
		red(cursor, '/login?err=0')
	else:
		if hash(request.forms.get('pass')) == res[0]:
			ip = request['REMOTE_ADDR']
			agent = request.headers.get('User-Agent')
			_hash = hash(hash(hash(request.forms.get('pass'))+ip)+agent)
			cursor.execute('insert into session values(null, ?, ?, ?, ?);', (request.forms.get('login'), ip, agent, _hash))
			db.commit()
			cursor.execute('select id from session where id_user=? and ip=? and agent=?;', (request.forms.get('login'), ip, agent))
			response.set_cookie('auth', _hash, max_age=432000)
			response.set_cookie('id_auth', str(cursor.fetchone()[0]), max_age=432000)
		else:
			red(cursor, '/login?err=1')
	red(cursor, '/login')


@route('/exit')
@db_work
@login
def exit(cursor, session):
	response.set_cookie('auth', '')
	response.set_cookie('id_auth', '')
	cursor.execute('delete from session where id=?;', (session[0],))
	db.commit()
	red(cursor, '/')


@error(404)
def err404(err):
	return prepare_err('Як ти сюди потрапив?', '404.png')


@error(500)
def err500(err):
	return prepare_err('Або ти лізеж куди не треба, або у нас '
		'полетіла БД. І якщо це так — то пізно срати. '
		'Може полагодим скоро, може ні', '500.png')


@error(401)
def err401(err):
	return prepare_err('У тебе немає доступу до цього.'
		' Йди-но звідси доки не втрапив у халепу', '401.png')


if __name__ == '__main__':
	if len(argv) <= 0:
		print('Specify work dir')
		exit(1)
	db = sqlite3.connect(get_path('db'))
	db.execute('pragma foreign_keys = 1')

	SETTING = None
	try:
		with open(get_path('conf.json'), 'r') as fd:
			SETTING = load(fd)
	except FileNotFoundError:
		print('Config not found! Creating template...')
		SETTING = {'ADMIN_KEY': '', 'ADMIN_MODE': False, 'RELOAD': False, 'QUITE': True, 'IP': '127.0.0.1', 'SRV': 'wsgiref', 'PORT': 80, 'SSL': '', 'MAIN_TYPE': 0}
		with open(get_path('conf.json'), 'w') as fd:
			dump(SETTING, fd)
		print('Template was created')

	print('RL:{} QT:{} AM:{}'.format(SETTING['RELOAD'], SETTING['QUITE'], SETTING['ADMIN_MODE']))

	MAIN_TYPE = SETTING['MAIN_TYPE']

	print('Admin key is: {}'.format(SETTING['ADMIN_KEY']))

	ADMIN_KEY = SETTING['ADMIN_KEY']

	try:
		if SETTING['SRV'] == 'gevent':
			from gevent import monkey; monkey.patch_all()
			run(server=SETTING['SRV'], host=SETTING['IP'],
					port=SETTING['PORT'], quiet=SETTING['QUITE'],
					reloader=SETTING['RELOAD'],
					keyfile=SETTING['SSL']+'privkey.pem',
					certfile=SETTING['SSL']+'fullchain.pem')
		else:
			run(server=SETTING['SRV'], host=SETTING['IP'], port=SETTING['PORT'], quiet=SETTING['QUITE'], reloader=SETTING['RELOAD'])
	except BrokenPipeError:
		print('Someone disconect!')

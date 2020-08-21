#codec=utf-8
import pages
import sqlite3
from bottle import route, run, static_file, abort, post, response, request, redirect, error
from os import listdir
from random import choice
from json import load, dump


ADMIN_KEY = ''
ADMIN_ON = False

CHAR_DICT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
db = sqlite3.connect('db')


def _optimize(text):
	return text.replace('\n', '').replace('\t', '')


def prepare_main(text, header=''):
	return _optimize(pages.main_page.format(header+text))
	

def prepare_err(text, ico):
	return _optimize(pages.main_page.format(pages.error.format(text, ico)))


def concat(text, *args):
	"""
	Concat multiple strings

	:param text: Initial text
	:param args: Secondary texts
	"""
	ret = text
	for i in args:
		ret += str(i)
	return ret
	
	
def get_header(c_request):
	"""
	Check admin mode status and generate header
	
	:param c_request: gotted request
	"""
	header = ''
	if ADMIN_ON:
		header = pages.header.format(pages.admin_button)
		if c_request.get_cookie('admin') == ADMIN_KEY:
			header += pages.admin_yes.format(choice(listdir('static/admin')))
	else:
		header = pages.header.format('')
	return header
	

def get_flag(id):
	cursor = db.cursor()
	flag = ''
	if cursor.execute('select * from lang where id_hentai=?;', (id, )).fetchone() is not None:
		flag = pages.flag_ua
	cursor.close()
	return flag
	

@route('/static/<file:path>')
def load_static(file):
	return static_file(file, 'static')


@route('/hentai/<file:path>')
def load_hentai(file):
	return static_file(file, 'hentai', 'image/jpg')


def db_work(func):
	def wrap(*a, **ka):
		cursor = db.cursor()
		ret = func(*a, cursor=cursor, **ka)
		cursor.close()
		return ret
	return wrap
	

@db_work
def get_manga(sql, param='', cursor=''):
	"""
	:param sql: sql query to get id, name, dir
	:param param: tuple param to sql
	"""
	if cursor == '':
		abort(500)
	ind = cursor.execute(sql, param).fetchall()
	content = '<div class=wrap>'
	for row in ind:
		content += f'''
			<div class=block>
			{get_flag(row[0])}
			<a href=/manga/{row[0]}>
			<img class=image src="/hentai/{row[2]}/
			{sorted(listdir('hentai/'+row[2]))[0]}">
			</a>
			<div class=caption>{row[1]}</div>
			</div>'''
	content += '</div>'
	return content


@route('/')
def index():
	return prepare_main(get_manga('select id,name,dir from hentai;'), get_header(request))


@route('/genres/<id:int>')
def genres(id):
	return prepare_main(
		get_manga(
			'select id,name,dir from hentai,hentai_genres where id_hentai=id and id_genres=?;',
			(id, )),
		get_header(request))
	
	
@route('/lang/<id:int>')
def lang(id):
	return prepare_main(
		get_manga('select id, name, dir from hentai, lang where id_hentai = id;'),
		get_header(request))


@route('/manga/<id:int>')
@db_work
def manga(id, cursor):
	cursor.execute('select name,dir from hentai where id=?;', (id,))
	res = cursor.fetchone()
	if res is not None:
		content = f'''
				<div class=name style="margin: 15px 0;">{res[0]}</div>
				<div><div class=block>{get_flag(id)}<a href=/show/{id}>
				<img class=image src="/hentai/
				{res[1]}/{sorted(listdir('hentai/' + res[1]))[0]}"></a>
				</div><div class=disc>'''
		genres = cursor.execute('select id_genres from hentai_genres'
		' where id_hentai=?;', (id,)).fetchall()
		for genre in genres:
			cursor.execute('select id,name from genres where id=?;', (genre[0],))
			genre_info = cursor.fetchone()
			content += f'''
					<a class=genre href=/genres/{genre_info[0]}>
					{genre_info[1]}
					</a>'''

		if request.get_cookie('admin') == ADMIN_KEY:
			content += f'<div class="w3-row" style="width:480px;">' \
				'<div class="w3-half">' \
				'<form class="w3-container" method="post" action="/a_add">' \
				'<input type="hidden" name=id value={id}>'\
				'<select multiple size=15 name="genres">'

			genres_full = cursor.execute('select id, name from genres;').fetchall()
			genres_exclude = [i for i in genres_full if (i[0],) not in genres]
			genres_x = [i for i in genres_full if (i[0],) in genres]

			for genre_i in genres_exclude:
				content += f'<option value="{genre_i[0]}">{genre_i[1]}</option>'
			content += f'</select><br><button class="w3-button '\
				'w3-dark-gray" type="submit">Додати</button></form></div>'\
				'<div class="w3-half">'\
				'<form class="w3-container" method="post" action="/a_del">'\
				'<input type="hidden" name=id value={id}>'\
				'<select multiple size=15 name="genres">'

			for genre_i in genres_x:
				content += f'<option value="{genre_i[0]}">{genre_i[1]}</option>'

			content += '</select><br><button class="w3-button w3-dark-gray"'\
				' type="submit">Видалити</button></form></div></div>'
		content += f'</div><div><a href=/><img class=control src=/static/ico/la.png>' \
			'</a> <a href=/show/{id}><img class=control src=/static/ico/ra.png>' \
			'</a></div>'
		return prepare_main(content, get_header(request))
	else:
		cursor.close()
		abort(500)


@route('/show/<id:int>')
@db_work
def show(id, cursor):
	dir = cursor.execute('select dir from hentai where id=?;', (id, )).fetchone()[0]
	content = ''
	for img in sorted(listdir('hentai/' + dir)):
		content += f'<img class=imgs src="/hentai/{dir}/{img}"><br>'
	return prepare_main(pages.show.format(content))


@route('/a')
def admin():
	if ADMIN_ON:
		if request.get_cookie('admin') == ADMIN_KEY:
				return prepare_main(pages.admin_mode, get_header(request))
		else:
			admin_welcome = choice(pages.admin_welcome)
			admin_enter = choice(pages.admin_enter)
			return prepare_main(pages.admin.format(admin_welcome, admin_enter), get_header(request))
	else:
		abort(404)
		
		
def admin_test(func):
	def wrap(*a, **ka):
		if ADMIN_ON:
			if request.get_cookie('admin') == ADMIN_KEY:
				try:
					return func(*a, **ka)
				except KeyError:
					abort(404)
			else:
				abort(401)
		else:
			abort(404)
	return wrap


@post('/a')
def admin_post():
	if ADMIN_ON:
		if request.POST['key'] == ADMIN_KEY:
			response.set_cookie('admin', ADMIN_KEY)
			redirect('/')
		else:
			abort(401)
	else:
		abort(404)


@post('/a_add')
@admin_test
def admin_add():
	cursor = db.cursor()
	for genre in request.forms.getall('genres'):
		cursor.execute('insert into hentai_genres values(?, ?);',
				(request.POST['id'], genre))
	cursor.close()
	db.commit()
	redirect('/manga/{}'.format(request.POST['id']))


@post('/a_del')
@admin_test
def admin_del():
	cursor = db.cursor()
	for genre in request.forms.getall('genres'):
		cursor.execute('delete from hentai_genres where id_hentai=? '
					'and id_genres=?;', (request.POST['id'], genre))
	cursor.close()
	db.commit()
	redirect('/manga/{}'.format(request.POST['id']))
		

@post('/a_am')
@admin_test
def admin_add_manga():
	cursor = db.cursor()
	cursor.execute('insert into hentai values(null, ?, ?);',
		(request.forms.name,
		request.forms.dir))
	cursor.close()
	db.commit()
	redirect('/a')
	
	
@post('/a_at')
@admin_test
def admin_add_tag():
	cursor = db.cursor()
	cursor.execute('insert into genres values(null, ?);',
		(request.forms.name, ))
	cursor.close()
	db.commit()
	redirect('/a')
		
		
@route('/about')
def about():
	return prepare_main(pages.about, get_header(request))


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
	SETTING = None
	RELOAD = False
	QUITE = True
	IP = '127.0.0.1'
	SERVER = 'wsgiref'
	try:
		with open('conf.json', 'r') as fd:
			SETTING = load(fd)
	except FileNotFoundError:
		print('Config not found! Creating template...')
		with open('conf.json', 'w') as fd:
			dump({'ADMIN_KEY': '', 'ADMIN_MODE': False, 'RELOAD': False, 'QUITE': True, 'IP': '127.0.0.1', 'SRV': 'wsgiref'}, fd)
		print('Template was created')
	if SETTING is not None:
		RELOAD = SETTING['RELOAD']
		QUITE = SETTING['QUITE']
		ADMIN_KEY = SETTING['ADMIN_KEY']
		ADMIN_ON = SETTING['ADMIN_MODE']
		IP = SETTING['IP']
		SERVER = SETTING['SRV']
		print('Config was load')
	else:
		print('Config not loaded')
	print(f'RL:{RELOAD} QT:{QUITE} AM:{ADMIN_ON}')

	if ADMIN_KEY == '':
		ADMIN_KEY = ADMIN_KEY.join(choice(CHAR_DICT) for i in range(32))
	print(f'Admin key is: {ADMIN_KEY}')

	try:
		run(server=SERVER, host=IP, port=80, quiet=QUITE, reloader=RELOAD)
	except BrokenPipeError:
		print('Someone disconect!')

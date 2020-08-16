import pages
import sqlite3
from bottle import route, run, static_file, abort, post, response, request, redirect, error
from os import listdir
from random import choice


ADMIN_KEY = '1'
ADMIN_ON = True

CHAR_DICT = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
db = sqlite3.connect('db')


def prepare_str(text, *args):
	"""
	Optimize templates and format it

	Parameters:
		text (String): Templates string
		args (any): What will be added to text
	"""
	return text.format(*args).replace('\n', '').replace('\t', '')


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


@route('/static/<file:path>')
def load_static(file):
	return static_file(file, 'static')


@route('/hentai/<file:path>')
def load_hentai(file):
	return static_file(file, 'hentai', 'image/jpg')


@route('/')
def index():
	cursor = db.cursor()
	content = ''
	if ADMIN_ON:
		content = pages.admin_header
		if request.get_cookie('admin') == ADMIN_KEY:
			content += pages.admin_yes.format(choice(listdir('static/admin')))
	content += '<div class=wrap>'
	for row in cursor.execute('select id,name,dir from hentai;'):
		content = concat(content, '<div class=block><a href=/manga/',
				row[0], '><img class=image src="/hentai/',
				row[2], '/', listdir('hentai/'+row[2])[0],
				'"></a><div class=caption>', row[1], '</div></div>')
	content += '</div>'
	cursor.close()
	return prepare_str(pages.main_page, content)


@route('/manga/<id:int>')
def manga(id):
	cursor = db.cursor()
	cursor.execute('select name,dir from hentai where id=?;', (id,))
	res = cursor.fetchone()
	content = ''
	if ADMIN_ON:
		content = pages.admin_header
		if request.get_cookie('admin') == ADMIN_KEY:
			content += pages.admin_yes.format(choice(listdir('static/admin')))
	content = concat(content, '<div class=name>', res[0],
						'</div><div><div class=block><a href=/show/',
						id, '><img class=image src="/hentai/',
						res[1], '/', listdir('hentai/' + res[1])[0],
						'"></a></div><div class=disc>')
	genres = cursor.execute('select id_genres from hentai_genres'
	' where id_hentai=?;', (id,)).fetchall()
	for genre in genres:
		cursor.execute('select id,name from genres where id=?;', (genre[0],))
		genre_info = cursor.fetchone()
		content = concat(content, '<a id=genre href=/genres/',
			genre_info[0], '>', genre_info[1], '</a> ')
	content += '<div class="w3-row" style="width:480px;">' \
		'<div class="w3-half">' \
		'<form class="w3-container" method="post" action="/a_add">' \
		'<input type="hidden" name=id value={}>'\
		'<select multiple size=15 name="genres">'.format(id)

	genres_full = cursor.execute('select id, name from genres;').fetchall()
	genres_exclude = [i for i in genres_full if (i[0],) not in genres]
	genres_x = [i for i in genres_full if (i[0],) in genres]

	for genre_i in genres_exclude:
		content += '<option value="{}">{}</option>'.format(genre_i[0], genre_i[1])
	content += '</select><br><button class="w3-button '\
		'w3-dark-gray" type="submit">Додати</button></form></div>'\
		'<div class="w3-half">'\
		'<form class="w3-container" method="post" action="/a_del">'\
		'<input type="hidden" name=id value={}>'\
		'<select multiple size=15 name="genres">'.format(id)

	for genre_i in genres_x:
		content += '<option value="{}">{}</option>'.format(genre_i[0], genre_i[1])

	content += '</select><br><button class="w3-button w3-dark-gray"'\
		' type="submit">Видалити</button></form></div></div></div><div>'\
		'<a href=/><img class=control src=/static/ico/la.png></a> '\
		'<a href=/show/{}'\
		'><img class=control src=/static/ico/ra.png></a></div>'.format(id)
	cursor.close()
	return prepare_str(pages.manga, content)


@route('/genres/<id:int>')
def genres(id):
	cursor = db.cursor()
	mangas = cursor.execute('select id,name,dir from hentai,hentai_genres '
							'where id_hentai=id and id_genres=?;', (id, ))\
							.fetchall()
	content = ''
	if ADMIN_ON:
		content = pages.admin_header
		if request.get_cookie('admin') == ADMIN_KEY:
			content += pages.admin_yes.format(choice(listdir('static/admin')))
	else:
		content = '<a href=/><img class="home control" src=/static/ico/home.png></a>'
	content += '<div class=wrap>'
	for manga in mangas:
		content = concat(content, '<div class=block><a href=/manga/',
						manga[0], '><img class=image src="/hentai/',
						manga[2], '/', listdir('hentai/'+manga[2])[0],
						'"></a><div class=caption>', manga[1], '</div></div>')
	content += '</div>'
	cursor.close()
	return prepare_str(pages.genres, content)


@route('/show/<id:int>')
def show(id):
	cursor = db.cursor()
	dir = cursor.execute('select dir from hentai where id=?;', (id, )).fetchone()[0]
	content = ''
	for img in listdir('hentai/' + dir):
		content += '<img id=imgs src="/hentai/' + dir + '/' + img + '"><br>'
	cursor.close()
	return prepare_str(pages.show, content)


@route('/a')
def admin():
	if ADMIN_ON:
		admin_welcome = choice(pages.admin_welcome)
		admin_enter = choice(pages.admin_enter)
		return prepare_str(pages.admin, admin_welcome, admin_enter)
	else:
		abort(404)


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


@error(404)
def err404(error):
	return prepare_str(pages.error, 'Як ти сюди потрапив?', '404.png')


@error(500)
def err500(error):
	return prepare_str(pages.error, 'Або ти лізеж куди не треба, або у нас '
		'полетіла БД. І якщо це так то пізно срати. '
		'Може полагодим скоро, може ні', '500.png')


if __name__ == '__main__':
	if ADMIN_KEY == '':
		ADMIN_KEY = ADMIN_KEY.join(choice(CHAR_DICT) for i in range(32))
	print('Admin key is:{}'.format((ADMIN_KEY,)))
	run(host='127.0.0.1', port=80, debug=True)

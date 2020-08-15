import pages
import sqlite3
from bottle import route, run, static_file
from os import listdir


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
	content = '<div class=wrap>'
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
	content = concat('<div class=name>', res[0],
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

	content = concat(content, '</div></div><div><a href=/><img class=control '
		'src=/static/ico/la.png></a> <a href=/show/', id,
		'><img class=control src=/static/ico/ra.png></a></div>')
	cursor.close()
	return prepare_str(pages.manga, content)


@route('/genres/<id:int>')
def genres(id):
	cursor = db.cursor()
	mangas = cursor.execute('select id,name,dir from hentai,hentai_genres '
							'where id_hentai=id and id_genres=?;', (id, ))\
							.fetchall()
	content = '<div class=wrap>'
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


if __name__ == '__main__':
	run(host='127.0.0.1', port=80, debug=True)

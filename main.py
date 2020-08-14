import pages
import sqlite3
from bottle import route, run
from os import listdir


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
		ret += i
	return ret


@route('/')
def index():
	cursor = sqlite3.connect('db').cursor()
	content = '<div class=wrap>'
	for row in cursor.execute('select id,name,dir from hentai;'):
		concat(content, '<div class=block><a href=manga/',
				row[0], '><img class=image src="hentai/',
				row[2], '/', listdir('hentai/'+row[2])[0],
				'"></a><div class=caption>', row[1], '</div></div>')
	return prepare_str(pages.main_page)


@route('/manga/<name>')
def manga(name='Syka'):
	return prepare_str(pages.zzz_test, name, 'po', 'jo')


if __name__ == '__main__':
	run(host='127.0.0.1', port=80, debug=True)

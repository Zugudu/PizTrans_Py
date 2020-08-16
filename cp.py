#codec=utf-8
from bottle import route, run, post, request, redirect
from main import _optimize
from json import load, dump


cp = '''
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" href="../static/css/w3.css">
</head>
<body>
<center>
<form method="post" class="w3-padding">
<table>
<tr>
	<th><label class="we-medium" style="display: table-cell;vertical-align: middle;padding-right:10px;">Admin key</label></th>
	<th><input type="text" class="w3-input" style="display: table-cell;" name="ADK" value="{}"></th>
</tr>
<tr>
	<th><label class="we-medium" style="display: table-cell;vertical-align: middle;padding-right:10px;">IP</label></th>
	<th><input type="text" class="w3-input" style="display: table-cell;" name="IP" value="{}"></th>
</tr>
<tr>
	<th><label class="we-medium" style="display: table-cell;vertical-align: middle;padding-right:10px;">Reload</label></th>
	<th><input type="checkbox" class="toggle" style="display: table-cell;" {} name="RLD"></th>
</tr>
<tr>
	<th><label class="we-medium" style="display: table-cell;vertical-align: middle;padding-right:10px;">Quite</label></th>
	<th><input type="checkbox" class="toggle" style="display: table-cell;" {} name="QUT"></th>
</tr>
<tr>
	<th><label class="we-medium" style="display: table-cell;vertical-align: middle;padding-right:10px;">Admin mode</label></th>
	<th><input type="checkbox" class="toggle" style="display: table-cell;" {} name="ADM"></th>
</tr>
<tr>
	<th style="padding-top:10px;" colspan="2"><button class="w3-button w3-light-gray w3-border" type="submit">Внести зміни</button></th>
</tr>
</table>
</form>
</center>
</body>
</html>
'''


@route('/')
def index():
	try:
		SETTING = None
		with open('conf.json', 'r') as fd:
			SETTING = load(fd)
		RLD = ''
		QUT = ''
		ADM = ''
		ADK = SETTING['ADMIN_KEY']
		IP = SETTING['IP']
		if SETTING['RELOAD']:
			RLD = 'checked'
		if SETTING['QUITE']:
			QUT = 'checked'
		if SETTING['ADMIN_MODE']:
			ADM = 'checked'
		return _optimize(cp.format(ADK, IP, RLD, QUT, ADM))
	except FileNotFoundError:
		print('Config not found! Creating template...')
		with open('conf.json', 'w') as fd:
			dump({'ADMIN_KEY': '', 'ADMIN_MODE': False, 'RELOAD': False, 'QUITE': True, 'IP': '127.0.0.1'}, fd)
		print('Template was created')
		return _optimize(cp.format('', '127.0.0.1', '', 'checked', ''))


@post('/')
def i_post():
	flags = [False] * 3
	if request.forms.get('RLD'):
		flags[0] = True
	if request.forms.get('QUT'):
		flags[1] = True
	if request.forms.get('ADM'):
		flags[2] = True
	with open('conf.json', 'w') as fd:
		dump({'ADMIN_KEY': request.forms.get('ADK', ''), 'ADMIN_MODE': flags[2],
				'RELOAD': flags[0],
				'QUITE': flags[1], 'IP': request.forms.get('IP', '127.0.0.1')}, fd)
	redirect('/')


if __name__ == '__main__':
	print('Control panel started on http://127.0.0.1:4240/')
	run(host='127.0.0.1', port=4240, quiet=True)
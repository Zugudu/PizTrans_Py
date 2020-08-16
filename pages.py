main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name=viewport width=device-width>
<link rel="stylesheet" href="/static/css/w3.css">
<link rel="stylesheet" href="static/css/style.css" />
<link rel="stylesheet" media="(max-device-width:480px)" 
href="static/css/mob.css"/>
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


manga = '''
<html>
<head>
<meta charset=utf8>
<link rel="stylesheet" href="/static/css/style.css" />
<link rel="stylesheet" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<link rel="stylesheet" href="/static/css/w3.css">
<style>
@font-face
{{
	font-family: Anime;
	src: url(/static/css/a.ttf);
}}
.name
{{
	margin: 15px 0;
}}
.block
{{
	display: inline-block;
}}
</style>
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


genres = '''
<html>
<head>
<meta charset=utf8>
<meta name=viewport width=device-width>
<link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<link rel="stylesheet" href="/static/css/w3.css">
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


show = '''
<html>
<head>
<meta charset=utf8>
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
<link rel="stylesheet" type="text/css" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<link rel="stylesheet" href="/static/css/w3.css">
</head>
<body>
<center>
<a href=/><img class="control home" src=/static/ico/home.png></a>
{}
</center>
</body>
</html>
'''


admin = '''
<html>
<head>
	<meta charset=utf8>
	<link rel="stylesheet" href="/static/css/w3.css">
</head>
<body>
<div class="w3-bar">
	<a href=/><button class="w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red anime">Home</button></a>
	<a href=/a><button class="w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red anime">Admin</button></a>
</div>
<div class="w3-xlarge w3-padding w3-center">{}</div>
<div class="w3-container" style="width:50%;margin:auto;">
	<form method="post">
		<input type="text" class="w3-input" name="key" placeholder="{}">
		<button class="w3-button w3-dark-gray w3-margin-top w3-block" type="submit">Підтвердити</button>
	</form>
</div>
</body>
</html>
'''


admin_header = '''
<div class="w3-bar">
	<a href=/><button class="w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Home</button></a>
	<a href=/a><button class="w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Admin</button></a>
</div>
'''
admin_yes = '<div class="admin-status"><img height=128px src="/static/admin/{}"></div>'
admin_welcome = ('Скільки годин?', 'Три останні цифри числа Пі', 'Я тебе звати?', 'CVV2 код твоєї картки', 'Що ти тут забув?', 'Як ти сюди потрапив?', 'Схоже я забув вимкнути відображення цієї сторінки...', 'Семпаю, тільки не ламай нічого')
admin_enter = ('Сасай кудасай', 'Чємуске', 'Пароль:root', 'Введіть сюди 4225', '42')


error = '''
<html>
<head>
<meta charset=utf8>
<link rel="stylesheet" href="/static/css/w3.css">
</head>
<body>
<center>
<div class='w3-container' style='width:50%;'>
<div class="w3-container w3-red w3-padding">{}</div>
<img src="/static/ico/{}"><br>
<a href="/" class="w3-button w3-block w3-dark-gray w3-margin-top">Назад</a>
</div>
</center>
</body>
</html>
'''
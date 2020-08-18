#codec=utf-8
main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name=viewport width=device-width>
<link rel="stylesheet" href="/static/css/w3.css">
<link rel="stylesheet" href="/static/css/style.css" />
<link rel="stylesheet" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<title>Piztrans</title>
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


main_plain = '''
<html>
<head>
<meta charset=utf8>
<meta name=viewport width=device-width>
<link rel="stylesheet" href="/static/css/w3.css">
<title>Piztrans</title>
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


show = '<a href=/><img class="control home" src=/static/ico/home.png></a>{}'


admin = '''
<div class="w3-xlarge w3-padding w3-center">{}</div>
<div class="w3-container" style="width:50%;margin:auto;">
	<form method="post">
		<input type="text" class="w3-input" name="key" placeholder="{}">
		<button class="w3-button w3-dark-gray w3-margin-top w3-block" type="submit">Підтвердити</button>
	</form>
</div>
'''


header = '''
<div class="w3-bar">
	<a href=/><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Головна</button></a>
	{}
	<a href=/about><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Про нас</button></a>
</div>
'''
admin_button = '<a href=/a><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Адмінка</button></a>'
admin_yes = '<div class="admin-status"><img height=128px src="/static/admin/{}"></div>'
admin_welcome = ('Скільки годин?', 'Три останні цифри числа Пі', 'Я тебе звати?', 'CVV2 код твоєї картки', 'Що ти тут забув?', 'Як ти сюди потрапив?', 'Схоже я забув вимкнути відображення цієї сторінки...', 'Семпаю, тільки не ламай нічого')
admin_enter = ('Сасай кудасай', 'Чємуске', 'Пароль:root', 'Введіть сюди 4225')


error = '''
<div class='w3-container' style='width:50%;'>
<div class="w3-container w3-red w3-padding">{}</div>
<img src="/static/ico/{}"><br>
<a href="/" class="w3-button w3-block w3-dark-gray w3-margin-top">Назад</a>
</div>
'''


about = '''
<div class="w3-medium w3-padding" style="width:880px;">
Привіт, як ти вже встиг помітити, ти знаходишся на сайті з хєнтаєм.<br>Весь код є власністю Клубу Кібернетики Коледжу (ККК)<br>
Розробкою сайту займалися:
<ul class="w3-ul w3-border w3-light-gray w3-margin w3-hoverable" style="width:300px;">
<a href="https://github.com/Zugudu" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><li style="border-bottom:1px solid #ddd;" class="anime">Ісус</li></a>
<li class="anime">Шурік</li>
<a href="https://myanimelist.net/profile/s0fko" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><li class="anime">s0fko</li></a>
</ul>
</div>
'''
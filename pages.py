#codec=utf-8
main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name=keywords content="хєнтай, хентай, манга, hentai, manga, порно, комикси, комікси">
<link rel="stylesheet" href="/static/css/w3.css">
<link rel="stylesheet" href="/static/css/style.css" />
<link rel="stylesheet" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<title>uHentai</title>
</head>
<body>
<center>
{}
</center>
</body>
</html>
'''


show = '<a href="/manga/{}"><img class=home src="/static/ico/home.png"></a>{}'
show_book = '<a href="{}"><img class=imgs src="/hentai/{}/{}"></a><br>'
genre_button = '<a class=genre href=/genres/{}>{}</a>'


manga = '''
<div class="name" style="margin: 15px 0;">{}</div>
<div>
<div class="block">{}<a href="/show/{}"><img class="image" src="/hentai/{}/{}"></a></div>
<div class="disc">{}</div>
<div>
<a class="w3-button w3-blue w3-mobile read-btn" href="/show/{}/0">Читати немов книгу</a>
<a class="w3-button w3-blue w3-mobile read-btn" href="/show/{}">Читати немов сувій</a>
</div>
</div>
'''


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
	<a href=/genres><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Жанри</button></a>
	{}
	<a href=/about><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Про нас</button></a>
</div>
'''


admin_mode = '''
<div>
<div style="width:300px;display:inline-block;padding-right:20px;">
	<form method="post" class="w3-padding" action="a_am">
		<div class="w3-medium" style="padding-bottom:16px;"><b>Додати мангу</b></div>
		<div><input type="text" class="w3-input" style="display: table-cell;" name="name" placeholder="Назва"></div>
		<div><input type="text" class="w3-input" style="display: table-cell;" name="dir" placeholder="Місцезнаходження"></div>
		<div style="padding-top:10px;"><button class="w3-button w3-light-gray w3-border" type="submit">Додати</button></div>
	</form>
</div>
<div style="width:300px;display:inline-block;">
	<form method="post" class="w3-padding" action="a_at">
		<div class="w3-medium" style="padding-bottom:16px;"><b>Додати тег</b></div>
		<div><input type="text" class="w3-input" style="display: table-cell;" name="name" placeholder="Назва"></div>
		<div style="padding-top:10px;"><button class="w3-button w3-light-gray w3-border" type="submit">Додати</button></div>
	</form>
</div>
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
<div class="w3-medium w3-padding" style="width:90%;">
Привіт, як ти вже встиг помітити, ти знаходишся на сайті з хєнтаєм.<br>Весь код є власністю Клубу Кібернетики Коледжу (ККК)<br>
Зворотній зв'язок <a href="https://t.me/Zugudu" target="_blank" rel="noopener noreferrer" class="w3-text-blue">@Zugudu</a><br>
Розробкою сайту займалися:
<ul class="w3-ul w3-border w3-light-gray w3-margin w3-hoverable" style="width:300px;">
<a href="https://github.com/Zugudu" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><li style="border-bottom:1px solid #ddd;" class="anime" title="Програміст, прости Госоподи веб-дизайнер, системний адміністратор, спеціаліст інформаційної безпеки і просто хороша людина">Ісус</li></a>
<li class="anime w3-hover-none" title="Додавання та присвоєння жанрів">Шурік</li>
<a href="https://myanimelist.net/profile/s0fko" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><li class="anime" title="Переклад хентаю українською">s0fko</li></a>
</ul>
</div>
'''


flag_ua = '<a href="/lang/1" class="flag"><div class="flag-231 w3-blue"></div><div class="flag-232 w3-yellow"></div></a>'
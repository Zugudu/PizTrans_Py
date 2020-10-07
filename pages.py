#codec=utf-8
w3_button = 'anime w3-button w3-medium w3-bar-item w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red'


main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name=keywords content="хєнтай хентай манга манґа мангу манґу hentai manga порно комикси комікси українською читати онлайн юхентай uhentai">
<meta name="description" content="Сайт присвячений перекладу манґи та хентаю українською, командою Юманго"> 
<link rel="stylesheet" href="/static/css/w3.css">
<link rel="stylesheet" href="/static/css/style.css" />
<link rel="stylesheet" media="(max-device-width:480px)" href="/static/css/mob.css"/>
<link rel="icon" type="image/png" href="/static/ico/logo.png">
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
genre_button = '<a class=genre href=/search/{}/{}>{}</a>'


manga = '''
<div class="name" style="margin: 15px 0;">{}</div>
<div>
<div class="block">{}<a href="/show/{}"><img class="image" src="/hentai/{}/{}"></a></div>
<div class="disc">{}</div>
<div>
{}
</div>
</div>
'''


header = '''
<div class="w3-bar w3-margin-bottom">
	<a href=/><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Головна</button></a>
	<a href=/{}><button class="anime w3-button w3-medium w3-bar-item w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red w3-bottombar">{}</button></a>
  	<div class="dropdown">
		<button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red" style="float: none;">Пошук за:</button>
		<div class="dropdown_content">
			<a href="/list/chars" class="anime w3-button w3-mobile w3-blue read-btn" style="border-bottom: #000 solid 1px">персонажем</a>
			<a href="/list/series" class="anime w3-button w3-mobile w3-blue read-btn" style="border-bottom: #000 solid 1px">серією мальописів</a>
			<a href="/list/genres" class="anime w3-button w3-mobile w3-blue read-btn" style="border-bottom: #000 solid 1px">жанром</a>
			<a href="/list/comands" class="anime w3-button w3-mobile w3-blue read-btn">перекладачем</a>
		</div>
	</div>
	{}
	<a href=/about><button class="anime w3-button w3-medium w3-bar-item w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red w3-bottombar">Про нас</button></a>
	<a href=/friend><button class="anime w3-button w3-medium w3-bar-item w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red w3-bottombar">Наші друзі</button></a>
</div>
'''


admin_mode = '''
<a href=/a_manga><div class="w3-button w3-light-gray w3-border">Додати нову манґу</div></a><hr>
<div>
{}
</div>
'''


admin_mode_el = '''
<div style="width:300px;display:inline-block;">
	<form method="post" class="w3-padding" action="a_a/{0}">
		<div class="w3-medium" style="padding-bottom:16px;"><b>Додати {1}</b></div>
		<div><input type="text" class="w3-input" style="display: table-cell;" name="name" placeholder="Назва"></div>
		<div style="padding-top:10px;"><button class="w3-button w3-light-gray w3-border" type="submit">Додати</button></div>
	</form>
	<form method="post" class="w3-padding" action="a_d/{0}">
		<div class="w3-medium" style="padding-bottom:16px;"><b>Видалити {1}</b></div>
		<select multiple size=15 name='el'>{2}</select>
		<div style="padding-top:10px;"><button class="w3-button w3-light-gray w3-border" type="submit">Видалити</button></div>
	</form>
</div>
'''


admin_button = '<a href=/a><button class="anime w3-button w3-medium w3-bar-item w3-bottombar w3-border-blue w3-hover-none w3-hover-text-black w3-hover-border-red">Адмінка</button></a>'
admin_yes = '<div class="admin-status"><img height=128px src="/static/admin/{}"></div>'


error = '''
<div class='w3-container error'>
<div class="w3-container w3-red w3-padding">{}</div>
<img src="/static/ico/{}"><br>
<a href="/" class="w3-button w3-block w3-dark-gray w3-margin-top">Назад</a>
</div>
'''


error_head = '''
<div class="w3-container w3-red w3-padding">{}</div>
'''


about = '''
<div class="w3-medium" style="width:90%;">
Привіт, як ти вже встиг помітити, ти знаходишся на сайті з хентаєм.<br>Весь код є власністю Наукової ради з питань розвитку хентаю в Україні<br>
Зворотній зв'язок <a href="https://t.me/ukrMango" target="_blank" rel="noopener noreferrer" class="w3-text-blue">@ukrMango</a><br>
Розробкою сайту займалися:
<ul class="w3-ul w3-border w3-light-gray w3-margin w3-hoverable" style="width:300px;">
<li style="border-bottom:1px solid #ddd;" class="anime w3-hover-none" title="Програміст, прости Госоподи веб-дизайнер, системний адміністратор, спеціаліст інформаційної безпеки і просто хороша людина">Zugudu</li>
<li class="anime w3-hover-none" title="Додавання та присвоєння жанрів">Шурік</li>
<a href="https://myanimelist.net/profile/s0fko" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><li style="border-bottom:1px solid #ddd;" class="anime" title="Голова відділу перекладу">s0fko</li></a>
<li class="anime w3-hover-none" title="Вєб дезіґнер">MrSancho</li>
</ul>
Наші проєкти:
<div class='w3-row-padding w3-margin ' style='width:400px;'>
	<div class='w3-half'>
	<a href='https://uhentai.tk'>
	<div class='w3-card w3-padding anime w3-hover-light-gray' style="width:150px;">
		<img src='/static/ico/logo.svg' style="width:90px;margin:5px;"><br>
		Uhentai
	</div>
	</a>
	</div>
	<div class='w3-half'>
	<a href='https://umanga.tk'>
	<div class='w3-card w3-padding anime w3-hover-light-gray' style="width:150px;">
		<img src='/static/ico/logo.svg' style="width:90px;margin:5px;"><br>
		Umanga
	</div>
	</a>
	</div>
</div>
</div>
'''


friend = '''
<div class="w3-medium" style="width:90%;">
	<a href='https://otaku-first.online/' target="_blank" rel="noopener noreferrer">
	<div class='w3-card w3-padding anime w3-hover-light-gray' style="width:150px;">
		<img src='/static/fr_logo/fis.png' style="width:90px;margin:5px;"><br>
		Otaku-First
	</div>
	</a>
</div>
'''


add_manga = '''
<form action="/a_manga" method="post" enctype="multipart/form-data">
<table class=anime>
<tr><td align=right>Назва</td><td><input type="text" name="dir" /></td></tr>
<tr><td align=right>Zip архів з манґою</td><td><input type="file" name="zip" class="w3-button w3-light-gray w3-border"/></td></tr>
<tr><td colspan=2><center><button type="submit" class="w3-button w3-light-gray w3-border">Завантажити</button></center></td><tr>
</table>
</form>
'''


flag_ua = '<a href="/lang/1" class="flag"><div class="flag-231 w3-blue"></div><div class="flag-232 w3-yellow"></div></a>'


genre_group = '<div class="genre_group"><a class="symbol" name="{}">{}</a>'
genres_bottom_bar = '<a href="#{}" class="{} w3-topbar">{}</a>'


page_scroll = '''
<div class="page_scroll">
	<div style="visibility: {};">
		<a href="{}"><img src="/static/ico/double_arrow.svg"></a>
		<a href="{}"><img src="/static/ico/arrow.svg"></a>
	</div>
	<form class="ps_form" method="post">
		<input type="text" name="page" size="8" placeholder="{} з {}">
		<button type="submit">
			<img style="width: 19px; height: 19px;" src="/static/ico/lupa.svg">
		</button>
	</form>
	<div style="visibility: {};">
		<a href="{}"><img style="transform: rotate(180deg);" src="/static/ico/arrow.svg"></a>
		<a href="{}"><img style="transform: rotate(180deg);" src="/static/ico/double_arrow.svg"></a>
	</div>
</div>
'''


login = '''
<form method=POST class='w3-container w3-card w3-padding w3-margin' style='width:300px;'>
<label>Лоґін</label>
<input name='login' type='text' placeholder='Лоґін' class='w3-input'>
<label>Пароль</label>
<input name='pass' type='password' placeholder='Пароль' class='w3-input'>
<button class='w3-btn w3-black w3-block w3-margin-top' type='submit'>Увійти</button>
</form>
'''
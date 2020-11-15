#codec=utf-8
main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name=keywords content="хєнтай хентай манга манґа мангу манґу hentai manga порно комикси комікси українською читати онлайн юхентай uhentai">
<meta name="description" content="Сайт присвячений перекладу манґи та хентаю українською, командою Юманго">
<link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" media="(max-device-width:768px)" href="/static/css/mob.css"/>
<link rel="icon" type="image/png" href="/static/ico/logo.png">
<title>uHentai</title>
</head>
<body>
{}
</body>
</html>
'''


show = '<a href="/manga/{}"><img class="svg back-arrow" src="/static/ico/back_arrow.svg"></a><div class="container show-book">{}</div>'
show_book = '<div class="container show-book"><a href="{}"><img class="show__img" src="/hentai/{}/{}"></a></div>'


manga = '''
<div class="wrap container">
	<div class="font big-font block__title manga__title">{}</div>
	<div class="manga">
		{}
		<a href="/show/{}"><img class="block manga__block" src="{}"></a>
		<div>
			{}
		</div>
	</div>
	{}
'''


header = '''
<header class="header">
	<div class="header__body">
		<a class="svg logo" href="/">
			<img src="/static/ico/U_logo.svg">
		</a>
		<div class="font">UHentai</div>
			<input type="checkbox" id="burger">
			<label for="burger" class="mobile-menu">
				<div class="mobile-menu__button"><div></div></div>
			</label>
		<nav class="menu font">
			<ul class="menu__list">
				<li>
					<input type="checkbox" id="mobile-menu__search">
					<label for="mobile-menu__search" class="menu__link">
						Пошук за:
						<div class="mobile-menu__arrow"></div>
					</label>
					<ul class="sub-menu__list">
						<li><a class="sub-menu__link" href="/list/chars">персонажем</a></li>
						<li><a class="sub-menu__link" href="/list/series">серією мальописів</a></li>
						<li><a class="sub-menu__link" href="/list/genres">жанром</a></li>
						<li><a class="sub-menu__link" href="/list/comands">перекладачем</a></li>
					</ul>
				</li>
				<li><a class="menu__link" href=/about>Про нас</a></li>
				<li><a class="menu__link" href=/friend>Наші друзі</a></li>
				{}
			</ul>
		</nav>
	</div>
</div>
</header>
'''


admin_mode = '''
<div class="wrap container font">
	{}
</div>
'''


admin_mode_el = '''
<div class="list-block">
	<div class="list">
		<form method="post" action="a_a/{0}">
			<div>Додати {1}</div>
			<input class="font admin-input" type="text" name="name" size="19" placeholder="Назва">
			<button class="font button" type="submit">Додати</button>
		</form>
	</div>
	<div class="list">
		<form method="post" action="a_d/{0}">
			<div>Видалити {1}</div>
			<select multiple class="font list__select" name='el'>{2}</select>
			<button class="font button" type="submit">Видалити</button>
		</form>
	</div>
</div>
'''

template_btn = '<li><a class="menu__link" href=/{}>{}</a></li>'
admin_button = template_btn.format('a', 'Адмінка')
login_button = template_btn.format('login', 'Увійти')
exit_button = template_btn.format('exit', 'Вийти')
add_manga_button = template_btn.format('a_manga', 'Завантажити главу')

admin_yes = '<div class="admin-status"><img src="/static/admin/{}"></div>'


error = '''
<div class="error container">
	<div class="font big-font manga__font block__title manga__title">{}</div>
	<img class="error__img" src="/static/ico/{}"><br>
	<a href="/" class="font button">Назад</a>
</div>
'''


error_head = '''
<div class="font login__error">{}</div>
'''


about = '''
<div class="container wrap font">
	Привіт, як ти вже встиг помітити, ти знаходишся на сайті з хентаєм.<br>Весь код є власністю Наукової ради з питань розвитку хентаю в Україні<br><br>
	Якщо Ви бажаєте викладати у нас україномовні мальописи чи хентай<br>ми з радістю допоможемо Вам<br><br>
	Наш ТГ канал <a href="https://t.me/ukr_mango" target="_blank" rel="noopener noreferrer" class="link-font">ЮМанго</a><br>
	Зворотній зв'язок <a href="https://t.me/ukrMango" target="_blank" rel="noopener noreferrer" class="link-font">@ukrMango</a><br>
	Наші проєкти:
	<div>
		<a href='https://uhentai.tk'>
			<div class="font block img-href" style="width:150px;">
				<img src="/static/ico/logo.svg"><br>
				Uhentai
			</div>
		</a>
		<a href="https://umanga.tk">
			<div class="font block img-href" style="width:150px;">
				<img src="/static/ico/logo.svg"><br>
				Umanga
			</div>
		</a>
	</div>
</div>
'''


friend = '''
<div class="wrap container">
	<a href='https://otaku-first.online/' target="_blank" rel="noopener noreferrer">
	<div class="font block img-href">
		<img src="/static/fr_logo/fis.png"><br>
		Otaku-First
	</div>
	</a>
</div>
'''


add_manga = admin_mode.format('''
<form class="add-manga" action="/a_manga" method="post" enctype="multipart/form-data">
	<div>
		Назва
		<input class="font" type="text" name="dir"/>
	</div>
	<div>
		Zip архів з манґою
		<input type="file" name="zip"/>
	</div>
	<div>
		<button class="font button" type="submit" class="">Завантажити</button>
	</div>
</form>
''')


u_manga_edit = '''
<form class="add-manga" action="/c_name/{0}" method="post">
	<input class="font admin-input" type="text" name="name" placeholder="Нова назва"/><br>
	<button class="font button" type="submit" class="">Змінити назву</button>
</form><br>
<form class="add-manga font" action="/c_file/{0}" method="post" enctype="multipart/form-data" style="margin-top: 10px;">
	Zip архів з манґою <input type="file" name="zip"/><br>
	<button class="font button" type="submit" class="">Перезалити</button>
</form>
'''


flag_ua = ''


genre_group = '<div class="search-group"><a class="font big-font search-group__symbol" name="{}">{}</a>'
genre_button = '<a class="font button" href=/search/{}/{}>{}</a>'
bottom_bar_symbol = '<a href="#{}" class="font big-font bottom-bar__symbol">{}</a>'


page_scroll = '''
<div class="bottom-bar">
	<a href="/manga/{}"><img class="svg back-arrow" src="/static/ico/back_arrow.svg"></a>
	<div class="container page-scroll">
		<div class="page-scroll__group" style="visibility: {};">
			<a href="{}"><img class="svg page-scroll__svg" src="/static/ico/double_arrow.svg"></a>
			<a href="{}"><img class="svg page-scroll__svg" src="/static/ico/arrow.svg"></a>
		</div>
		<form class="page-scroll__group page-scroll__form" method="post">
			<input class="font" type="text" name="page" placeholder="{} з {}">
			<button type="submit">
				<img class="svg page-scroll__svg" src="/static/ico/lupa.svg">
			</button>
		</form>
		<div class="page-scroll__group" style="visibility: {}; transform: rotate(180deg)">
			<a href="{}"><img class="svg page-scroll__svg page-scroll__back-svg" src="/static/ico/double_arrow.svg"></a>
			<a href="{}"><img class="svg page-scroll__svg page-scroll__back-svg" src="/static/ico/arrow.svg"></a>
		</div>
	</div>
</div>
'''


login = '''
<div class="container wrap font">
{}
<form method=POST class="block block-not-hover login">
<label>Лоґін</label><br>
<input name='login' type='text' placeholder='Лоґін' class="admin-input font"><br>
<label>Пароль</label><br>
<input name='pass' type='password' placeholder='Пароль' class="admin-input font"><br>
<button class="button font" type='submit'>Увійти</button>
</form>
</div>
'''

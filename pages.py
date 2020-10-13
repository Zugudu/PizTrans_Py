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
<div class="content container">
	<div class="font big-font block__title manga__title">{}</div>
	<div class="manga">
		{}
		<a href="/show/{}"><img class="block manga__block" src="/hentai/{}/{}"></a>
		<div>
			{}
		</div>
	</div>
	{}
'''


admin = '''
<div class="content container">
	<div class="font">{}</div>
	<form method="post">
		<input type="text" size="20" class="font admin-input" name="key" placeholder="{}"><br>
		<button class="font button" type="submit">Підтвердити</button>
	</form>
</div>
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
				<li>{}</li>
			</ul>
		</nav>
	</div>
</div>
</header>
'''


admin_mode = '''
<div class="content container font">
	<a class="button" href=/a_manga>Додати нову манґу</a>
	<div>
	{}
	</div>
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


admin_button = '<a class="menu__link" href=/a>Адмінка</a>'
admin_yes = '<div class="admin-status"><img src="/static/admin/{}"></div>'
admin_welcome = ('Скільки годин?', 'Три останні цифри числа Пі', 'Як тебе звати?', 'CVV2 код твоєї картки', 'Що ти тут забув?', 'Як ти сюди потрапив?', 'Схоже, я забув вимкнути відображення цієї сторінки...', 'Семпаю, тільки не ламай нічого')
admin_enter = ('Сасай кудасай', 'Чємуске', 'Пароль:root', 'Введіть сюди 4225')


error = '''
<div class="error container">
	<div class="font big-font manga__font block__title manga__title">{}</div>
	<img class="error__img" src="/static/ico/{}"><br>
	<a href="/" class="font button">Назад</a>
</div>
'''


about = '''
<div class="container content font">
	Привіт, як ти вже встиг помітити, ти знаходишся на сайті з хентаєм.<br>Весь код є власністю Наукової ради з питань розвитку хентаю в Україні<br>
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
<div class="content container">
	<a href='https://otaku-first.online/' target="_blank" rel="noopener noreferrer">
	<div class="font block img-href">
		<img src="/static/fr_logo/fis.png"><br>
		Otaku-First
	</div>
	</a>
</div>
'''


add_manga = '''
<div class="font content container">
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
</div>
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

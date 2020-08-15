main_page = '''
<html>
<head>
<meta charset=utf8>
<meta name=viewport width=device-width>
<link rel="stylesheet" type="text/css" href="static/css/style.css" />
<link rel="stylesheet" type="text/css" media="(max-device-width:480px)" 
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
<link rel="stylesheet" type="text/css" href="/static/css/style.css" />
<link rel="stylesheet" type="text/css" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
<style>
@font-face
{{
	font-family: Anime;
	src: url(/static/css/a.ttf);
}}
div
{{
	margin: 15px 0;
	font: 100% Anime;
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
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
<link rel="stylesheet" type="text/css" media="(max-device-width:480px)" 
href="/static/css/mob.css"/>
</head>
<body>
<center>
<a href=/><img class="home control" src=/static/ico/home.png></a>
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
</head>
<body>
<center>
<a href=/><img class="control home" src=/static/ico/home.png></a>
{}
</center>
</body>
</html>
'''
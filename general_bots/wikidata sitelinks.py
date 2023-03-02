import pywikibot
from pywikibot.exceptions import NoPageError

src = pywikibot.Site('he', 'wikisource')
pedia = pywikibot.Site('he', 'wikipedia')

for page in src.allpages(start='חוק גיל'):
	print(page)
	try:
		pywikibot.ItemPage.fromPage(page)
	except NoPageError:
		pass
	else:
		continue
	if page.isRedirectPage():
		try:
			pywikibot.ItemPage.fromPage(page.getRedirectTarget())
		except NoPageError:
			pass
		else:
			continue
	
	pedia_page = pywikibot.Page(pedia, page.title())
	if not pedia_page.exists():
		continue
	
	try:
		item = pywikibot.ItemPage.fromPage(pedia_page)
	except NoPageError:
		continue
	try:
		item.getSitelink(src.dbName())
	except NoPageError:
		pass
	else:
		continue
	
	print('about to add', page, 'as a sitelink to', item.getID(), 'which is connected to [[w:' + pedia_page.title() + ']]')
	if pywikibot.input_yn('do you want to add?', 'n'):
		item.setSitelink(page, summary='Set sitelink ' + src.dbName())
		print('added!')
import pywikibot
from pywikibot.exceptions import NoPageError

src = pywikibot.Site('he', 'wikisource')
pedia = pywikibot.Site('he', 'wikipedia')

for page in src.allpages(start='בן סירב'):
	print(page)
	try:
		item = pywikibot.ItemPage.fromPage(page)
		continue
	except NoPageError:
		pass
	
	pedia_page = pywikibot.Page(pedia, page.title())
	if not pedia_page.exists():
		continue
	
	try:
		item = pywikibot.ItemPage.fromPage(pedia_page)
	except NoPageError:
		continue
	print('about to add', page, 'as a sitelink to', item.getID(), 'which is connected to [[w:'+ pedia_page.title()+']]')
	if pywikibot.input_yn('do you want to add?', 'n'):
		item.setSitelink(sitelink={'site': src.dbName(), 'title': page.title()}, summary='Set sitelink hewikisource')
		print('added!')

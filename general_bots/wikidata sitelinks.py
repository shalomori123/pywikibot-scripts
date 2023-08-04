import pywikibot
from pywikibot.exceptions import NoPageError

src = pywikibot.Site('he', 'wikisource')
pedia = pywikibot.Site('he', 'wikipedia')

for page in src.allpages(start='נחונ'):
	print(page)
	try:
		pywikibot.ItemPage.fromPage(page)
	except NoPageError:
		pass
	else:
		continue
	if page.isRedirectPage():
		target = page.getRedirectTarget()
		if target.namespace() == "ביאור:":
			continue
		try:
			pywikibot.ItemPage.fromPage(target)
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
	else:
		with open("dont_add_wikidata.csv", "a") as f:
			f.write("'"+page.title()+"',")

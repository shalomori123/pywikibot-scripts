import asyncio

from aioconsole import ainput
import pywikibot
from pywikibot.exceptions import NoPageError

src = pywikibot.Site('he', 'wikisource')
pedia = pywikibot.Site('he', 'wikipedia')
gen = src.allpages(start='נחונ')

async def do(page):
	print(page)
	try:
		pywikibot.ItemPage.fromPage(page)
	except NoPageError:
		pass
	else:
		return
	if page.isRedirectPage():
		target = page.getRedirectTarget()
		if target.namespace() == "ביאור:":
			return
		try:
			pywikibot.ItemPage.fromPage(target)
		except NoPageError:
			pass
		else:
			return
	
	pedia_page = pywikibot.Page(pedia, page.title())
	if not pedia_page.exists():
		return
	
	try:
		item = pywikibot.ItemPage.fromPage(pedia_page)
	except NoPageError:
		return
	try:
		item.getSitelink(src.dbName())
	except NoPageError:
		pass
	else:
		return
	
	print()
	user_input = await pywikibot.input_yn('about to add ' + page + ' as a sitelink to ' + item.getID() + 
			     ' which is connected to [[w:' + pedia_page.title() + ']]\n'
			     'do you want to add? (y / default-n) ')
	if user_input == 'y':
		item.setSitelink(page, summary='Set sitelink ' + src.dbName())
		print('added!')
	else:
		with open("dont_add_wikidata.csv", "a") as f:
			f.write("'"+page.title()+"',")

async def main():
	async for page in gen:
		await do(page)

asyncio.run(main)
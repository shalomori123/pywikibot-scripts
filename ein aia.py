import pywikibot
import re

site = pywikibot.Site()
mainmainpage = pywikibot.Page(site, 'עין איה')
mainpages = mainmainpage.linkedPages()
for mainpage in mainpages:
	print(mainpage.title())
	if not re.match('עין איה/שבת', mainpage.title()):
		continue
	pages = mainpage.linkedPages()
	x=''
	y=''
	for page in pages:
		if '|דף|עמוד}}' in page.text and page.exists():
			print(page.title())
			if 'פאה' in page.title():
				continue
			a = re.search('\{\{צתב\|(.*?)\|', page.text)
			try:
				print(a.expand('\\1'))
			except:
				print(page.text)
			daf = input('מה הדף? ')
			while not re.search('[א-ת]*', daf):
				daf = input('שגוי. נסה שנית: ')
			if not daf:
				daf = x
				amud = y
			else:
				x = daf
				amud = input('מה העמוד? ')
				while amud not in ['א', 'ב']:
					amud = input('שגוי. נסה שנית: ')
				y = amud
			page.text = page.text.replace('|דף|עמוד}}', '|%s|%s}}' % (daf, amud))
			page.save(summary='הוספת מספר הדף ידנית, בעזרת בוט')
print('perfect!')

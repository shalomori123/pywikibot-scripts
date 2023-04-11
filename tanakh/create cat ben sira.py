import pywikibot
from pywikibot import textlib

ALEPHBET = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא')
site = pywikibot.Site()

for i in ALEPHBET:
	cat = pywikibot.Page(site, 'קטגוריה:בן סירא '+i)
	if not cat.exists():
		cat.text = '[[קטגוריה:בן סירא]]'
		cat.save('יצירת דף קטגוריה')
	page = pywikibot.Page(site, 'בן סירא '+i)
	page.text += '\n' + cat.title(as_link=True)
	page.save('קטגוריה')

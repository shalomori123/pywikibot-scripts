import pywikibot

ALEPHBET = ('0', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז')
site = pywikibot.Site()

for i, letter in enumerate(ALEPHBET):
	page = pywikibot.Page(site, 'מלבי"ם על דברי הימים ב ' + letter)
	if not page.exists():
		continue
		print(page, 'skipped')
	page.text = '{{פרשן על פרק|מלבי"ם|דברי הימים ב|%s|%s|%s}}\n' % (ALEPHBET[i-1], letter, ALEPHBET[i+1]) + page.text
	page.save(summary = 'תבנית ניווט')
print('mission comleted!')
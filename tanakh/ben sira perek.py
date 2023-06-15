import pywikibot
import re
from pywikibot.textlib import extract_sections

ALEPHBET = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא')
from19 = [30,31,27,27,27,33,26,29,30,26,28,25,
31, 24, 33, 31, 26, 31, 31, 34, 35, 30,
22, 25, 33, 23, 26, 20, 25, 25, 16, 29, 30]

site = pywikibot.Site()

for i,letter in enumerate(ALEPHBET):
	if i < 22:
		continue
	perek = pywikibot.Page(site, 'בן סירא '+letter)
	
	sections = extract_sections(perek.text, site).sections
	for section in sections:
		if section.title.strip().strip('=').strip() == 'תרגום בן זאב':
			page = pywikibot.Page(site, 'בן סירא/בן זאב/'+letter)
			page.text += section.content
			page.save('מתוך דף הפרק')
		if section.title.strip().strip('=').strip() == 'מהדורת דוד כהנא (על בסיס המקור העברי מכתבי יד)':
			page = pywikibot.Page(site, 'בן סירא/דוד כהנא/'+letter)
			page.text += section.content
			page.save('מתוך דף הפרק')
	
	psukim = '\n==פסוקים==\n'
	temp = lambda x: '[[בן סירא '+letter+' '+x+'|'+x+']] {{*}} '
	if i >= 18:
		for j in range(from19[i-18]):
			psukim += temp(ALEPHBET[j])
	else:
		for j in ALEPHBET:
			page = pywikibot.Page(site, 'בן סירא '+letter+' '+j)
			if page.exists():
				psukim += temp(j)
	perek.text += psukim
	input(psukim)
	perek.save('קישורים לפסוקים')
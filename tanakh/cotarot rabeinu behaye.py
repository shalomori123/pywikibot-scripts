import pywikibot
import re

ALEPHBET = ('', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט',
'ס', 'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט',
'ע', 'עא', 'עב', 'עג', 'עד', 'עה', 'עו', 'עז', 'עח', 'עט',
'פ', 'פא', 'פב', 'פג', 'פד', 'פה', 'פו', 'פז', 'פח', 'פט')

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'רבינו בחיי על התורה')
for page in mainpage.linkedPages():
	if not page.exists():
		continue
	numbers = re.findall(r'Verse (\d\d?)', page.text)
	perek = page.title().replace('רבינו בחיי על ', '')
	for num in numbers:
		letter = ALEPHBET[int(num)]
		page.text = page.text.replace(f'Verse {num}', f'==[[{perek} {letter}|פסוק {letter}]]==', 1)
	page.save(summary='כותרות')
print('mission comleted!')
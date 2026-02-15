import pywikibot
from pywikibot.pagegenerators import PrefixingPageGenerator

ALEPHBET = ('', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט',
'ס', 'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט',
'ע', 'עא', 'עב', '')

site = pywikibot.Site()
#for page in PrefixingPageGenerator('גבורות ה\'/פרק'):
#	letter = page.title().split()[-1]
#	prev_letter = ALEPHBET[ALEPHBET.index(letter)-1]
#	next_letter = ALEPHBET[ALEPHBET.index(letter)+1]
#	navigation = '{{סרגל ניווט|גבורות ה\'||פרק '+prev_letter+'|פרק '+letter+'|פרק '+next_letter+'|קטגוריה=1}}\n'
#	input(navigation)
#	page.text = navigation + page.text
#	page.save('הוספת ניווט')

base = 'דרך חיים (מהר"ל)/'
for page in PrefixingPageGenerator(base+'פרק'):
	current = page.title().split('/')[-1]
	perek = current.split()[1]
	mishna = current.split()[-1]
	print(perek, mishna)
	prev_letter = ALEPHBET[ALEPHBET.index(mishna)-1]
	prev_perek = ALEPHBET[ALEPHBET.index(perek)-1]
	prev_page = 'פרק '+perek+' משנה '+prev_letter if prev_letter else 'פרק '+prev_perek+' משנה '
	next_letter = ALEPHBET[ALEPHBET.index(mishna)+1]
	next_perek = ALEPHBET[ALEPHBET.index(perek)+1]
	next = 'פרק '+perek+' משנה '+next_letter
	next_page = next if pywikibot.Page(site, base+next).exists() else 'פרק '+next_perek+' משנה א'
	navigation = '{{סרגל ניווט|דרך חיים (מהר"ל)||'+prev_page+'|'+current+'|'+next_page+'|קטגוריה=1}}\n'
	input(navigation)
	page.text = navigation + page.text
	page.save('הוספת ניווט')
print('completed!')
	
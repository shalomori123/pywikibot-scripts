import pywikibot
from pywikibot.pagegenerators import CategorizedPageGenerator

ALEPHBET = ('', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט',
'ס', 'סא', 'סב', 'סג', 'סד', 'סה', 'סו', 'סז', 'סח', 'סט',
'ע', 'עא', 'עב', 'עג', 'עד', 'עה', 'עו', 'עז', 'עח', 'עט',
'פ', 'פא', 'פב', 'פג', 'פד', 'פה', 'פו', 'פז', 'פח', 'פט',
'צ', 'צא', 'צב', 'צג', 'צד', 'צה', 'צו', 'צז', 'צח', 'צט',
'ק', 'קא', 'קב', 'קג', 'קד', 'קה', 'קו', 'קז', 'קח', 'קט',
'קי', 'קיא', 'קיב', 'קיג', 'קיד', 'קטו', 'קטז', 'קיז', 'קיח', 'קיט',
'קכ', 'קכא', 'קכב', 'קכג', 'קכד', 'קכה', 'קכו', 'קכז', 'קכח', 'קכט',
'קל', 'קלא', 'קלב', 'קלג', 'קלד', 'קלה', 'קלו', 'קלז', 'קלח', 'קלט',
'קמ', 'קמא', 'קמב', 'קמג', 'קמד', 'קמה', 'קמו', 'קמז', 'קמח', 'קמט',
'קנ', 'קנא')

site = pywikibot.Site()
cat = pywikibot.Category(site, 'קטגוריה:פרקי התנ"ך')
for perek in CategorizedPageGenerator(cat):
	name = perek.title()
	*books, letter = name.split(' ')
	book = ' '.join(books)
	prev = ALEPHBET[ALEPHBET.index(letter)-1]
	nextl = ALEPHBET[ALEPHBET.index(letter)+1]
	
	mgname = 'מ"ג ' + name
	mg = pywikibot.Page(site, mgname)
	mg.text = '{{מקראות גדולות על פרק|' + book + '|' + prev + '|' + letter + '|' + nextl + '}}'
	mg.save()
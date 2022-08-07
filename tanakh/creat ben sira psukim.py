import pywikibot

ALEPHBET = ('א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד', 'לה', 'לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט')

from1 = [30,18]
from19 = [30,31,27,27,27,33,26,29,30,26,28,25]
from31 =  [31, 24, 33, 31, 26, 31, 31, 34, 35, 30]
site = pywikibot.Site()
from41 = [22, 25, 33, 23, 26, 20, 25, 25, 16, 29, 30]

for i,psukim in enumerate(from19):
	perek = ALEPHBET[i+18]
	for j in range(psukim):
		pasuk = ALEPHBET[j]
		page = pywikibot.Page(site, 'בן סירא '+perek+' '+pasuk)
		
		if page.exists():
			continue
		prev = ''
		if j==0:
			prev = '|פרק קודם=כן|הקודם=' + ALEPHBET[from1[i-19]-1]
		
		nextp = ''
		if j==psukim-1:
			nextp = '|פרק הבא=כן'
			
		page.text = '{{פסוק בבן סירא|' + perek +'|' + pasuk + prev + nextp + '}}'
		page.save(summary='יצירת דף עם התוכן: '+page.text)
	input('press enter')
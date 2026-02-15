import pywikibot

site = pywikibot.Site()
temp = pywikibot.Page(site, 'תבנית:פרק משנה')
gen = temp.getReferences(only_template_inclusion=True)

for page in gen:
	print(page.title())
	if len(page.title().split()) == 4:
		_, mas, echet, perek = page.title().split()
		masechet = mas + ' ' + echet
	else:
		_, masechet, perek = page.title().split()
	rambam = page.title() + ' רמבם'
	barte = 'ברטנורא על '+masechet+' '+perek
	rambam_p = 'רמב"ם על '+masechet+' '+perek
	toyt =  'תוספות יום טוב על '+masechet+' '+perek
	tiferet = 'תפארת ישראל על '+masechet+' '+perek
	
	mefarshim = [rambam, barte, rambam_p, toyt, tiferet]
	pages = [pywikibot.Page(site, m) for m in mefarshim]
	
	temp = '\n{{פירוש על פרק משנה|'+masechet+'|'+perek+'}}\n'
	summary = 'הוספת {{פירוש על פרק משנה}}'
	noin = '<noinclude>'
	noinend = '</noinclude>'
	
	if temp in pages[0].text:
		continue
	
	pages[0].text = pages[0].text.replace(page.title(as_link=True), page.title(as_link=True)+temp)
	
	pages[1].text = noin+temp+ '[[קטגוריה:ברטנורא על המשנה|'+masechet+' '+perek+']]'+noinend + '\n' + pages[1].text
	
	pages[2].text = pages[2].text + '\n' + noin+temp+ '[[קטגוריה:פירוש המשנה לרמב"ם|'+masechet+' '+perek+']]'+noinend
	
	pages[3].text = pages[3].text + '\n' + noin+temp+noinend
	
	pages[4].text = noin+temp+ '[[קטגוריה:תפארת ישראל על המשנה|'+masechet+' '+perek+']]'+noinend + '\n\n' + pages[4].text
	
	for p in pages:
		p.save(summary)

print('completed!')

import pywikibot
import re

site = pywikibot.Site()
#page = pywikibot.Page(site, 'ספר יראים/כל')
#text = page.text[:16000]
#print(text)
#regex = '<קטע סוף=\{\{פסוק קודם\|\{\{המרת מספרים לאותיות\|(\d+)\}\}\}\}>\s*<קטע התחלה=(\{\{המרת מספרים לאותיות\||)\\1\}?\}?>'
#print(re.findall(regex, text))


#from pywikibot.textlib import extract_sections
#page = pywikibot.Page(site, 'משתמש:Shalomori123/טיוטה')
#print(extract_sections(page.text, site))


#temp = pywikibot.Page(site, 'תבנית:מ"מ')
#i = 0
#for page in temp.getReferences(only_template_inclusion=True):
#	if '|הק=' in page.text:
#		print(page.title())
#	if i > 1000:
#		print('1000')
#		i=0
#	i += 1


#temp = pywikibot.Page(site, 'תבנית:דף של מדרש')
#gen = temp.getReferences(only_template_inclusion=True)
#dicto = {}
#for page in gen:
#	reg = re.search('\|פיסקאות=(\d{1,3})[\}\|]', page.text)
#	if reg is not None:
#		dicto[page.title()] = reg.group(1)
#print(dict(sorted(dicto.items())))


ALEPHBET = ('ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט',
'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט',
'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט',
'ל', 'לא', 'לב', 'לג', 'לד')
for i in ALEPHBET:
	page = pywikibot.Page(site, 'תרגום ירושלמי (קטעים)/ספר דברים/'+i)
	page.text = re.sub('<קטע (התחלה|סוף)=', '\\g<0>'+i+' ', page.text)
	page.save()
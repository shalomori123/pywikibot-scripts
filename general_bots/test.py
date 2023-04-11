import pywikibot
#import re

site = pywikibot.Site()
#page = pywikibot.Page(site, 'ספר יראים/כל')
#text = page.text[:16000]
#print(text)
#regex = '<קטע סוף=\{\{פסוק קודם\|\{\{המרת מספרים לאותיות\|(\d+)\}\}\}\}>\s*<קטע התחלה=(\{\{המרת מספרים לאותיות\||)\\1\}?\}?>'
#print(re.findall(regex, text))


from pywikibot.textlib import extract_sections
page = pywikibot.Page(site, 'משתמש:Shalomori123/טיוטה')
print(extract_sections(page.text, site))


#temp = pywikibot.Page(site, 'תבנית:מ"מ')
#i = 0
#for page in temp.getReferences(only_template_inclusion=True):
#	if '|הק=' in page.text:
#		print(page.title())
#	if i > 1000:
#		print('1000')
#		i=0
#	i += 1
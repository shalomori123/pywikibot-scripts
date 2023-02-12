import pywikibot
#import re

site = pywikibot.Site()
#page = pywikibot.Page(site, 'ספר יראים/כל')
#text = page.text[:16000]
#print(text)
#regex = '<קטע סוף=\{\{פסוק קודם\|\{\{המרת מספרים לאותיות\|(\d+)\}\}\}\}>\s*<קטע התחלה=(\{\{המרת מספרים לאותיות\||)\\1\}?\}?>'
#print(re.findall(regex, text))

from pywikibot.textlib import extract_sections
page = pywikibot.Page(site, 'בעל הטורים על התורה/במדבר/ב')
print(extract_sections(page.text, site))
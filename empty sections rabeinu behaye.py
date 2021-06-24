import pywikibot
import re

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'משתמש:Shalomori123/קישורים לבוט')
for page in mainpage.linkedPages():
	if not page.exists():
		continue
	if re.search('<קטע התחלה=[ט-צ]?[א-ט]?/><קטע סוף', page.text):
		page.text = re.sub('\n.*\n<קטע התחלה=[ט-צ]?[א-ט]?/><קטע סוף.*', '', page.text)
	while '\n\n\n' in page.text:
		page.text = page.text.replace('\n\n\n', '\n\n')
	page.save(summary='מחיקת כותרות ריקות')
print('mission comleted!')
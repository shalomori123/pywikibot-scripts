import pywikibot
from pywikibot.textlib import extract_sections, add_text

#pagename = 'שו"ת רדב"ז/חלק ד'
#pagename = 'אור חדש/6'
basename = 'שו"ת רדב"ז/' # pagename + '/'
summary = 'בוט פיצול: פוצל מתוך דף [[' + pagename + ']]'

site = pywikibot.Site()
page = pywikibot.Page(site, pagename)
sections = extract_sections(page.text, site)
links = []

for sec in sections.sections:
	part = sec.title.strip().strip('=').strip()
	new_name = basename + part
	sec_page = pywikibot.Page(site, new_name)
	new_text = sec.title + sec.content
	#if not sec_page.exists():
	sec_page.text = add_text(sec_page.text, new_text, site=site)
	sec_page.save(summary)
	links.append('[[' + new_name + '|' + part + ']]')

print(links)
toc = '==תוכן הספר==\n* ' + '\n* '.join(links)
page.text = sections.header + toc + sections.footer
page.save('בוט פיצול: הדף פוצל לדפי משנה')
print('completed!')

import re
import pywikibot
from pywikibot import textlib

#pagename = 'משתמש:Shalomori123/טיוטה'
#pagename = 'שו"ת רדב"ז/חלק ד'
#pagename = 'אור חדש/6'
#pagename = 'הגהות רבי עקיבא איגר/יורה דעה'
#pagename= 'גור אריה על בראשית/9'
#pagename= 'גור אריה על שמות/8'
#pagename= 'גור אריה על ויקרא/6'
#pagename= 'גור אריה על במדבר/5'
#pagename= 'גור אריה על דברים/4'
#pagename = 'טיוטה:סמ"ק'
pagename = 'טיוטה:הגהות רבינו פרץ'

max_order = 2
notitle = True
basename = 'הגהות רבינו פרץ על סמ"ק/'
if not basename:
	basename = pagename + '/'
summary = 'בוט פיצול: פוצל מתוך דף [[' + pagename + ']]'

def header_regex(max_order=5):
	equals = '='
	equals += '=?' * (max_order-1)
	return re.compile(
            r'(?:(?<=\n)|\A)(?:<!--[\s\S]*?-->)*'
            + equals +
            r'[^=\n](?:[^\n]|<!--[\s\S]*?-->)*='
            r' *(?:<!--[\s\S]*?--> *)*(?=\n|\Z)')

site = pywikibot.Site()
page = pywikibot.Page(site, pagename)
textlib._create_default_regexes()
textlib._regex_cache['header'] = header_regex(max_order)
sections = textlib.extract_sections(page.text, site)
links = []
for sec in sections.sections:
	part = sec.title.strip().strip('=').strip()
	new_name = basename + part
	sec_page = pywikibot.Page(site, new_name)
	new_text = ('' if notitle else sec.title) + sec.content
	#if not sec_page.exists():
	sec_page.text = textlib.add_text(sec_page.text, new_text, site=site)
	sec_page.save(summary)
	links.append('[[' + new_name + '|' + part + ']]')

print(links)
toc = '==תוכן הספר==\n* ' + '\n* '.join(links)
page.text = sections.header + toc + sections.footer
page.save('בוט פיצול: הדף פוצל לדפי משנה')
print('completed!')

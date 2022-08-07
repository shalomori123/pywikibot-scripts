import pywikibot
import re

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'תוספות רי"ד')
pages = mainpage.linkedPages()
for page in pages:
    list_page = page.title().split('/')
    masechet = list_page[1]
    if masechet not in ['בבא בתרא', 'עבודה זרה', 'עירובין', 'ברכות', 'הוריות'] and page.exists():
        page.text = re.sub('=== ?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב]) ?===',
                           '===[[%s \\1 \\2|דף \\1 עמוד \\2]]===' % masechet,
                           page.text)
        page.save(summary='כותרות שמקשרות לדף')

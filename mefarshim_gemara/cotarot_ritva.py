import pywikibot
import re

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'חידושי הריטב"א על הש"ס')
pages = mainpage.linkedPages()
for page in pages:
    list_page = page.title().split('/')
    masechet = list_page[1]
    if masechet in ['ברכות','עירובין','יומא','סוכה','ראש השנה','תענית','כתובות','בבא בתרא', 'מכות','עבודה זרה','נדה']:
        page.text = re.sub('=== ?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב]) ?===',
                           '===[[%s \\1 \\2|דף \\1 עמוד \\2]]===' % masechet,
                           page.text)
        page.save(summary='כותרות שמקשרות לדף')
    

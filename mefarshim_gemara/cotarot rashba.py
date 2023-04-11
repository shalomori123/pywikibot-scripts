import pywikibot
import re

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'חידושי הרשב"א על הש"ס')
pages = mainpage.linkedPages()
for page in pages:
    page.get()
    if 'קידושין' not in page.title() and page.exists():
        list_page = page.title().split('/')
        masechet = list_page[1]
        page.text = re.sub('=== ?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב]) ?===',
                           '===[[%s \\1 \\2|דף \\1 עמוד \\2]]===' % masechet,
                           page.text)
    else:
        page.text = re.sub('== ?דף (ק?[ט-צ]?[א-י]?) עמוד ([אב]) ?==',
                           '===[[קידושין \\1 \\2|דף \\1 עמוד \\2]]===',
                           page.text)
    page.save(summary='כותרות שמקשרות לדף')
    

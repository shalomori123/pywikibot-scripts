import pywikibot
import re

site = pywikibot.Site()
mainpage = pywikibot.Page(site, 'פני יהושע')
pages = mainpage.linkedPages()
for page in pages:
    if not page.exists() or not page.title().startswith('פני יהושע/'):
        continue
    list_page = page.title().split('/')
    masechet = list_page[1]
    page.text = re.sub('=== ?דף (ק?[ט-צ]?[א-י]?) עמ(?:וד|\') ([אב]) ?===',
                           '===[[%s \\1 \\2|דף \\1 עמוד \\2]]===' % masechet,
                           page.text)
    page.save(summary='כותרות שמקשרות לדף')

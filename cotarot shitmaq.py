import pywikibot
import re

site = pywikibot.Site()
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא קמא')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא מציעא')
# mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/בבא בתרא')
mainpage = pywikibot.Page(site, 'שיטה מקובצת על הש"ס/כתובות')
pages = mainpage.linkedPages()
for page in pages:
    list_page = page.title().split('/')
    masechet = list_page[1]
    # if masechet in ['בבא בתרא', 'ביצה', 'נדרים', 'נזיר', 'סוטה'] and page.exists():
    page.text = re.sub('=?== ?דף (ק?[ט-צ]?[א-י]?) עמ(וד|\') ([אב]) ?===?', '===[[%s \\1 \\3|דף \\1 עמוד \\3]]===' % masechet, page.text)
    page.text = re.sub('=?== ?דף (ק?[ט-צ]?)"?([א-י]?)\'? ע"([אב]) ?===?', '===[[%s \\1\\2 \\3|דף \\1\\2 עמוד \\3]]===' % masechet, page.text)
    page.save(summary='כותרות שמקשרות לדף')

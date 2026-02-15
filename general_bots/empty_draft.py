import pywikibot

site = pywikibot.Site('he', 'wikisource')
page = pywikibot.Page(site, 'משתמש:shalomori123/קישורים לבוט')
page.text = "'''זהו דף טיוטה שמכיל קישורים של דפים שבוט מסוים צריך לרוץ עליהם:'''"
page.save('ריקון')
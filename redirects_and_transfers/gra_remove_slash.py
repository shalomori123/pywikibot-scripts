import pywikibot
alephbet = ('לו', 'לז', 'לח', 'לט',
'מ', 'מא', 'מב', 'מג', 'מד', 'מה', 'מו', 'מז', 'מח', 'מט',
'נ', 'נא', 'נב', 'נג', 'נד', 'נה', 'נו', 'נז', 'נח', 'נט')
site = pywikibot.Site()
for letter in alephbet:
	page = pywikibot.Page(site, 'ביאור הגר"א על אורח חיים/'+letter)
	page.move('ביאור הגר"א על אורח חיים '+letter, reason='כשאר המהדורה')
import pywikibot

site = pywikibot.Site()
redirs = site.allpages(start='תהלים רנא', namespace=0,
                         filterredir=True, content=True)
counter = 0
for redir in redirs:
	try:
		targ = redir.getRedirectTarget()
	except:
		continue
	if targ.namespace() == "ביאור:" and '[[קטגוריה:הפניות מהמרחב הראשי למרחב ביאור]]' not in redir.text:
		redir.text += '\n\n[[קטגוריה:הפניות מהמרחב הראשי למרחב ביאור]]'
		redir.save('קטגוריה להפניות למרחב ביאור')
		counter += 1
		print(counter)
print('completed!', counter)
import pywikibot
import re
from pywikibot.bot import (SingleSiteBot, ExistingPageBot)

ALEPHBET = (0, 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'יא', 'יב', 'יג', 'יד', 'טו', 'טז', 'יז', 'יח', 'יט', 'כ', 'כא', 'כב', 'כג', 'כד', 'כה', 'כו', 'כז', 'כח', 'כט', 'ל')

class MefarshimToDafBot(SingleSiteBot, ExistingPageBot):
	"""A bot to add 'mefarshim to daf of gmara' temp to pages"""
	
	def __init__(self, site=pywikibot.Site()):
		super().__init__(site=site)
		mainpage = pywikibot.Page(site, 'משתמש:Ori229/כל דפי הבבלי')
		self.generator = mainpage.linkedPages()
		self.perek_counter = 1
		self.until = ''
	
	def treat(self, page):
		title_words = page.title().split(' ')
		
		if len(title_words) == 3:
			masechet = title_words[0]
		elif len(title_words) == 4:
			masechet = title_words[0] +' '+ title_words[1]
		else:
			print('Wrong page!')
			masechet = ''
		
		daf = title_words[-2]
		amud = title_words[-1]
		
		if page.title().startswith('בבלי') or masechet[0] in ['ב']:
			return
		
		if daf+' '+amud == 'ב א':
			self.perek_counter = 1
			print(masechet)
			self.until = input('עד איזה דף פרק א? ')
		perek = ALEPHBET[self.perek_counter]
		two_pereks = ''
		if daf+' '+amud == self.until:
			two_pereks = input('האם בדף זה יש שני פרקים? (y/כן) ')
			self.perek_counter += 1
			self.until = input('עד איזה דף פרק ' + ALEPHBET[self.perek_counter] + '? ')
		
		if '{{מפרשים לדף גמרא' in page.text:
			self._skip_counter += 1
			print(page.title() + 'skipped')
			return
		
		oldtext = page.text
		newtext = page.text + '\n{{מפרשים לדף גמרא|' + masechet + '|' + perek + '|' + daf + '|' + amud + '}}'
		if two_pereks == 'y' or two_pereks == 'כן':
			newtext = re.sub('(\{\{מפרשים לדף גמרא\|.*?)\}\}', '\\1|שני פרקים=כן}}', newtext)
		
		summary = 'הוספת {{מפרשים לדף גמרא}}'
		self.userPut(page, oldtext, newtext, summary = summary)

bot = MefarshimToDafBot()
bot.run()
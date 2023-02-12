import re
import pywikibot
from pywikibot.bot import SingleSiteBot, ExistingPageBot
from pywikibot import pagegenerators


docuReplacements = {'&params;': pagegenerators.parameterHelp}  # noqa: N816

DEFAULT_ARGS = {
    'summary': '[[משתמש:ShalomOrobot/בוט המקורות|בוט המקורות]]: ',
    'always': False,
    'minor': True,
}


def edit_spaces(text):
	while '\n ' in text:
		text = text.replace('\n ', '\n')
	while ' \n' in text:
		text = text.replace(' \n', '\n')
	
	while ' )' in text:
		text = text.replace(' )', ')')
	while '( ' in text:
		text = text.replace('( ', '(')
	while re.search('[^\s\(\[\|\{\>\<]\(', text):
		text = re.sub('([^\s\(\[\|\{\>\<])\(', r'\1 (',text)
	while re.search('\)[^\s\)\]\}\|\>\<]', text):
		text = re.sub('\)([^\s\)\]\}\|\>\<])', r') \1', text)
	
	while '׃' in text:
		text = text.replace('׃', ':')
	while ' :' in text:
		text = text.replace(' :', ':')
	while ' .' in text:
		text = text.replace(' .', '.')
	while ' ,' in text:
		text = text.replace(' ,', ',')
	while ' ;' in text:
		text = text.replace(' ;', ';')
	while '  ' in text:
		text = text.replace('  ', ' ')
	
	return text


class Sources:
	def __init__(self, text):
		self.text = text
		self.input = text
		#self.test_bible()
		#self.test_bavli()
		self.check_bavli = None
		self.check_bible = None
		self.check_midrash = None
		self.check = lambda: self.text != self.input
		
	def bavli(self, text=None):
		if text is None:
			text = self.text
		oldtext = text
		masechtot = ["ברכות", "שבת", "עירובין", "פסחים", "ראש השנה", "יומא", "סוכה",
"ביצה", "תענית", "מגילה", "מועד קטן", "חגיגה", "יבמות", "כתובות", "נדרים",
"נזיר", "גיטין", "סוטה", "קידושין", "בבא קמא", "בבא מציעא", "בבא בתרא",
"סנהדרין", "מכות", "שבועות", "עבודה זרה", "הוריות", "זבחים", "מנחות",
"חולין", "בכורות", "ערכין", "תמורה", "כריתות", "מעילה", "תמיד", "נדה",
"ערובין", "קדושין", "נידה", 'ע"ז', 'עכו"ם', "סנהד'", "פסח'", 'ב"ק', 'ב"מ', 'ב"ב',
'מו"ק', 'ר"ה', "הורי'", "גטין", 'מ"ק']
		masech_reg = '(' + '|'.join(masechtot) + ')'
		
		daf_regex = '\((?:בבלי,? )?'+masech_reg+',?(?: ד[\'׳]| דף|) ((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])),?'
		text = re.sub(daf_regex+' (?:עמוד |עמ[׳\'] |ע[״"]|)([אב])[\'׳]?\)(?!\])', '{{הפניה-גמ|\\1|\\3\\4\\5\\6|\\7|מסכת=כן}}', text)
		text = re.sub(daf_regex+'\.\)(?!\])', '{{הפניה-גמ|\\1|\\3\\4\\5\\6|א|מסכת=כן}}', text)
		text = re.sub(daf_regex+'\:\)(?!\])', '{{הפניה-גמ|\\1|\\3\\4\\5\\6|ב|מסכת=כן}}', text)
		
		daf_regex = masech_reg+' \((?:ד[\'׳] |דף |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])),?'
		text = re.sub(daf_regex+' (?:עמוד |עמ[׳\'] |ע[״"]|)([אב])[\'׳]?\)(?!\])', '\\1 {{הפניה-גמ|\\1|\\3\\4\\5\\6|\\7}}', text)
		text = re.sub(daf_regex+'\.\)(?!\])', '\\1 {{הפניה-גמ|\\1|\\3\\4\\5\\6|א}}', text)
		text = re.sub(daf_regex+'\:\)(?!\])', '\\1 {{הפניה-גמ|\\1|\\3\\4\\5\\6|ב}}', text)
		
		self.text = text
		if self.text == oldtext:
			return False
		return True
	
	def bible(self, text=None):
		if text is None:
			text = self.text
		oldtext = text
		books = ["בראשית", "שמות", "ויקרא", "במדבר", "דברים",
"יהושע", "שופטים", "שמואל א", "שמואל ב", "מלכים א", "מלכים ב",
"ישעיהו", "ירמיהו", "יחזקאל", "הושע", "יואל", "עמוס", "עובדיה", "יונה",
"מיכה", "נחום", "חבקוק", "צפניה", "חגי", "זכריה", "מלאכי",
"תהלים", "משלי", "איוב", "שיר השירים", "רות", "איכה", "קהלת", "אסתר",
"דניאל", "עזרא", "נחמיה", "דברי הימים א", "דברי הימים ב",
"ישעיה", "ירמיה", "תהילים", "קוהלת", 'ש"א', 'ש"ב', 'מ"א', 'מ"ב', 'דה"א', 'דה"ב', 'שה"ש',
"שמואל א'", "שמואל ב'", "מלכים א'", "מלכים ב'", "דברי הימים א'", "דברי הימים ב'",
"ישעי'", "ירמי'", "נחמי'", "ד\"ה א'", "ד\"ה ב'", "ד\"ה א", "ד\"ה ב", "צפני'", "זכרי'", "תלים"]

		#for Tehilim that has perek 80+ (without פ"x, with ק)
		books_reg = '(' + '|'.join(['תהלים', 'תהילים', 'תלים']) + ')'
		#book inside ()
		perek_regex = '\('+books_reg+',? (?:פרק |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])),?'
		text = re.sub(perek_regex+'\)(?!\])', '{{מ"מ|\\1|\\3\\4\\5\\6}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוק |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט]))\)(?!\])', '{{מ"מ|\\1|\\3\\4\\5\\6|\\8\\9\\10\\11|ק={{שם הדף}}}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוקים |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])) ?- ?((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט]))\)(?!\])', '{{הפניה לפסוקים|\\1|\\3\\4\\5\\6|\\8\\9\\10\\11|\\13\\14\\15\\16}}', text)
		
		#book outside ()
		perek_regex = books_reg+' \((?:פרק |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])),?'
		text = re.sub(perek_regex+'\)(?!\])', '\\1 {{מ"מ|\\1|\\3\\4\\5\\6}}', text)
		text = re.sub(perek_regex+'[: ](?:פס[\'׳] |פסוק |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט]))\)(?!\])', '\\1 {{מ"מ|\\1|\\3\\4\\5\\6|\\8\\9\\10\\11|ק={{שם הדף}}}}', text)
		text = re.sub(perek_regex+'[: ](?:פס[\'׳] |פסוקים |)((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט])) ?- ?((ק?)[״"]?([א-צ])[׳\']?|(ק?[ט-צ])[״"]?([א-ט]))\)(?!\])', '\\1 {{הפניה לפסוקים|\\1|\\3\\4\\5\\6|\\8\\9\\10\\11|\\13\\14\\15\\16}}', text)
		
		
		#other books
		books_reg = '(' + '|'.join(books) + ')'
		#book inside ()
		perek_regex = '\('+books_reg+',? (?:פ[\'׳] |פרק |פ[״"]?|)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט])),?'
		text = re.sub(perek_regex+'\)(?!\])', '{{מ"מ|\\1|\\3\\4\\5}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוק |)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט]))\)(?!\])', '{{מ"מ|\\1|\\3\\4\\5|\\7\\8\\9|ק={{שם הדף}}}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוקים |)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט])) ?- ?(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט]))\)(?!\])', '{{הפניה לפסוקים|\\1|\\3\\4\\5|\\7\\8\\9|\\11\\12\\13}}', text)
		
		#book outside ()
		perek_regex = books_reg+' \((?:פ[\'׳] |פרק |פ[״"]?|)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט])),?'
		text = re.sub(perek_regex+'\)(?!\])', '\\1 {{מ"מ|\\1|\\3\\4\\5}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוק |)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט]))\)(?!\])', '\\1 {{מ"מ|\\1|\\3\\4\\5|\\7\\8\\9|ק={{שם הדף}}}}', text)
		text = re.sub(perek_regex+'[ :](?:פס[\'׳] |פסוקים |)(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט])) ?- ?(([א-צ])[׳\']?|([ט-צ])[״"]?([א-ט]))\)(?!\])', '\\1 {{הפניה לפסוקים|\\1|\\3\\4\\5|\\7\\8\\9|\\11\\12\\13}}', text)
		
		self.text = text
		if self.text == oldtext:
			return False
		return True
	
	def midrash(self):
		text = self.text
		oldtext = text
		#TODO
		'''
מדרש:
ויק"ר
ילקו"ש
ב"ר
מכילתא
במ"ר
תנחומא

פ"א
פ' א'
'''
		text = re.sub('', '', text)
		self.text = text
		if self.text == oldtext:
			return False
		return True
	
	def add(self):
		self.check_bavli = self.bavli()
		self.check_bible = self.bible()
		#self.check_midrash = self.midrash()
		return self
	
	def test_bible(self):
		oldtext = self.text
		options = '''אפשרויות פסוקים:
(קהלת ג ד)
(משלי ד', א')
(משלי מ"ד, א׳)
(משלי מ״ד ע"ב)
(דברים, פרק מד ע"א)
(משלי פ' מד, ע"א)
(ישעיהו פמ"ד פסוק א)
(תהלים פ' ג')
(תהלים פ"ג)
(משלי כ"ד פס' א)
(משלי ל"א, כ"ג-כ״ד)
(משלי לא כג - כד)
(משלי ד)
(משלי, פרק מד)
(בראשית כ״ג:מ״ד)
כנ"ל כשהסוגריים רק מהפרק:
משלי (ד', א')
משלי (מ"ד, א׳)
תהלים (קמ״ד ע"ב)
יהושע (פרק מד ע"א)
משלי (פ' מד, ע"א)
תהלים (פרק קמ"ד פסוק א)
משלי (כ"ד פס' א)
משלי (ד)
משלי (פרק מד)'''
		self.bible(options)
		print('original text:\n\n', options, '\n\n\noutput:\n\n', self.text)
		self.text = oldtext
	
	def test_bavli(self):
		oldtext = self.text
		options = '''אפשרויות בבלי:
(ברכות ד', א')
(בבלי ברכות מ"ד, א׳)
(ברכות קמ״ד ע"ב)
(קדושין, דף קמד ע"א)
(ברכות ד' קמד, ע"א)
(ב"ק דף קמ"ד עמוד א)
(ברכות ק"ד עמוד א)
(ברכות ד.)
(ברכות, דף קמד:)
כנ"ל כשהסוגריים רק מהדף:
ברכות (ד', א')
ברכות (מ"ד, א׳)
ברכות (קמ״ד ע"ב)
קדושין (דף קמד ע"א)
ברכות (ד' קמד, ע"א)
ב"ק (דף קמ"ד עמוד א)
ברכות (ק"ד עמוד א)
ברכות (ד.)
ברכות (דף קמד:)'''
		self.bavli(options)
		print('original text:\n\n', options, '\n\n\noutput:\n\n', self.text)
		self.text = oldtext
	

class SourcesBot(SingleSiteBot, ExistingPageBot):
	"""A bot for adding templates of sources to pages.
	it's replacing () with template in the site.
		"""
	def __init__(self, **kwargs):
		super().__init__(generator=kwargs['gen'])
		self.opt.update(kwargs)

	def treat(self, page):
		if page.isRedirectPage():
			page = page.getRedirectTarget()
		
		oldsummary = self.opt.summary
		oldtext = page.text
		
		page.text = edit_spaces(page.text)
		if page.text != oldtext:
			self.opt.summary += 'עריכת רווחים, '
		
		src = Sources(page.text)
		src.add()
		page.text = src.text
		
		if src.check():
			if src.check_bavli:
				self.opt.summary += 'בבלי, '
			if src.check_bible:
				self.opt.summary += 'תנ"ך'
			
			self.userPut(page, oldtext, page.text, summary = self.opt.summary, minor = self.opt.minor)
		self.opt.summary = oldsummary


def main(*args: str) -> None:
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    :param args: command line arguments
    """
    local_args = pywikibot.handle_args(args)
    gen_factory = pagegenerators.GeneratorFactory()
    local_args = gen_factory.handle_args(local_args)
    gen = gen_factory.getCombinedGenerator(preload=True)
    if not gen:
    	pywikibot.bot.suggest_help(missing_generator=True)
    	return
    
    options = DEFAULT_ARGS
    for arg in local_args:
        arg, sep, value = arg.partition(':')
        option = arg[1:]
        if option in ('summary'):
            options[option] = value
        elif option in ('minor', 'always'):
            options[option] = True
        elif option == 'major':
        	options['minor'] = False
        else:
        	raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = SourcesBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()

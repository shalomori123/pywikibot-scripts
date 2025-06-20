import mwparserfromhell as mwparser
import pywikibot
from pywikibot.bot import SingleSiteBot, ExistingPageBot
from pywikibot import pagegenerators, textlib


def adding_temp_rev(page, temp_name):
	prev_rev = page.latest_revision
	for rev in page.revisions(content=True):
		text = rev.text
		temps = textlib.extract_templates_and_params(text)
		has_temp = temp_name in [t[0] for t in temps]
		if not has_temp:
			return prev_rev
		prev_rev = rev
	return prev_rev


class AddDateBot(SingleSiteBot, ExistingPageBot):
	def __init__(self, **kwargs):
		super().__init__(generator=kwargs['gen'])
		self.opt.update(kwargs)
		
	def treat_page(self):
		rev = adding_temp_rev(self.current_page, self.opt.temp_name)
		date = rev.timestamp.strftime("%d.%m.%Y")
		
		if self.opt.warning:
			user = rev.user
			talk_text = """
== שינוי טכני בתבנית "בעבודה" ==

שלום {{א|%s}},

בקרוב, בהמשך ל[[וק:תבנית/אולם דיונים#תבנית בעבודה: הוספה אוטומטית של תאריך הצבה|דיון באולם הדיונים לתבניות]], תבנית {{תב|בעבודה}} תמלא אוטומטית את הפרמטר {{פר|תאריך}}, כדי להקל על איתור תבניות "בעבודה" מתיישנות.

לצורך השינוי הזה, יש לשנות את שמותיהן של התבניות שכבר מוצבות בערכים מ"בעבודה" ל"בעבודה עם זמן", וניתן להוסיף להן את התאריך ידנית, או באמצעות בוט.

אם ברצונך לבצע את העדכון בעצמך, כדי למנוע התנגשות עריכה עם העריכה של הבוט, אז כל מה שצריך זה להחליף את:
{{קוד|מימין לשמאל=כן|{{((}}בעבודה{{))}}}}
לקוד המקור הבא:
{{קוד|מימין לשמאל=כן|1={{((}}בעבודה עם זמן{{!}}תאריך=%s{{))}}}}
(אם יש פרמטרים נוספים בתבנית, ניתן להשאיר אותם.)
לחלופין, אפשר להשאיר לבוט לבצע את העריכה הזו. '''הבוט ירוץ ב[תאריך ושעה שבה נבחר להריץ אותו] ויבצע עריכה''', ולכן רצוי לשמור את הערך לפני כן במידה ועורכים אותו באותו זמן, כדי למנוע התנגשות. אם השינוי יבוצע ידנית קודם לכן, הבוט ידלג על הערך הזה.

תודה רבה! ~~~~
""" % (user, date)
			talk_page = self.current_page.toggleTalkPage()
			talk_page.text += talk_text
			talk_page.save()
			return
		
		text = self.current_page.text
		code = mwparserfromhell.parse(text)
		for template in code.filter_templates():
			if template.name.matches(self.opt.temp_name) and not template.has("תאריך"):
				template.add("תאריך", date)
				template.name = str(template.name) + "עם זמן"
		new_text = str(code)
		
		self.current_page.text = new_text
		self.current_page.save(summary=f"הוספת תאריך לתבנית {{{self.opt.temp_name}}}")

		
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
    
    options = {}
    for arg in local_args:
        arg, sep, value = arg.partition(':')
        option = arg[1:]
        if option in ('temp_name'):
            options[option] = value
        elif option in ('warning'):
            options[option] = True
        else:
        	raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = AddDateBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()

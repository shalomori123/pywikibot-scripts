import mwparserfromhell as mwparser
import pywikibot
from pywikibot.bot import SingleSiteBot, ExistingPageBot
from pywikibot import pagegenerators

def edit_mikra_temps(text):
    wikicode = mwparser.parse(text, skip_style_tags=True)
    templates = wikicode.filter_templates()
    navigate = ""
    for temp in templates:
        if temp.name.matches('H'):
            temp.name = 'מ:ירושלם'
        elif temp.name.matches('קמץ'):
            temp.name = 'מ:קמץ'
        elif temp.name.matches('נוסח'):
            edit_nosah(temp)
        elif temp.name.matches('ניווט טעמים'):
            navigate = str(temp)
    return str(wikicode), navigate

def edit_nosah(temp):
    params = temp.params
    lst_params = [str(param) for param in params if not param.name.matches('1')]
    param2 = '{{ש}}'.join(lst_params)
    param1 = str(temp.get(1))
    params.clear()
    temp.add('1', param1, showkey=False)
    temp.add('2', param2, showkey=True)


# debug
#page="""
#<noinclude>{{ניווט טעמים|זכריה|ב}}
#{{טעמי המקרא באינטרנט}}
#{{מ:שוליים|5}}
#{{מ:טעמי המקרא}}
#</noinclude><קטע התחלה=פרק ב/>{{נוסח|{{פפ}}|ל=פרשה סתומה}}
#<קטע התחלה=סימן/>{{מ:פסוק|זכריה|ב|א}}<קטע סוף=סימן/><קטע התחלה=א/>וָאֶשָּׂ֥א אֶת־עֵינַ֖י וָאֵ֑רֶא וְהִנֵּ֖ה אַרְבַּ֥ע קְרָנֽוֹת׃<קטע סוף=א/>
#<קטע התחלה=סימן/>{{מ:פסוק|זכריה|ב|ב}}<קטע סוף=סימן/><קטע התחלה=ב/>וָאֹמַ֗ר אֶל־הַמַּלְאָ֛ךְ הַדֹּבֵ֥ר בִּ֖י מָה־אֵ֑לֶּה וַיֹּ֣אמֶר אֵלַ֔י אֵ֤לֶּה הַקְּרָנוֹת֙ אֲשֶׁ֣ר זֵר֣וּ אֶת־יְהוּדָ֔ה אֶת־יִשְׂרָאֵ֖ל {{נוסח|וִירוּשָׁל{{H|ָ|ֽ}}ם|=ק,ש1 ובדפוסים|ל!=וִירוּשָׁלָֽם (חסרה נקודת החיריק בלמ"ד)|הערות ברויאר ודותן והמקליד}}׃<קטע סוף=ב/>
#"""
#with open('txt.txt', 'a') as f:
#    f.write(edit_mikra_temps(page))
#    #f.write(str(mwparser.parse(page).get_tree()).encode('utf-8').decode('unicode_escape'))


class EditBot(SingleSiteBot, ExistingPageBot):
    def __init__(self, **kwargs):
        self.use_redirects = False
        
        super().__init__(generator=kwargs['gen'])
        self.opt.update(kwargs)
        
    def treat_page(self):
        text = self.current_page.text
        new_text, navigate = edit_mikra_temps(text)
        self.put_current(new_text, summary=self.opt.summary)
        
        newtitle = self.current_page.title().replace('/טעמים', '/הערות נוסח')
        newpage = pywikibot.Page(self.current_page.site, newtitle)
        newpage.text = navigate.replace('ניווט טעמים', 'דף פרק עם הערות נוסח')
        newpage.save()


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
        if option in ('summary'):
            options[option] = value
        elif option in ('always'):
            options[option] = True
        else:
            raise ValueError(f'"{arg}" is invalid arg.')
    
    bot = EditBot(gen=gen, **options)
    bot.run()

if __name__ == '__main__':
    main()

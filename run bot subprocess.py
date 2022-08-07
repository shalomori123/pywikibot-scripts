"""This is the new version of "wiki bot text to cmd.txt" which was text file to copy and paste.
This file uses subprocesses to run the bot directly from python."""

from subprocess import run
from os import chdir

paws = False
pwb_dir = '/storage/emulated/0/python/pywikibot'
if paws:
	pwb_dir = '/srv/paws/pwb'

chdir(pwb_dir)

#useful params
call = ['python', 'pwb.py']
user = '-user:ShalomOrobot'
main_user = '-user:shalomori123'
site = '-site:wikisource:he'
pt = '-pt:0'
all_pages = '-start:!'


#init scripts
#run(call + ['login'])
#run(call + ['generate_user_files'])

#frequent scripts
#run(call + ['keta tags bot'])
#run(call + ['empty draft'])
#run(call + ['redirect', 'double'])
#run(call + ['test'])

#one-time scripts
#run(call + ['replace', '[[קטע:', '[[', '-prefixindex:מצודות על ירמיה',
#pt, '-summary:תיקון הפניה שבורה'])
#run(call + ['replace', 'אבן עזרה}}', 'אבן עזרא}}', '-prefixindex:ביאור:מ"ג'])
#run(call + ['cotarot pnei yehoshua'])
#run(call + ['keta 3.0', '-page:משתמש:Shalomori123/טיוטה', 
#'-titles', '-remove_empty']) #test
#run(call + ['keta 2.0', '-page:משתמש:Shalomori123/טיוטה', '-regex:']) #test
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=איסור והיתר לרבנו ירוחם|\
#{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\n{{#קטע:איסור והיתר לרבנו ירוחם/כל התוכן\
#|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', '-links:איסור והיתר לרבנו ירוחם', '-createonly'])
#run(call + ['keta 2.0', '-page:איסור והיתר לרבנו ירוחם/כל התוכן',
#'-regex:==סימן ([ט-פ]?"?[א-ט]?)\'?=='])
#run(call + ['keta 2.0', '-page:משיבת נפש/הכל', '-regex:==(.*?)=='])
#run(call + ['add_text', '-text:{{ניווט ספר|שם הספר=משיבת נפש|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}\
#\n{{#קטע:משיבת נפש/הכל|{{ס:#titleparts:{{ס:שם הדף}}|1|2}}}}', 
#'-links:משיבת נפש', '-titleregex:משיבת נפש/', '-createonly'])
#run(call + ['replace', '{{ספר עץ חיים}}', '<noinclude>\n{{ספר עץ חיים}}\n</noinclude>', 
#'-prefixindex:עץ חיים/', pt, '-summary:תגי noinclude'])
#run(call + ['replace', '<קטע התחלה=/>', '', '<קטע סוף=/>', '', '-prefixindex:מלבי"ם'])
run(call + [])
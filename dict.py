import random
import enchant
from googletrans import Translator,constants
from PyDictionary import PyDictionary


# Instance / Objects
dictionary = PyDictionary()
d = enchant.Dict('en_US')
translator = Translator()
word_list = []
count = 0

while count < 5:
    count += 1
    randm_num = random.randint(97,122)
    word = [asci for asci in chr(randm_num)]
    word_list.append(word)

em_lst = []
for i in word_list:
    for j in i:
        em_lst.append(j)
w = (''.join(em_lst))
check_word = d.check(w)
if check_word == False:
    print(w,'----> Word Not found')
sgst_w = d.suggest(w)    
print('Suggested word ------> ', sgst_w)

# translate a English text to Bangla

translation = translator.translate(sgst_w, src='en',dest='bn')
for tr_word in translation:
    print(f"{tr_word.origin}) --> {tr_word.text} ({tr_word.dest})")

for tr_wor in translation:
    print(dictionary.translate(tr_wor,'bn','utf-8'))

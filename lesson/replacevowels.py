import re

def replace_vowels(txt, ch):
    vowels ='AEIOUaeiou'
    
    for element in vowels:
        txt = txt.replace(element,ch)
    return txt
	

def replace_vowels(txt, ch):
	return re.sub(r'[aeiouAEIOU]', ch, txt)

print(replace_vowels('Solomon','*'))
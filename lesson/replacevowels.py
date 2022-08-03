def replace_vowels(txt, ch):
    vowels ='AEIOUaeiou'
    
    for element in vowels:
        txt = txt.replace(element,ch)
    return txt
	
def shuffle_text(txt):
    data =[]
    for item in txt.split(' '):
        data.append(item)
    return '{} {}'.format(data[1],data[0])

def name_shuffle(str):
    	return ' '.join(reversed(str.split(' ')))
 
print(shuffle_text('Geremew Solomon'))
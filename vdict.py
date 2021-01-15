def vowels(text):
    vdict={'a':0,'e':0,'q':0,'w':0,'k':0,'u':0,'i':0}
    for ch in text:
        if ch in vdict:
            vdict[ch]+=1
    return vdict
input_text=iput('words:')
vowels_dict=vowels(input_text)
print(vowels_dict)

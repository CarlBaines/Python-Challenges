def syllablecounter(word):
    word = word.lower()
    count = 0
    vowels = ['a','e','i','o','u']
    if word [0] in vowels:
        count = count + 1
    for index in range(1,len(word)):
        if word[index] not in vowels and word[index - 1] not in vowels:
            count = count + 1
    if word.endswith('e'):
        count = count - 1
    if count == 0:
        count = count + 1
    return count
print(syllablecounter('Harry'))
        
        
    

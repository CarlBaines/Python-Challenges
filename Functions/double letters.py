def double_letters(word):
    for i in range(len(word)):
        if word[i] == word[i-1]:
            print("True")
            return True
    else:
        print("False")
        return False
double_letters("hello")

    

        
        
    

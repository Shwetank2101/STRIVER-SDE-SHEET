def reverse(word):
    i,j=0,len(word)-1
    while i<j:
        word[i],word[j]=word[j],word[i]
        i+=1
        j-=1
    word=' '.join(word)
    print(word)
        
word=input()
word=word.split()
reverse(word)

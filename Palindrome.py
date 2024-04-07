def palindrome(word):
    word = word.lower()
    word = word.replace(" ","")
    return word == word[::-1]
    

word = input("Enter the word you want to check.\n")
    
if palindrome(word):
    print(f"✅  {word} is a palindrome. ")
else:
    print(f"❌ {word} is not a palindrome")        
    

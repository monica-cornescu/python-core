# get a string from user and then count letters in it

userText = input("Tell me your thoughts: ")

if 'a' in userText or 'e' in userText or 'i' in userText or 'o' in userText or 'u' in userText:
    countVowels = userText.count('a') + userText.count('e') + userText.count('i') + userText.count('o') + userText.count('u')
    print('the number of vowels in your text is: ', countVowels)
    if countVowels < 10:
        print('I don\'t really know what to say; maybe you didn\'t say much')
    elif countVowels > 15:
        print('did you say aaaaaaaaaaaaaaaa?')
else:
    print("your stupid text has no vowels, so it can't be read; next time try another text, maybe it won't be so stupid")
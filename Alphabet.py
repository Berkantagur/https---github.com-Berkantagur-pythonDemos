#Learning whether the letter entered by the user is vowel or silent

vowel = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
silent = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']

letter = input("Enter a letter: ")

if letter in vowel:
    print(letter, "is a vowel letter.")

else:
    print(letter, "is a silent letter.")


'''

Exercise 5c

Consider an alternative version of Pig Latin—We do not check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we do not move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we will add “way” to the end of it, giv-
ing us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word? (Hint: sets can come in
handy here.)

'''

def pig_latin(word):
    first_letter = word[0]
    last = word[-1]
    vowels = 'aeiou'
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
            vowels = vowels.replace(letter, '')
    if vowel_count >= 2:
        word += 'way'
    elif vowel_count == 1:
        word = word[1:] + first_letter + 'ay'
    if first_letter.isupper():
        word = f'{word[0].upper()}{word[1:].lower()}'
    if last in '.!?,";)':
        word = word.replace(last, '') + last
    return word
 
print(pig_latin('Computer'))
print(pig_latin('Python'))
print(pig_latin('arrow'))
print(pig_latin('Hi!'))
print(pig_latin('toothpaste'))
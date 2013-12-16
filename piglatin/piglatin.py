def piglatin(word):
    vowels = ["a", "e", "i", "o", "u", ]
    consonants = []

    for i, character in enumerate(word):
        if i == 1:
            # 'y' isn't considered a vowel unless it's in the middle of a word.
            vowels.append('y')
        if character not in vowels:
            consonants.append(character)
        elif i == 0 and character in vowels:
            return word + "way"
        else:
            return word[i:] + ''.join(consonants) + 'ay'

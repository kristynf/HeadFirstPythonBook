def search4vowels():
    """Use to display any vowel found is any search term"""
    vowels = set('aeiou')
    word = input("Provide a term to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
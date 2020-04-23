def search4vowels():
    """Return a boolean depending if any vowel found in any search term"""
    vowels = set('aeiou')
    word = input('Provide a term to search for vowels: ')
    found = vowels.intersection(set(word))
    return bool(found)
def search4vowels(word):
    """Return a boolean depending if any vowel found in any search term"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

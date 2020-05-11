def search4vowels(word:str) -> set:
    """Return a boolean depending if any vowel found in any search term"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
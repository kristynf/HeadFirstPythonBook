def search4vowels(phrase:str) -> set:
    """Return a boolean depending if any vowel found in any search term"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
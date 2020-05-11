def search4vowels(phrase: str) -> set:
    """Return a boolean depending if any vowel found in any search term"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters found in 'phrase'."""
    return set(letters).intersection(set(phrase))

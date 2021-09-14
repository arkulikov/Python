def search4vowels(word:str) -> set:
    """Выводит гласные, найденный в указанном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

help(search4vowels)


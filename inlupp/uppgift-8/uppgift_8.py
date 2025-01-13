# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string:str) -> dict [str, int]:
    """
    Skriv beskrivning här.
    """
    my_dict={}
    uniq=set(string)
    for bukstav in uniq:
        my_dict[bukstav] = string.count(bukstav)
    return my_dict




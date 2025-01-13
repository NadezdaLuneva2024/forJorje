# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text:str) -> int:
    """
    Skriv beskrivning här.
    """
    ord = text.split()
    return len(ord)

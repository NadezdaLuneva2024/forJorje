# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers: int) -> list[int]:
    """
    Skriv beskrivning här.
    """
    jamna_tal = []
    for n in numbers:
        if n % 2 == 0:
            jamna_tal.append(n)
    return jamna_tal


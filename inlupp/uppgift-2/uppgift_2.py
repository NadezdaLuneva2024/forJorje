# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers: list[int]) -> int:
    """
    Skriv beskrivning här.
    """
    summan = 0
    for numb in numbers:
        summan = summan + numb
    return summan


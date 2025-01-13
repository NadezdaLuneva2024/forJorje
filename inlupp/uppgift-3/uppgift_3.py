# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list[int]) -> int:
    """
    Skriv beskrivning här.
    """
    maximum = max(numbers)
    return maximum

def max_in_list(numbers: list[int]) -> int:
    """
    Skriv beskrivning här.
    """
    maximum = numbers[0]
    for numb in numbers:
        if numb>maximum:
            maximum=numb
    return maximum

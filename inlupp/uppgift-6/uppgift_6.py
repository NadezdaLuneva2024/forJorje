# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n: int, limit: int) -> list[int]:
    """
    Skriv beskrivning här.
    """
    tabellen =[]
    for i in range(1, limit+1):
        tabellen.append(i*n)
    return tabellen

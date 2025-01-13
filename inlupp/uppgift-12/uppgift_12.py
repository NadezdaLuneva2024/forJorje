# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students: list[str,int]) -> dict [str, int]:
    """
    Skriv beskrivning här.
    """
    my_dict = dict(students)
    return my_dict

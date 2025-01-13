# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password:str) -> bool:
    """
    Skriv beskrivning här.
    """
    if any(char.isdigit() for char in password) and len(password)>=8:
        return True
    return False

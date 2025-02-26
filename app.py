def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    """Multiplie deux nombres."""
    return x * y


def divide(x, y):
    """Divise x par y en vérifiant que y n'est pas nul."""
    if y != 0:
        return x / y
    return None 


def greet(name):
    """Génère un message de salutation."""
    if name == "":
        return "Hello, World!"
    return f"Hello, {name}" 

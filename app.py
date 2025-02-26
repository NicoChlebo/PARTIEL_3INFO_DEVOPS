def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    beta = 0  # Variable inutilisée, tu peux la supprimer si elle n'est pas nécessaire
    if y != 0:
        return x / y


def greet(name):
    """Génère un message de salutation."""
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name

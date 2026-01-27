import random

def greeting(name, myfunction):
    saludo = myfunction(name)
    full_greeting = f"Greeting: {saludo}"
    return full_greeting

def message(name):
    edad = random.randint(18, 80)

    if edad > 45:
        return message(name)
    
    return f"Hola {name} tienes {edad} años"

names = ['Marcos', 'Juan', 'Maria', 'Pedro', 'Ana']

if __name__ == '__main__':
    for name in names:
        result = greeting(name, message)
        print(result)
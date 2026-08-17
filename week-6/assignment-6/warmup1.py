def greet(name, greeting="Hello"):
    prompt = f'{greeting}, {name}!'
    print(prompt)

greet("Alex")
greet("Alex", "Good Morning")
greet("Alex", greeting="Hello")
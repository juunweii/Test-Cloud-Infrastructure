def greet(name):
    """Greet a person with their name."""
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, there!"

# Example usage
user_name = input("Enter your name: ")
print(greet(user_name))

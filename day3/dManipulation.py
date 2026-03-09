numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Standard way to find squares of even numbers:
squares = [n**2 for n in numbers if n % 2 == 0]

print(f"Even squares: {squares}")

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

even_or_odd = lambda number: 'Even' if number % 2 == 0 else 'Odd'

even_or_odd=lambda n:'EOvdedn'[n%2::2]
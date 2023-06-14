def triple_numbers(numbers):
    tripled = list(map(lambda x: x * 3, numbers))
    return tripled

numbers = [1,2,3,4,5,6,7]

tripled_numbers =triple_numbers(numbers)
print(f"The tripled numbers are: {tripled_numbers}")

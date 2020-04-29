# Exception handling
# Mechanism for interrupting normal program flow and continuing in surrounding context
from math import factorial
DIGIT_DICT = {
'zero' : '0',
'one' : '1',
'two' : '2',
'three' : '3',
'four' : '4',
'five' : '5',
'six' : '6',
'seven' : '7',
'eight' : '8',
'nine' : '9',
}

def convert_to_string(s):
    """ convert string to integer"""
    x = -1
    try:
        number = ''
        for item in s:
            number += DIGIT_DICT[item]
        x = int(number)
        print(f"Conversion succeeded x = {x}")
    except (KeyError, TypeError):
        print("Conversion failed")

    return x

print(convert_to_string("one three seven six matis".split()))

# List Comprehensions
#[expr(item) for item in iterable]
words = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor".split()
print([len(word) for word in words])


f = [len(str(factorial(x))) for x in range(20)]
print(f)
#Set Comprehensions
s = {len(str(factorial(x))) for x in range (20)}
print(s)

#Dictionary Comprehensions
"""
{
key_expr(item) : value_expr(item)
for item in iterable
}
"""
country_to_capital = {
'United Kingdom': 'London',
'Brazil' : 'Brasilia',
'Sweden' : 'STockholm'
}

#Invert Dictionary
#capital cities as the keys on the left, countries as the values on the right
capital_to_country = {capital: country for (country, capital) in country_to_capital.items()}
print(capital_to_country)
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

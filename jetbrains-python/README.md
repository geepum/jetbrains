# Python notes

## Useful functions

eval()
- reads strings and make it a math operation
```python
eval('2 + 5') # 7
```

## identity testing

same value but different id
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, they contain the same value

# But they have different identities
print(id(a))  # 4558721352
print(id(b))  # 4560238984
```

checking the difference
```python
a = [1, 2, 3]
b = [1, 2, 3]

identity_test = a is b  # False, because a and b refer to different objects in memory
equality_test = a == b  # True, because a and b contain the same value

b = a

identity_test = a is b  # True, because now both variables refer to the same object
```

use case of `None`
```python
def say_hello(name=None):
    if name is None:
        print('Hello!')
    else:
        print(f'Hello, {name}!')


say_hello()        # 'Hello!'
say_hello('Nick')  # 'Hello, Nick!'
```
Same logic can be applied for True and False.

## list comprehension

condition
```python
# odd numbers
numbers = [4, 8, 15, 16, 23, 42, 108]
odd_list = [x for x in numbers if x % 2 == 1]  # [15, 23]
```

if and else
```python
# conditions with functions
text = ["function", "is", "a", "synonym", "of", "occupation"]
words_tion = [word for word in text if word.endswith("tion")]  
print(words_tion)  # ["function", "occupation"]
```

## default arguments

mutable objects as default
```python
def add_player(player, team=[]):
    ...
    team.append(player)
    return team
```

option 1
```python
ice_hockey_team = add_player("Chris", ["Robert", "Alice"])
print(ice_hockey_team)    # ['Robert', 'Alice', 'Chris']
```

option 2
```python
rugby_team = add_player("Robin")
print(rugby_team)     # ['Robin']

football_team = add_player("Andrew")
print(football_team)  # ['Robin', 'Andrew']
print(rugby_team)     # ['Robin', 'Andrew']
```

better way
```python
def add_player(player, team=None):
    if team is None:
        team = []
    team.append(player)
    return team
```

## lambda function

invoking lambda function
```python
(lambda x, y: (x + y) % 2)(1, 5)
# The output is 0

func = lambda x, y: (x + y) % 2
func(1, 10)
# The output is 1

lambda x: 'even' if x % 2 == 0 else 'odd'

lambda x:
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'
```

when to use
```python
def create_function(n):
    return lambda x n * x

# Creating a function that doubles its argument
doubler = create_function(2)

# This function will triple its argument
tripler = create_function(3)

doubler(2)
# Outputs 4

tripler(2)
# Outputs 6
```

## map()
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def doubler(x):
    return 2*x

doubled_numbers = map(doubler, numbers)

print(list(doubled_numbers))
# Outputs [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

```python
doubled_numbers = map(lambda x: 2*x, numbers)

print(list(doubled_numbers))
# Outputs [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

```python
x_list = [1, 2, 3] 
y_list = [4, 5, 6]
z_list = [7, 8, 9] 

s = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))

print(s)
# The output is [12, 15, 18]
```

## filter
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = filter(lambda x: x % 2, numbers)

print(list(odd_numbers))
# The output is [1, 3, 5, 7, 9]
```

```python
letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']

def choose_vowels(letters):
	vowels = ['a', 'e', 'i', 'u', 'o']
	return list(filter(lambda x: x in vowels, letters))

print(choose_vowels(letters))
```

```python
def celsius_to_fahrenheit(c):
    return ((c + 40) * 1.8) - 40


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))

temp_over_80 = list(filter(lambda x: x > 80, daily_temp_f))
```

## args
```python
def recipe(*args, sep=" or "):
    return sep.join(args)


print(recipe("meat", "fish"))               # meat or fish
print(recipe("meat", "fish", sep=" and "))  # meat and fish
```


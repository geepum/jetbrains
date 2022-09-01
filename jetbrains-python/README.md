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




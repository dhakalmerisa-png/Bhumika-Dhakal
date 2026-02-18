# Python
 ## * Introduction
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs qwith fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. 
This means that prototyping can be very quick.


 ## * Core concepts
    
**Variables**: Think of variables as labeled containers that store data like numbers (age = 25) or text (name = "Alice").

**Indentation**: Unlike many other languages that use curly braces, Python uses whitespace indentation to define code blocks.

**Functions**: These are reusable blocks of code that perform a specific task, making your programs modular and organized.

**Control Flow**: You use conditional statements (if, elif, else) and loops (for, while) to control the order in which your code runs, allowing the program to make decisions and repeat tasks. 




```python
  print("Hello, I'm Python!")

  Hello, I'm Python!
```
## *Core Language Features

### Keywords: 
These are reserved words that have special meanings and cannot be used as variable names. They define the structure and logic of the language.

**Control Flow**: if, elif, else, for, while, break, continue.

**Function & Class Definition**: def, class, lambda, return, yield.

**Module Management**: import, from, as.
Exception Handling: try, except, raise, finally.

### Built-in Functions:
 These are functions available at all times without needing to import modules. They perform common tasks.

**print()**: Displays output to the console.

**len()**: Returns the length of an object (string, list, tuple, etc.).

**input()**: Accepts user input from the console.

**range()**: Generates a sequence of numbers, often used in for loops.

**type()**: Returns the type of an object.

**dir()**: Returns a list of attributes and methods of an object or in the current namespace. 

## * Data Structures & Operations

Python offers powerful built-in data structures and associated methods. 

**Lists**: Ordered, mutable collections of items (append(), insert(), pop(), sort(), reverse(), etc.).

**Dictionaries**: Unordered collections of key-value pairs (get(), setdefault(), keys(), values(), etc.).

**Strings**: Sequences of characters with numerous methods (capitalize(), find(), count(), strip(), upper(), join(), etc.).

**Sets**: Collections of unique elements (add(), remove(), union(), etc.).

**Slicing**: A powerful way to extract a subset of a sequence using [start:stop:step] syntax. 

## * Expanding Functionality with Modules and Libraries
Python's strength lies in its extensive standard library and third-party packages, accessed via the import statement. 

### Standard Library Modules:

**os and pathlib**: For interacting with the operating system and handling file paths.

**math**: Provides mathematical functions and constants (e.g., math.sqrt(), math.pi).

**sys**: For accessing system-specific parameters and functions, including command-line arguments via sys.argv.

**collections**: Offers specialized container datatypes like Counter and deque.

**argparse**: For writing user-friendly command-line interfaces.

### Package Management:
**pip**: The standard package manager used to install and manage third-party libraries (e.g., pip install requests). 

_**There are 35 keywords in python.
And four soft keywords.**_ 
**(match	case	_	type)**

[GitHub commands](    https://www.google.com/search?q=github+basic+commands&newwindow=1&sca_esv=6a3dc1d72e9664c9&rlz=1C1PNBB_enNP1194NP1194&biw=1707&bih=932&sxsrf=ANbL-n4QjF8BzhLN4y0Af2WYUbRQBZFtiw%3A1771219990669&ei=FqySaYTEKK7F4-EP68WNGA&oq=github+basic+c&gs_lp=Egxnd3Mtd2l6LXNlcnAiDmdpdGh1YiBiYXNpYyBjKgIIADIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5I8xFQxQFYygNwAXgBkAEAmAHQAaAB9wKqAQUwLjEuMbgBAcgBAPgBAZgCA6ACjAPCAgoQABiwAxjWBBhHwgIKEAAYgAQYFBiHAsICCxAAGIAEGJECGIoFmAMAiAYBkAYIkgcFMS4xLjGgB6YLsgcFMC4xLjG4B4MDwgcDMi0zyAcQgAgA&sclient=gws-wiz-se)

![alt text](2022-07-19-Melhores-cursos-de-Python.jpg)


Starting code sadhai gap binna suru huncha
body ma chai gap hunna paryo 

##### indentation is major thing of python

##### : is used to make body (statement ko body bhitra)

```python
age=10
if age>=18 :
 print("you can vote")
else:
    print("you cannot vote")

    Output : you cannot vote

age =20
if age>=18 :
   print("you can vote")
print("you cannot vote")

Output : you can vote
        you cannot vote
```

### Elif=else if ("if the previous conditions were not true, then try this condition".)


```python
num=20
    if num>0:
       print("positive")
    elif num<0:
       print("negative")
    else:
       print("zero")

       Output: positive
```
```python
num=20
    if num>0:
       print("positive")
    if num<0:
       print("negative")
    else:
       print("zero")

       Output : positive
                zero
```
### How to handle thoose data?? (data structure) 
* array python ma exact array hudena tara testo data type chai banauna milcha-(same data type)
### known as list (same ra diff/multiple datatype duitai rakhna milcha)
 ## datatype python le run time ma nei decide garcha

 # *List
 #### vaule can be changed
  ```python
  fav_fruits=["apple", "banana", "cherry"]
print(fav_fruits[0])  
print(fav_fruits[2]) 

output :apple
       cherry

fav_fruits[1]="grape"
print(fav_fruits)

Output: ['apple', 'grape', 'cherry']

fav_fruits.append("orange")
print(fav_fruits)

Output :['apple', 'grape', 'cherry', 'orange']

fav_fruits.insert(1,"kiwi")
print(fav_fruits) 

Output :['apple', 'kiwi', 'grape', 'cherry', 'orange']
```

```python
fav_fruits.remove("cherry")
print(fav_fruits)

Output : ['apple', 'kiwi', 'grape', 'orange']

fav_fruits.pop(2)
print(fav_fruits)

Output: ['apple', 'kiwi', 'orange']

fav_fruits.sort()
print(fav_fruits)

Output :['apple', 'kiwi', 'orange']

fav_fruits.sort(reverse=True)
print(fav_fruits)

Output:['orange', 'kiwi', 'apple']
```
```python
numbers=[5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)

OUTPUT:[1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)

OUTPUT:[9, 6, 5, 5, 2, 1]
```

 ```python
 fav_fruits=["apple", "banana", "cherry"]
print(fav_fruits)

Output:

fav_fruits2=["grape", "kiwi"]
print(fav_fruits2)

combined_fruits=fav_fruits+fav_fruits2
print(combined_fruits)
```
# *Tuple
 #### vaule cannot be changed (emutable)
 #### ekchuti bhanaye paxi read matra garna milcha

 ```python
 fav_fruits=("apple,banana,cherry")
print(fav_fruits[0])
print(fav_fruits[2])  

Output:['apple', 'banana', 'cherry', 'grape', 'kiwi']






# 0x09. Python - Everything is object

This project is a little bit different than the usual projects.
The first part is only questions about Python’s specificity like
“What would be the result of…”.
The Answers for each question is found in a one line text file. (`*.txt`)

## Mandatory

[0-answer.txt](./0-answer.txt)

- What function would you use to get the type of an object?

[1-answer.txt](./1-answer.txt)

- How do you get the variable identifier (which is the memory address in
  the CPython implementation)?

[2-answer.txt](./2-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 89
>>> b = 100
```

[3-answer.txt](./3-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 100
>>> b = 100
```

[4-answer.txt](./4-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 100
>>> b = a
```

[5-answer.txt](./5-answer.txt)

- In the following code, do a and b point to the same object?
  Answer with Yes or No.

```python
>>> a = 100
>>> b = a + 1
```

[6-answer.txt](./6-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

[7-answer.txt](./7-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 is s2)
```

[8-answer.txt](./8-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

[9-answer.txt](./9-answer.txt)

- What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

[10-answer.txt](./10-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

[11-answer.txt](./11-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

[12-answer.txt](./12-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

[13-answer.txt](./13-answer.txt)

- What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

[14-answer.txt](./14-answer.txt)

- What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

[15-answer.txt](./15-answer.txt)

- What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1 += [4]
print(l2)
```

[16-answer.txt](./16-answer.txt)

- What does this script print?

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

[17-answer.txt](./17-answer.txt)

- What does this script print?

```python
def increment(n):
    n.append(4)
You should check for both 3 and 5 first
l = [1, 2, 3]
increment(l)
print(l)
```

[18-answer.txt](./18-answer.txt)

- What does this script print?

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

[19-copy_list.py](./19-copy_list.py)

- A function that returns a copy of list.
- The file must be 3 lines long.

[20-answer.txt](./20-answer.txt)

- Is `a` a tuple? Answer with Yes or No.

```python
a = ()
```

[21-answer.txt](./21-answer.txt)

- Is `a` a tuple? Answer with Yes or No.

```python
a = (1, 2)
```

[22-answer.txt](./22-answer.txt)

- Is `a` a tuple? Answer with Yes or No.

```python
a = (1)
```

# Chapter 10 PY4E Quix

### 1. What is the difference between a Python tuple and a Python list?
- [ ] Tuples can be expanded after they are created and lists cannot
- [ ] Lists maintain the order of the items and tuples do not maintain order
- [ ] Lists are indexed by integers and tuples are indexed by strings
- [x] Lists are mutable and tuples are not

### 2. Which of the following methods work both in Python lists and Python tuples?
- [ ] append()
- [ ] reverse()
- [ ] pop()
- [x] index()
- [ ] sort()

### 3. What will end up in the variable _y_ after this code is executed?
```
x , y = 3 , 4
```
- [ ] 3
- [ ] A two item list
- [x] 4
- [ ] A dictionary with the key 3 mapped to the value 4
- [ ] A two item tuple

### 4. In the following Python code, what will end up in the variable _y_?
```
x = { 'chuck': 1, 'fred': 42, 'jan': 100}
y = x.items()
```
- [x] A list of tuples
- [ ] A list of integers
- [ ] A list of strings
- [ ] A tuple with three integers

### 5. Which of the following tuples is greater than _x_ in the following Python sequence?
```
x = (5, 1, 3)
if ??? > x :
    ...
```
- [ ] (4, 100, 200)
- [ ] (5, 0, 300)
- [ ] (0, 1000, 2000)
- [x] (6, 0, 0)

### 6. What does the following Python code accomplish, assuming the _c_ is a non-empty dictionary?
```
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
```
- [ ] It computes the largest of all the values in the dictionary
- [ ] It computers the average of all the values in the dictionary
- [x] It creates a list of tuples where each tuple is a value, key pair
- [ ] It sorts the dictionary based on its key values

### 7. If the variable _data_ is a Python list, how do we sort it in reverse order?
- [ ] data = sortrev(data)
- [ ] data.sort.reverse()
- [ ] data = data.sort(-1)
- [x] data.sort(reverse=True)

### 8. Using the following tuple, how would you print 'Wed'?
- [ ] print(days{2})
- [ ] print(days.get(1,-1))
- [ ] print(days(2))
- [x] print(days[2])
- [ ] print(days[1])

### 9. In the following Python loop, why are there two iteration variables (k and v)?
```
c = {'a':10, 'b':1, 'c':22}
```
- [ ] Because there are two items in the dictionary
- [ ] Because for each item we want the previous and current key
- [ ] Because the keys for the dictionary are strings
- [x] Because the items() method in dictionaries returns a list of tuples

### 10. Given that Python list and Python tuples are quite similar - when might you prefer to use a tuple over a list?
- [ ] For a list of items that you want to use strings as key values instead of integers
- [ ] For a list of items you intend to sort in place
- [x] For a temporary variable that you will use and discard without modifying
- [ ] For a list of items that will be extended as new items are found

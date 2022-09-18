print("hello")
#string concatenation must have the same data types on both sides
#and or not must be like this
#membership opreators
a = "hello"
print('h' in a)
print('h' not in a)

#identity operator is same as the comparison == opreator
x=10
y=10
print(x is y,x==y)
print(x is not y,x!=y)

#bitwise opreator 
# & and ,| or ,^ xor
#it works on the binary forms 
x = 10
y = 8
print(bin(x))#bin is used to find binary value of the number
print(bin(y))

print(x&y,bin(x&y))
print(x|y,bin(x|y))
print(x^y,bin(x^y))

#data types
"""
Mutable is that you can change value of anyting that you written without creating it agian as we change any value by using index in list 
Immutable is that you can not change value of define object you must have to redefine it 

1.Numeric(I)
  -integers 
  -float
  -complex numbers
2.Sequence type
    -String(I)
    -List(M) order sequence of items a = [10,10.9,"a"]
    -tuple(I) same as list but fast and use () a =() must have more than one value 
3.Dictionary(M) unordered collection of key value pairs key must be unique d={'coursen':'python'} print(d[coursen]) 
4.set(I) unordered collection of unique values a = {1,2,3}

"""
#user input
val1 = input("Enter value 1 : ")

print(val1)
print(type(val1))

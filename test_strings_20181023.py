'''
str1="Hello"
str2='there'
bob=str1+str2
print(bob)
str3='123'
str3=str3+1
x=int(str3)+1
print(x)
'''

'''
name=input('Enter:')
print(name)
apple=input('Enter:')
x=apple-10
x=int(apple)-10
print(x)
'''

'''
fruit='banana'
letter=fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)
'''

'''
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index, letter)
    index=index+1
'''

'''
fruit='banana'
for letter in fruit:
	print(letter)
index=0
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1
'''

'''
word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
print(count)
'''

'''
for letter in 'banana':
    print(letter)
'''

if word =='banana':   
    print('All right, bananas.')
    
if word <'banana':
    print('Your word,'+word +', comes before banana.')
elif word > 'banana':
    print('Your word,'+word +', comes after banana.')
else:
    print('All right, bananas.')

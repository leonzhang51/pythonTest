age = 20
name="ali"
print("hello world \n",end="!") #switch to new line and add ! at the begin of second line
print(f"my name is", name, "and my age is" ,age,sep=",") #add comma between two arguments

#help(print) #to get information about a function

rng=range(0,20,2) #range(start,stop,step) to create a range of numbers
print(list(rng))

strings=["my","world","apple","banana"]
lengths=map(len,strings) #map(function,iterable) to apply a function to an iterable and return an iterator, here to get the length of each string
print(list(lengths))

lengths=map(lambda x:x.upper()+"s",strings) #map(function,iterable) to apply a function to an iterable and return an iterator, here to upper case each string and add "s" at the end
print(list(lengths))

def add_s(string):
    return string.upper()+"s"
lengths=map(add_s,strings) #map(function,iterable) to apply a function to an iterable and return an iterator, here to add "s" at the end of each string
print(list(lengths))

def longer_than_4(string):
    return len(string)>4
lengths=filter(longer_than_4,strings) #filter(function,iterable) to apply a function to an iterable and return an iterator, here to filter the strings that are longer than 4 characters
print(list(lengths))

lengths=filter(lambda x:len(x)>4,strings) #filter(function,iterable) to apply a function to an iterable and return an iterator, here to filter the strings that are longer than 4 characters
print(list(lengths))

numbers={1,4,23,2,4,5}
print(sum(numbers,10)) #sum(iterable,start) to add all the numbers in the iterable and return the sum

sorted_numbers=sorted(numbers) #sorted(iterable) to sort the numbers in the iterable and return a list
print(sorted_numbers)

sorted_numbers=sorted(numbers,reverse=True) #sorted(iterable,reverse) to sort the numbers in the iterable and return a list, here to sort the numbers in descending order
print(sorted_numbers)

people=[{"name":"ali", "age":20},{"name":"mohamed", "age":30},{"name":"tom", "age":31},{"name":"david", "age":32},{"name":"bahaa", "age":40}]
sorted_people=sorted(people,key=lambda person:person["age"]) #sorted(iterable,key) to sort the people in the iterable and return a list, here to sort the people in ascending order based on their age
print(sorted_people)

sorted_people=sorted(people,key=lambda person:person["age"],reverse=True) #sorted(iterable,key) to sort the people in the iterable and return a list, here to sort the people in descending order based on their age
print(sorted_people)

#loop over a list enumerated
tasks=["write report","prepare presentation","send email","submit report","review code","debug code"]

for index,task in enumerate(tasks):
    print(f"task {index+1}: {task}")
    
for index in range(len(tasks)):
    print(f"task {index+1}: {tasks[index]}")

#zip function, to combine multiple iterables
names=["ali","mohamed","tom","david","bahaa"]
ages=[20,30,31,32,40]
gender=["male","male","male","male","male"]
for name,age,gen in zip(names,ages,gender):
    print(f"name: {name}, age: {age}, gender: {gen}")
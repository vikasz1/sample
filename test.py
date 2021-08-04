# import random

# color = ['red','brown','green']

# outcome  = random.randint(1,6)
# print("Dice: ",outcome)

# choose = random.choice(color)
# print(choose)

# list = []
# for x in range(50):
#     a = int(input())
#     list.append(a)

# print(sum(list))

# list = [9,7,5,4]
# for x in list:
#     print(x,end="-")


# def jungle(animal):
#     if animal == "lion":
#         return "It is a dangerous animal"
#     else:
#         return "It is not dangerous animal"
# print(jungle(animal))

# def addTwo(list):
#     return max(list)

# num = 5
# list = []
# while num != 0:
#     print("Please enter a number here : ")
#     num = int(input())
#     list.append(num)

# print(addTwo(list))

# def personalInfo(name,age):
#     return f"My name is {name} and My age is {age}" # Formatted string

# print(personalInfo(age = 8,name = "vikas"))


para = "this this is is my my my home ho"
my_dict = {}
splitted = para.split()
for word in splitted:
    if word not in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] += 1
# for w in sorted(my_dict, key=my_dict.get, reverse=True):
#     print(w, my_dict[w])
    
# print(sorted(my_dict))
sorted_number = sorted(my_dict,key = my_dict.get,reverse=True)
print(sorted_number[0])




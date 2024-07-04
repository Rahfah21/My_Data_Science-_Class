# # Function Class
# def greeting(name):
#     print("Good Morning",name)
#     print('Good Morning ' + name)
# greeting('Hajar')
# greeting('Dami')
# greeting('')
# #def power2()
# def greeting(country,name='user'):
#     print('Good Morning ' + name + ', how is ' + country)
#     print(f'Good Morning {name}, how is {country}')
# greeting('USA','Amina')
# print(greeting('Canada','Tosin'))
# print()
# print(2*2)
# print()
# print(2**5)
# print()
# def power(number,index):
#     print(number**index)
# power(2,6)
# print()
# def power(Number,Power):
#     print(Number**Power)
# power(2,4)
# print()
# # Create a function 
# def cal(Goods,Tax):
#     print(Goods*Tax)
# Tax=cal(10000,0.3)
# #Claas 2
# # Items=['Car', 'plate','Phone','Book','Laptop']
# # Correction on Tax
# def Total_price(amount,tax_percent):
#     total =  amount + (amount * tax_percent/100) 
#     print(total)
#     return(total)
# Total_price(1000,15)
# print()
# Ans=Total_price(1000,25)
# print(Ans)
# print(Ans + 2500)
# print(Ans * 0.9)
# # Second Class Work
# def pluraliseItems(itemList):
#     for item in itemList:
#         print(item + 's')
# Samples=['Car', 'plate','Phone','Book','Laptop']
# pluraliseItems(Samples)
# ## Corection
# def pluraliseItems(itemList):
#     for item in itemList:
#         if item[-1]== 'e' and item[-2]=='f':
#          print(item[0:-2] + 'ves')
#         continue
#     print(item + 's')
# Samples=['Car', 'plate','Phone','wife','knife']
# pluraliseItems(Samples)
# ## TO do
# amount = '2000'
# val = int(amount)
# print(val/2)
# print(val//3)
# print(val/3)
# print()
# amount = 'N2000'
# amount = amount.strip('N')
# print(amount)
# val = int(amount)
# print(val/4)
# weight = '20kg'
# weight = weight.strip('kg')
# value=int(weight)
# print(value/5)
# print()
# amount = '20,000'
# amount = amount.split(',')
# print(amount)
# print()
# amount = ''.join(amount)
# print(amount)
# print()
# val = int(amount)
# print(val/2)
# print()
# class person:
#     def __init__(self,name, age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#         print(self.name,self.age, self.height)
#         sam = person('samuel',14,'150cm')
#         human2 = person('joy',15,'45inches')
#         sam
#         human2
#         def age(birth_year,discurrent_year):
#             years = discurrent_year-birth_year 
#             return f"child's age is {years}"
#         my_child_age = age (2017, 2024)
#         print(f+"my{my_child_age}")
# Create a function that add it argument to the end at a list



# fruit = ['Orange','Apple','Banana']
# New_fruit = 'Cherry'
# Fruits =(fruit,New_fruit)
# print(Fruits)
# def add_value(fruit1):
#     if fruit1:
#         fruit1[0]="Abu"
#         return(fruit1)
 
 
# def add_value(value): 
#  for x in value:
#     if x == value:
#         print(x + 'X')
# Value1 = ['200kg','50kg','40kg']
    
    
# # Method 1
# def add_weights(weights):
#     total = 0
#     for weight in weights:
#         strval = weight.strip('kg')
#         numval = int(strval)
#         total = total + numval
#     return (total)
# goods = ['200kg','50kg','40kg']
# ans = add_weights(goods)
# print(ans)
# print(f'average is: {ans/3}')
#Print()
# def add_number(numbers):
#     total = 0
#     for x in numbers:
#      return (total)
# values = [2,4,5,6,4,8]
# ans2 =add_number(values)
# print(ans2)

numbers = [2,4,5,6,4,8]
def totalsum(values):
    total = 0
    for val in values:
        total = total + val
    return total
ans3 = totalsum(numbers)
print(ans3)
    
print(f' The average is: {ans3/6}')

        






    





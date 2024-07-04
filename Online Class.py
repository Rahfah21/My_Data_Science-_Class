# Class
# my_list=[2,"good"]
# our_list=[2,4,8]
# var=4
# word='Bad'
# print(type(our_list))
# print(type(my_list))
# my_list.append('new')
# print(my_list)
# print(type(var))
# print(type(word))
# print(type({}))
#   class Car:
# def_init_(self,color,make,model)
# self.colour=color
# self.make=make
 
class car:
    def init (self,color,make,model):
        self.color=color
        self.make=make
        self.model=model
        print("New instance of car created")
car1=car('blue','Toyota','Camry')
print(car1.color)
    # def describe(self):
    #      print(f'This is a {self.color}')
    
        
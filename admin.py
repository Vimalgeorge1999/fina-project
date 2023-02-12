import json
class admin:
    def __init__(self):
        self.food_item ={}
        self.food_id = len(self.food_item)+1
    def add_new_food_items(self):
        self.name=input("enter name :")
        self.quantity=int(input("enter the quantity of the food :"))
        self.price=int(input("enter the price :"))
        self.stock=int(input("enter the number of stock available :"))
        self.discount=int(input("enter the food discount :"))
        self.item={"name":self.name,"quantity":self.quantity,"price":self.price,"stock":self.stock,"discount":self.discount}
        self.food_id = len(self.food_item)+1
        self.food_item[self.food_id]=self.item
        with open("food_item.json","w") as f:
            json.dump(self.food_item,f)
        return self.food_item
    def view_food_items(self):
        l=[]
        with open("food_item.json","r") as f:
            v=json.load(f)
        for i in v.values():
            l.append(i)
        return l

    def edit_fooditem(self):
        self.food_item[1]["name"]=input("enter the food name : ")
        self.food_item[1]["quantity"]=int(input("enter the quantity : "))
        self.food_item[1]["price"]=int(input("enter the price : "))
        self.food_item[1]["stock"]=int(input("enter the stock : "))
        self.food_item[1]["discount"]=int(input("enter the discount : "))

    def remove(self):
        food_item = int(input("enter food id which you want to remove: "))
        del self.food_item[food_item]
        print("remaining food item is :" ,self.food_item)
        with open("food_item","w") as f:
            json.dump(self.food_item,f)
        return self.food_item

c=admin()
print(c.add_new_food_items())
print(c.add_new_food_items())
print(c.add_new_food_items())
print("*"*50)
print(c.view_food_items())
print("*"*50)
print(c.edit_fooditem())
print("*"*50)
print(c.remove())
print("*"*50)


    





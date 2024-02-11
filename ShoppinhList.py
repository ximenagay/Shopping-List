print("I´m going to the supermarket later. What do you want for dinner tonight?")
item_1 = input()
print("What do you want for dessert?")
item_2 = input()
print("And for after, what snack do you want?")
item_3 = input()
shopping_list = [item_1, item_2, item_3]
print("The shopping list is:", shopping_list) 

shoppin_list = [input("ingrese item {}:".format(i+1)) for i in range (3)]
print(shopping_list)

input_1 = "30"
input_2 = "40"
suma = int(input_1) + int(input_2)
print(suma)

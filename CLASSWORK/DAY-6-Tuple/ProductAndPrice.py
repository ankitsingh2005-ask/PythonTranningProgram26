# create an empty list to stroe product names and their prices
products_name = []
products_price = []

# take input from user
print("Enter the product names and their prices ")

# take input from user
for i in range(5):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products_name.append(name)
    products_price.append(price)


# typecasting the lists into tuples
products_name_tup = tuple(products_name)
# display the product names tuple
print("The product names tuple is: ", products_name_tup)

products_price_tup = tuple(products_price)
# display the product prices tuple
print("The product prices tuple is: ", products_price_tup)

# check for the lowest price in the tuple 
lowest_price = min(products_price_tup)
# display the lowest price
print("The lowest price is: ", lowest_price)

#check for the highest price in the tuple
highest_price = max(products_price_tup)
# display the highest price
print("The highest price is: ", highest_price)

#count the number of product whose price is greater than 4000 along with their names
count = 0
for i, price in enumerate(products_price_tup):
    if price > 4000:
        count += 1

        #display the product name and price
        print("Product name: ", products_name_tup[i], " Price: ", price)



    


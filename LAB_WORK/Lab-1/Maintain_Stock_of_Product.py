'''Lab 4: Inventory Management
Problem Statement:
Create a dictionary to maintain the stock of products in a shop.
Example:
{
'Laptop': 15,
'Mouse': 40,
'Keyboard': 25,
'Monitor': 10
}
Implement the following:
• Add a new product.
• Update the stock of an existing product.
• Remove a product from inventory.
• Display products having stock less than 20.
• Display the total number of items available in the inventory. '''

# Create a dictionary to maintain the stock of products in a shop
inventory = {'Laptop': 15, 'Mouse': 40, 'Keyboard': 25
, 'Monitor': 10}

# Add a new product
new_product = input("Enter the name of the new product: ")
new_stock = int(input("Enter the stock of the new product: "))
inventory[new_product] = new_stock

# Update the stock of an existing product
update_product = input("Enter the name of the product to update stock: ")   

# Check if the product exists in the inventory
if update_product in inventory:
    new_stock = int(input("Enter the new stock of the product: "))
    inventory[update_product] = new_stock

# Remove a product from inventory
remove_product = input("Enter the name of the product to remove from inventory: ")

# Check if the product exists in the inventory
if remove_product in inventory:
    del inventory[remove_product]

# Display products having stock less than 20
print("Products having stock less than 20: ")

for product, stock in inventory.items():
    if stock < 20:
        print(f"Product: {product}, Stock: {stock}")

# Display the total number of items available in the inventory
total_items = sum(inventory.values())

print("Total number of items available in the inventory: ", total_items)


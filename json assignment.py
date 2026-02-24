
import json

inventory = [
            {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
            {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
            ]

with open("inventory.json", "w") as f:
    json.dump(inventory,f)

with open("inventory.json", "r") as f:
    library_read = json.load(f)    
    print(f"Total number of books currently in the file: {len(inventory)}")
   

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
    
inventory.append(new_book)
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4)

with open("inventory.json", "r") as f:
    updated_inventory = json.load(f)  

    print("Updated inventory contents:")
    for book in updated_inventory:
        print(f"Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, In Stock: {book['in_stock']}") 

    
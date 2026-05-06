"""
Fantasy Game inventory
"""

def display_inventory(inventory):  
    n = 0
    print("Inventory")
    for item, amount in inventory.items():
        print(str(amount) + " " + str(item))
        n += amount
    print("Total number of items: " + str(n))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

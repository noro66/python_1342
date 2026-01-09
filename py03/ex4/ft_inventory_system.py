if __name__ == "__main__":
    print("=== Player Inventory System ===")
    print()
    alice_inventory = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 0,
            "price": 500
        },
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "price": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "price": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "price": 200
        }
    }
    bob_inventory = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "price": 500
        },
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 0,
            "price": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 0,
            "price": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "price": 200
        }
    }
    print("=== Alice's Inventory ===")
    inventory_value = 0
    item_count = 0
    categories = {}
    for key, value in alice_inventory.items():
        if value["quantity"] >= 1:
            cate = value["category"]
            rare = value["rarity"]
            quant = value["quantity"]
            price = value["price"]
            total_value = price * quant
            print(
                f"{key} ({cate}, {rare}):",
                f"{quant}x @ {price} gold each = {total_value} gold"
                  )
            inventory_value += total_value
            item_count += quant
            if cate in categories.keys():
                categories[cate] += quant
            else:
                categories[cate] = quant

    print(f"Inventory value: {inventory_value} gold")
    print(f"Item count: {item_count} items")
    print("Categories:", end=" ")

    first = True
    for key, value in categories.items():
        if not first:
            print(", ", end="")
        print(f"{key}({value})", end="")
        first = False
    print()

    print()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice_inventory["potion"]["quantity"] -= 2
    bob_inventory["potion"]["quantity"] += 2
    print("Transaction successful!")

    print()
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion']['quantity']}")
    print(f"Bob potions: {bob_inventory['potion']['quantity']}")

    print()
    print("=== Inventory Analytics ===")
    alice_inventory_value = 0
    alice_total_item = 0
    for _, value in alice_inventory.items():
        alice_inventory_value += value["quantity"] * value["price"]
        alice_total_item += value["quantity"]

    bob_inventory_value = 0
    bob_total_item = 0
    for _, value in bob_inventory.items():
        bob_inventory_value += value["quantity"] * value["price"]
        bob_total_item += value["quantity"]

    if alice_inventory_value > bob_inventory_value:
        print(f"Most valuable player: Alice ({alice_inventory_value} gold)")
    elif bob_inventory_value > alice_inventory_value:
        print(f"Most valuable player: Bob ({bob_inventory_value} gold)")

    if alice_total_item > bob_total_item:
        print(f"Most items: Alice ({alice_total_item} items)")
    elif bob_total_item > alice_total_item:
        print(f"Most items: Bob ({bob_total_item} items)")

    rarest_item = {}
    for key, value in alice_inventory.items():
        if value["rarity"] == "rare" and value["quantity"] >= 1:
            rarest_item[key] = value["quantity"]
    for key, value in bob_inventory.items():
        if value.get("rarity") == "rare" and value["quantity"] >= 1:
            rarest_item[key] = value["quantity"]

    print("Rarest items: ", end="")
    first = True
    for rare in rarest_item.keys():
        if not first:
            print(", ", end="")
        print(rare, end="")
        first = False
    print()

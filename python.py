class GameCharacter:
    def __init__(self, name, hp, attack, defense, gold, inventory, level, experience, quests):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._gold = gold
        self._inventory = inventory
        self._level = level
        self._experience = experience
        self._quests = quests

    # Getter และ Setter สำหรับ HP
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0  # HP ไม่สามารถน้อยกว่า 0
        else:
            self._hp = value

    # Getter และ Setter สำหรับ Gold
    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        if value < 0:
            print("Gold cannot be negative!")  # แจ้งเตือนหาก gold ติดลบ
        else:
            self._gold = value

    # Getter และ Setter สำหรับ Experience
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            self._experience = 0
        else:
            self._experience = value

    def attack_enemy(self, enemy):
        damage = max(self._attack - enemy.defense, 0)  # ปรับให้ดาเมจไม่เป็นค่าลบ
        if damage > 0:
            enemy.hp -= damage
        print(f"{self._name} attacks {enemy.name} for {damage} damage!")
    
        if enemy.hp <= 0:
            enemy.hp = 0
            print(f"{enemy.name} has been defeated!")
        else:
            print(f"{enemy.name} has {enemy.hp} HP left.")


        def buy_item(self, item):
            if self.gold >= item.price:
                self.gold -= item.price
                self._inventory.add_item(item)  # ใช้ self._inventory
                print(f"{self._name} bought {item.name}!")  # ใช้ self._name
            else:
                print(f"{self._name} doesn't have enough gold for {item.name}!")  # ใช้ self._name

    def display_status(self):
        print(f"Name: {self._name}, HP: {self.hp}, Attack: {self._attack}, Defense: {self._defense}, Gold: {self.gold}, Level: {self._level}, Experience: {self.experience}")  # ใช้ self._name
    
    def use_potion(self, potion):
        if potion in self._inventory.items:  # ใช้ self._inventory
            self.hp += potion.effect_value
            self._inventory.remove_item(potion)  # ใช้ self._inventory
            print(f"{self._name} used a {potion.name} and restored {potion.effect_value} HP!")  # ใช้ self._name
        else:
            print(f"{self._name} doesn't have a {potion.name} potion!")  # ใช้ self._name



class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_character(self, character):
        damage = max(self.attack - character.defense, 0)
        if damage > 0:
            character.hp -= damage
        print(f"{self.name} attacks {character.name} for {damage} damage!")

        if character.hp <= 0:
            character.hp = 0
            print(f"{character.name} has been defeated!")
        else:
            print(f"{character.name} has {character.hp} HP left.")

class Item:
    def __init__(self, name, item_type, price, effect_value=0):
        self.name = name
        self.item_type = item_type
        self.price = price
        self.effect_value = effect_value

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} removed from inventory.")
        else:
            print(f"{item.name} is not in the inventory.")

    def display_items(self):
        if self.items:
            print("Items in inventory:")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("Inventory is empty.")

class Shop:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def display_items(self):
        print(f"Welcome to {self.name}! Here are the items for sale:")
        for item in self.inventory:
            print(f"{item.name} - {item.price} gold")

    def sell_item(self, character, item_name):
        for item in self.inventory:
            if item.name == item_name:
                character.buy_item(item)
                return
        print(f"{item_name} is not available in the shop.")

class Quest:
    def __init__(self, name, description, target, reward):
        self.name = name
        self.description = description
        self.target = target
        self.reward = reward
        self.completed = False

    def complete(self, character):
        if not self.completed:
            self.completed = True
            character.gold += self.reward["gold"]
            character.experience += self.reward["experience"]
            print(f"Quest '{self.name}' completed! {character.name} received {self.reward['gold']} gold and {self.reward['experience']} experience.")
        else:
            print(f"Quest '{self.name}' is already completed.")


sword = Item("Sword", "weapon", 100, 10)
armor = Item("Armor", "armor", 150, 5)


shop = Shop("Blacksmith Shop", [sword, armor])


player = GameCharacter("Hero", 100, 15, 5, 200, Inventory(), 1, 0, [])


goblin_quest = Quest("Goblin Slayer", "Defeat 3 goblins", target=3, reward={"gold": 50, "experience": 20})


player.quests.append(goblin_quest)


shop.sell_item(player, "Sword")
shop.sell_item(player, "Armor")


player.display_status()
player.inventory.display_items()


enemy = Enemy("Goblin", 50, 10, 2)
player.attack_enemy(enemy)

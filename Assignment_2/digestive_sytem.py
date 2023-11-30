class DigestiveSystem:
    def __init__(self):
        self.stomach = Stomach()
        self.small_intestine = SmallIntestine()
        self.large_intestine = LargeIntestine()

    def process_food(self, food):
        print(f"Digestive System: Receiving {food}")
        self.stomach.digest(food)
        self.small_intestine.absorb_nutrients()
        self.large_intestine.process_waste()

class Stomach:
    def __init__(self):
        self.contents = []

    def digest(self, food):
        self.contents.append(food)
        print(f"Stomach: Digesting {food}")

class SmallIntestine:
    def absorb_nutrients(self):
        print("Small Intestine: Absorbing nutrients from digested food")
        # Logic to absorb nutrients from digested food

class LargeIntestine:
    def process_waste(self):
        print("Large Intestine: Processing waste and excreting it")
        # Logic to process waste and excrete it

# Instantiate the digestive system
human_digestive_system = DigestiveSystem()

# Simulate the digestive process
food = "Pizza"
human_digestive_system.process_food(food)

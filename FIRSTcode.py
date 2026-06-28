class Hacker:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def introduce(self):
        print(f"👨‍💻 Hacker: {self.name}")
        print(f"⚡ Skill Level: {self.skill}")

    def __add__(self, other):
        return self.skill + other.skill


class EliteHacker(Hacker):
    def __init__(self, name, skill, rank):
        super().__init__(name, skill)
        self.rank = rank

    def introduce(self):  # Polymorphism
        print("🔥 ELITE HACKER PROFILE 🔥")
        print(f"Name : {self.name}")
        print(f"Skill: {self.skill}")
        print(f"Rank : {self.rank}")


# Objects
h1 = Hacker("Akshi", 95)
h2 = Hacker("Shadow", 90)

# Encapsulation-like access
h1.introduce()

print("\n🚀 Combined Power:", h1 + h2)

elite = EliteHacker("Akshi", 100, "Legend")
print()
elite.introduce()

print("\n🌸 Easy Peasy 😌")
print("Mission Completed Successfully ✔️")
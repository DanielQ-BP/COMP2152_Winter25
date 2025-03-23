from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        print(f"Hero created with {self._combat_strength} strength and {self._health_points} HP")

    def hero_attacks(self, monster):
        global monster_kills
        print(f"Hero attacks Monster! ({self._combat_strength} damage)")

        # Debugging check
        print(f"DEBUG: Type of monster: {type(monster)}")
        print(f"DEBUG: Attributes of monster: {dir(monster)}")

        monster.health_points -= self._health_points  # This is where the error occurs

        if monster.health_points == 0:
            print("Monster is defeated!")


    def __del__(self):
        print("The hero is being destroyed by the garbage collector")
        super().__del__()
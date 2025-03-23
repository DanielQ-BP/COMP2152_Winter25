from character import Character


class Monster(Character):
    def __init__(self):
        super().__init__()
        print(f"Monster created with {self._combat_strength} strength and {self._health_points} HP")
        print(f"DEBUG: Monster health points (after init): {self._health_points}")  # Debug

    def monster_attacks(self, hero):
        print(f"Monster attacks the Hero! ({self._combat_strength}) damage")
        hero.health_points -= self._combat_strength
        if hero.health_points == 0:
            print("The hero has been defeated!")

    def __del__(self):
        print("The hero is being destroyed by the garbage collector")
        super().__del__()
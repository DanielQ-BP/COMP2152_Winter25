import random

class Character:
    def __init__(self):
        self._combat_strength = random.randint(1, 10)
        self._health_points = random.randint(5, 20)

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 1:
            self._combat_strength = value
        else:
            raise ValueError("Combat Strength must be greater than or equal to 1")

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self._health_points = value
        else:
            self._health_points = max(0, value)

    def __del__(self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector.")

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self.health = 100
        self.level = 1
        self.mana = 50


    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value
    
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, value):
        self._level = value
    
    def level_up(self):
        self._level += 1
        self._health = 100
        self._mana = 50
        print(f"{self._name} leveled up to {self._level}!")
    

    def __str__(self):
        return f"Character: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"
    

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
# I wrote this for the codewars kata here https://www.codewars.com/kata/5941c545f5c394fef900000c/

class Warrior():
    RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    
    @staticmethod
    def get_level(experience):
        return experience // 100
        
    @staticmethod
    def get_rank(level):
        return Warrior.RANKS[level // 10]
    
    def __init__(self):
        self.experience = 100
        self.achievements = []
    
    @property
    def level(self):
        return Warrior.get_level(self.experience)
    
    @property
    def rank(self):
        return Warrior.get_rank(self.level)
    
    def increment_experience(self, amount):
        self.experience = min(self.experience + amount, 10000)
    
    def training(self, description):
        if self.level < description[2]:
            return "Not strong enough"
        self.achievements.append(description[0])
        self.increment_experience(description[1])
        return description[0]
    
    def battle(self, enemy_level):
        diff = enemy_level - self.level
        
        # invalid case
        if not 0 < enemy_level <= 100:
            return "Invalid level"
        
        # defeated case
        elif diff >= 5 and Warrior.get_rank(enemy_level) != self.rank:
            return "You've been defeated"
        
        # disadvantaged case
        elif 0 < diff:
            self.increment_experience(20 * (diff ** 2))
            return "An intense fight"
        
        # tied case
        elif diff == 0:
            self.increment_experience(10)
            return "A good fight"
        
        # marginal advantage case
        elif diff == -1:
            self.increment_experience(5)
            return "A good fight"
        
        # dominant advantage case
        elif diff < -1:
            return "Easy fight"

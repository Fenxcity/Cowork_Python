class Assassin:
    def __init__(self, name, power, weakness, health, m_attack, m_defense):
        self.name = name
        self.power = power
        self.weakness = weakness
        self.health = health
        self.m_attack = m_attack
        self.m_defense = m_defense
        self.target = None

    def attack(self, target):
        if target.health <= 0:
            print(self.name, "no puede atacar a", target.name, "porque ya está derrotado")
            return False
        if target == self.name:
            print(self.name, "no puede atacarse a sí mismo")
            return False
            
        damage = self.m_attack
        if target.weakness == self.power:
            damage *= 1.5
            print("¡Ataque efectivo! El poder", self.power, "es la debilidad de", target.name)
            
        target.health -= damage
        print(self.name, "ha atacado a", target.name, "causando", damage, "puntos de daño")
        
        if target.health <= 0:
            print(target.name, "ha sido derrotado")
        return True
        
    def defend(self, attack):
        if self.defense <= 0:
            print(self.name, "no puede defenderse más")
            return False
        defense_used = min(attack, self.defense)
        self.defense -= defense_used
        print(self.name, "ha bloqueado", defense_used, "puntos de daño")
        if self.defense <= 0:
            print(self.name, "ya no puede defenderse más")
        return True

# Creación de 5 asesinos con diferentes características
Ninja = Assassin("Ninja", "Sigilo", "Agua", 100, 25, 15)
Samurai = Assassin("Samurai", "Katana", "Honor", 120, 30, 20)
Shinobi = Assassin("Shinobi", "Veneno", "Fuego", 90, 35, 10)
Ronin = Assassin("Ronin", "Velocidad", "Oscuridad", 110, 28, 18)
Kunoichi = Assassin("Kunoichi", "Manipulación", "Luz", 95, 32, 12)

# Demostración de las habilidades de los asesinos
print("\nDemostración de habilidades:")
Ninja.attack(Samurai)
Samurai.defend(Ninja.attack)
Shinobi.attack(Ronin)
Ronin.defend(Shinobi.attack)
Kunoichi.attack(Ninja)
Ninja.defend(Kunoichi.attack)






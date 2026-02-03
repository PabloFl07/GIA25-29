class Item:
    def __init__(self):
        pass

class Covering(Item):
    def __init__(self, protection : int):
        self.protection = protection

    def get_protection(self) -> int:
        raise NotImplementedError("get_protection no implementado")
    
    def set_protection(self, protection : int):
        raise NotImplementedError("set_protection no implementado")
    
class Armor(Covering):
    def __init__(self : str):
        pass

class Shield(Covering):
    def __init__(self : str):
        pass

class Weapon(Item):
    def __init__(self, power : int):
        self.power = power

    def get_power(self) -> int:
        raise NotImplementedError("get_power no implementado")
    
    def set_power(self, power : int):
        raise NotImplementedError("set_power no implementado")


class Avatar:
    def __init__(self, name : str, life : int, strength : int, defense : int, weapon : Weapon = None , armor : Armor = None):
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        self.weapon = weapon
        self.armor = armor


    #----- GETTERS -----# 
    def get_name(self) -> str:
        return self.name
    
    def get_life(self) -> int:
        return self.life
    
    def get_strength(self) -> int:
        return self.strength

    def get_defense(self) -> int:
        return self.defense
    
    def get_weapon(self) -> Weapon:
        raise NotImplementedError("Weapon get no implementado")
    
    def get_armor(self) -> Armor:
        raise NotImplementedError("Armor get no implementado")
    

    #----- SETTERS -----#
    def set_name(self, name : str):
        self.name = name

    def set_life(self, life : int):
        self.life = life

    def set_strength(self, strength : int):
        self.strength = strength

    def set_defense(self, defense : int):
        self.defense = defense

    def set_weapon(self, weapon : Weapon):
        raise NotImplementedError("Weapon set no implementado")
    
    def set_armor(self, armor : Armor):
        raise NotImplementedError("Armor set no implementado")
    

    #----- MÉTODOS -----#
    def attack(self) -> int:
        raise NotImplementedError("Ataque no implementado")
    
    def defend(self) -> int:
        raise NotImplementedError("Defensa no implementada")
    

class Melee(Avatar):
    def __init__(self, name : str, life : int, strength : int, defense : int, weapon : Weapon = None , armor : Armor = None, shield : Shield = None):
        super().__init__(name, life, strength, defense, weapon, armor)
        self.shield = shield

    #----- GETTERS -----#
    def get_shield(self) -> Shield:
        raise NotImplementedError("Shield get no implementado")
       
    def set_shield(self, shield : Shield):
        raise NotImplementedError("Shield set no implementado")
    
class Caster(Avatar):
    def __init__(self, name : str, life : int, strength : int, defense : int, mana : int, weapon : Weapon = None , armor : Armor = None,  ):
        super().__init__(name, life, strength, defense, weapon, armor)
        self.mana = mana


    def get_mana(self) -> int:
        return self.mana

    #----- GETTERS -----#

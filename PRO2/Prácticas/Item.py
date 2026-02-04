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
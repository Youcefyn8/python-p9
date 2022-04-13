from vehicule import Vehicule

class Camion(Vehicule):
    """
    Cette classe represente un camion
    """
    def __init__(self, marque: str, modele: str, carburant: str, type_carroserie: str, vitesse: int, ptac: float):
        super().__init__(marque, modele, carburant, vitesse)
        self.set._ptac(ptac)

        def __str__(self):
            return super().__str__() + f" {self.get_ptac}"
        
        def get_ptac(self) -> float:
            return self._ptac
        
    
        def set_ptac(ptac: float):
            if type(ptac) !=float:
                raise Exception("Le ptac doit etre un float")
                
            self._ptac = ptac



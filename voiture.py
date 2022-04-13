from vehicule import Vehicule

class Voiture(Vehicule):
    """
    Cette classe reprensenter une voiture
    C'est une classe concréte qui étend (ou heriter de) la classe Vehicule.
    Cette classe est destinée a etre instatanciée.
    """
    def __init__(self, marque: str, modele: str, carburant: str, type_carroserie: str, vitesse: int):
        super.__init__(marque, modele, carburant, vitesse)
        self._type_carroserie = type_carroserie
        # il faut utiliser un setter s'il y a une procedure de vérification des donées avant l'affectation 
        self._vitesse = vitesse

    def __str__(self):
        return super().__str__() + f"{self._type_carroserie}"
    
    def get_type_carroserie(self)-> str:
        return super().__str__()

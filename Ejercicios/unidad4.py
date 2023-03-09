# 1) Crear la superclase Vehiculo y las subclases Coche,
# Bicicleta, Camioneta, Motocicleta


# necesario para usar clases abstractas
from ABC import ABC, abstractmethod

# declaración de clases
class Vehiculo(ABC):
    # Constructor
    def __init__(self,color,ruedas):
        self._color= color
        self._ruedas= ruedas

class Coche(Vehiculo):
    def __init__(self,velocidad,cilindrada):
        self._velocidad= velocidad
        self._cilindrada= cilindrada

class Bicicleta(Vehiculo):
    def _init__(self,tipo):
        self._tipo=tipo        
    
class Camioneta(Coche):
    def __init__(self,carga):
        self._carga=carga

class Motocicleta(Bicicleta):
    def __init__(self,velocidad,cilindrada):
        self._velocidad=velocidad
        self._cilindrada=cilindrada


# programa principal

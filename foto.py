from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.ancho = ancho
        self.alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if ancho > self.MAX:
            raise DimensionError("Error de dimension", "Ancho", self.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if alto > self.MAX:
            raise DimensionError("Error de dimension", "Alto", self.MAX)
        self.__alto = alto

    @property
    def ruta(self) -> str:
        return self.__ruta
    
    @ruta.setter
    def ruta(self, ruta: str) -> None:
        self.__ruta = ruta
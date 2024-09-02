class DimensionError(Exception):
    def __init__(self, message:str, dimension: str=None, maximun:int=None)-> None:
        self.message = message
        self.dimension = dimension
        self.maximun = maximun
        super().__init__(message)

    def __str__(self) -> str:
        if self.dimension and self.maximun:
            return f"{self.message}: la dimensión {self.dimension} debe ser menor o igual a {self.maximun}."
        return super().__str__()
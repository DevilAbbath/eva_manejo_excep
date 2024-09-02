from foto import Foto
from error import DimensionError

def validar_foto(ancho: int, alto: int, ruta: str):
    try:
        foto = Foto(ancho, alto, ruta)
    except DimensionError as e:
        print(f"Se ha capturado un error de dimensión: {e}")
    except Exception as e:
        print(f"Se ha capturado una excepción general: {e}")
    else:
        print("La foto se creó correctamente.")
        return foto

if __name__ == "__main__":
    # Ejemplo de uso
    validar_foto(2000, 2600, "img/logo.jpg")

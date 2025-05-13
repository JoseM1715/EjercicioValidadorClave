from  abc import ABC, abstractmethod



class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int) -> None:
        self._longitud_espera: int = _longitud_esperada

    def _validar_longitud(self, clave: str)-> bool:
        return len(clave) > self._longitud_espera

    def _contiene_mayuscula(self, clave: str)->bool:
        return any(char.isupper()for char in clave)

    def _contiene_minuscula(sel, clave: strc)-> bool:
            return any(char.isdigit()for char in clave )

    def _contiene_numero(sel, clave: strc)-> bool:
            return any(char.isdigit()for char in clave )

@abstractmethod
def es_valida(self, clave: str) -> bool:
 pass





# TODO: Implementa el código del ejercicio aquí
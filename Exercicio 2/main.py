class BuscarPalabras:
    def __init__(self, ruta):
        self._ruta = ruta

    def contar_palabras(self):
        frecuencia = {}
        with open(self._ruta, 'r') as texto:
            lineas = texto.readlines()
            for linea in lineas:
                separador = linea.strip().split(" ")
                for p in separador:
                    palabra_limpia = p.lower().strip(",.")

                    if palabra_limpia in frecuencia:
                        frecuencia[palabra_limpia] += 1
                    else:
                        frecuencia[palabra_limpia] = 1

        for palabra, contar in frecuencia.items():
           print(f"La palabra '{palabra}' se repite {contar}")

        with open("conteo.txt", "w") as conteo:
            for palabra, contar in frecuencia.items():
                conteo.writelines(f"La palabra '{palabra}' se repite {contar} veces \n")

if __name__ == "__main__":
    b = BuscarPalabras('texto.txt')
    b.contar_palabras()
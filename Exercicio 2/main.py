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

        with open("resumo_palabras.txt", "w") as resumo_palabras:
            for palabra, contar in frecuencia.items():
                resumo_palabras.writelines(f"La palabra '{palabra}' se repite {contar} veces \n")

    # def leer_resumo(self, arquivo):
    #     with open(arquivo, 'r') as resumo_palabras:
    #         resumo_palabras.readlines()

    # def menu(self):
    #     opcion = 0
    #     texto = input("Introduce o nome dun arquivo de texto para leer: ")
    #     while opcion != 3:
    #         print(              "Contador de palabrasn\n"
    #               "-----------------------------------------------\n")
    #         print("Elixe unha das opcions:\n"
    #               "1.Contar palabras\n"
    #               "2.Leer resumo de palabras\n"
    #               "3.Sair")
    #         opcion = input(" ")
    #         if opcion == 1:
    #             self.contar_palabras(texto)
    #             print("Palabras contadas correctamente")
    #         elif opcion == 2:
    #             self.leer_resumo(texto)
    #         elif opcion == 3:
    #             print("Saindo...")
    #             break

if __name__ == "__main__":
    b = BuscarPalabras("texto.txt")
    b.contar_palabras()
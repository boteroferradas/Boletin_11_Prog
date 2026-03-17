import pickle
from cliente import Cliente

class XestorClientes:
    def __init__(self, ficheiro = "clientes.dat"):
        self.ficheiro = ficheiro
        self.lista_clientes = self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open(self.ficheiro, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def gardar_clientes(self):
        with open(self.ficheiro, 'wb') as f:
            pickle.dump(self.lista_clientes, f)

    def engadir_clientes(self):
        id = input("Introduce un ID(Identificador): ")
        nome = input("Nome do cliente: ")
        telefono = input("Telefono do cliente: ")

        novo_cliente = Cliente(id, nome, telefono)

        self.lista_clientes.append(novo_cliente)
        print("Novo cliente engadido a lista")

    def modificar_clientes(self):
        pass

    def mostrar_clientes(self):
        if not self.lista_clientes:
            print("\nA lista esta baleira")
            return False
        for indice, cliente in self.lista_clientes:
            print(f"Nº{indice} - {cliente}")

        return True

    def menu(self):
        while True:
            print("XESTOR DE CLIENTES\n"
                  "------------------\n"
                  "1. Engadir novo cliente"
                  "2. Modificar datos de cliente"
                  "3. Dar de baixa"
                  "4. Listar os clientes"
                  "5. Sair")
            opcion = input("Elixa unha das opcions(1,2,etc.): ")
            match opcion:
                case 1:
                    self.engadir_clientes()
                case 4:
                    self.mostrar_clientes()
                case 5:
                    self.gardar_clientes()
                    print("Gardando cambios..."
                          "Saindo...")
import pickle
from datetime import datetime
from tarefa import Tarefa

class XestorTarefas:
    def __init__(self, ficheiro ="tarefas.dat"):
        self.ficheiro = ficheiro
        self.lista_tarefas = self.cargar_tarefas()

    def cargar_tarefas(self):
        try:
            with open(self.ficheiro, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def gardar_tarefas(self):
        with open(self.ficheiro, 'wb') as f:
            pickle.dump(self.lista_tarefas, f)

    def engadir_tarefas(self):
        estado = input("Estado da tarefa (Pendente/En proceso/Rematada): ")
        nome_tf = input("Nome da tarefa: ")
        descricion = input("Descricion da tarefa: ")
        data_str = input("Introduce a data e hora (DD/MM/AAAA HH:MM): ")
        inicio = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        duracion = int(input("Introduce unha duracion en minutos: "))

        nova_tf = (Tarefa( estado=estado,
                            nome_tf=nome_tf,
                            descricion=descricion,
                            inicio=inicio,
                            duracion=duracion
                           ))
        self.lista_tarefas.append(nova_tf)
        self.gardar_tarefas()
        print("---- Tarefa gardada con exito ----")

    def mostrar_tarefas(self):
        if not self.lista_tarefas:
            print("\n A lista esta baleira.")
            return False
        print("\nLISTA DE TAREFAS\n")
        for indice, tarefa in enumerate(self.lista_tarefas):
            print(f"Nº{indice} - {tarefa}")

        return True

    def borrar_tarefa(self):
        if self.mostrar_tarefas():
            try:
                opcion = int(input("\nIntroduce o numero de tarefa que queiras eliminar: "))
                eliminada = self.lista_tarefas.pop(opcion)
                self.gardar_tarefas()
                # print(f"DEBUG: O tipo de obxecto é {type(eliminada)}")
                print(f"Tarefa '{eliminada.get_nome_tf()}' eliminada.")
            except (ValueError, IndexError):
                print("Numero de tarefa non valido")

    def modificar_tarefa(self):
        if self.mostrar_tarefas():
            try:
                indice = int(input("\nIntroduce o numero de tarefa a modificar: "))
                tarefa = self.lista_tarefas[indice]
                print(f"\nModificando: {tarefa.nome_tf}")
                print("\nQue queres modificar\n?"
                      "1.Estado\n"
                      "2.Nome\n"
                      "3.Data e hora de inicio\n"
                      "4.Duracion\n")

                cambio = input("\nQue queres modificar? ")
                match cambio:
                    case "1":
                        novo_estado = input("Novo estado: ")
                        tarefa.estado = novo_estado
                    case "2":
                        novo_nome = input("Novo nome: ")
                        tarefa.nome_tf = novo_nome
                    case "3":
                        nova_data = input("Nova data (DD/MM/AAAA HH:MM): ")
                        tarefa.inicio = datetime.strptime(nova_data, "%d/%m/%Y %H:%M")
                    case "4":
                        tarefa.duracion = int(input("Nova duración (min): "))
                    case _:
                        print("Opcion non válida.")
                        return

                self.gardar_tarefas()
                print("Tarefa actualizada con éxito.")

            except (ValueError, IndexError):
                print("Erro: Número de tarefa ou dato introducido invalido.")

    def menu(self):
        while True:
            print("\nPrograma de xestion de tarefas\n"
                  "------------------------------\n"
                  "1.Engadir Tarefa\n"
                  "2.Borrar unha tarefa\n"
                  "3.Modificar unha tarefa\n"
                  "4.Mostrar Tarefas\n"
                  "5.Sair\n")
            opcion = input("Introduce o numero dunha das opcions: ")
            match opcion:
                case "1":
                    self.engadir_tarefas()
                case "2":
                    self.borrar_tarefa()
                case "3":
                    self.modificar_tarefa()
                case "4":
                    self.mostrar_tarefas()
                case "5":
                    print("Saindo.....")
                    break



xestor = XestorTarefas()
xestor.menu()
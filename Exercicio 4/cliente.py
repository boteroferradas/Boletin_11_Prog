class Cliente:
    def __init__(self, id: str, nome: str, telefono: str):
        self._id = id
        self._nome = nome
        self._telefono = telefono

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    def __str__(self):
        return f"ID: {self._id}, Nome: {self._nome}, Telefono: {self._telefono}"

# c = Cliente("38495784E", "Sergio", "658348192")
# print(c)
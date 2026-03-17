class Tarefa:
    def __init__(self, data, hora, duracion, nome, descricion, estado):
        self._data = data
        self._hora = hora
        self._duracion = duracion
        self._nome = nome
        self._descricion = descricion
        self._estado = estado

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def hora(self):
        return self._hora
    @hora.setter
    def hora(self, hora):
        self._hora = hora

    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricion(self):
        return self._descricion
    @descricion.setter
    def descricion(self, descricion):
        self._descricion = descricion

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado = estado
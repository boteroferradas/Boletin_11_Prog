from datetime import datetime


class Tarefa:
    def __init__(self, inicio: datetime, duracion: int, nome_tf: str, descricion: str, estado: str):
        self._inicio = inicio
        self._duracion = duracion
        self._nome_tf = nome_tf
        self._descricion = descricion
        self._estado = estado

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def inicio(self):
        return self._inicio
    @inicio.setter
    def inicio(self, inicio):
        self._inicio = inicio

    @property
    def duracion(self):
        return self._duracion
    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def nome_tf(self):
        return self._nome_tf
    @nome_tf.setter
    def nome_tf(self, nome_tf):
        self._nome_tf = nome_tf

    @property
    def descricion(self):
        return self._descricion
    @descricion.setter
    def descricion(self, descricion):
        self._descricion = descricion

    def __str__(self):
        fecha_str = self._inicio.strftime("%d/%m/%Y %H:%M")
        return f"[{self._estado}] {self._nome_tf} - Inicia: {fecha_str} ({self._duracion} min)"

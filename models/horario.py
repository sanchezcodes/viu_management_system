# -*- coding: utf-8 -*-
"""
Módulo que define la clase Horario.
"""

from .registro import Registro

class Horario(Registro):
    """
    Representa un horario en el sistema de gestión.

    Attributes:
        id (str): Identificador único del horario.
        hora_inicio (str): Hora de inicio en formato HH:MM.
        hora_fin (str): Hora de fin en formato HH:MM.
    """
    def __init__(self, id, hora_inicio, hora_fin):
        super().__init__(id)
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_horario(self):
        """
        Retorna una cadena con la información del horario.
        """
        return f"Horario {self.id}: de {self.hora_inicio} a {self.hora_fin}"

    def to_dict(self):
        """
        Convierte el objeto Horario a un diccionario.

        Returns:
            dict: Diccionario con los atributos del horario.
        """
        return {"id": self.id, "hora_inicio": self.hora_inicio, "hora_fin": self.hora_fin}

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Horario a partir de un diccionario.

        Args:
            data (dict): Diccionario con las claves 'id', 'hora_inicio' y 'hora_fin'.

        Returns:
            Horario: Instancia de Horario.
        """
        return Horario(data["id"], data["hora_inicio"], data["hora_fin"])
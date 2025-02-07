# -*- coding: utf-8 -*-
"""
Módulo que define la clase Examen.
"""

from .registro import Registro

class Examen(Registro):
    """
    Representa un examen en el sistema de gestión.

    Attributes:
        id (str): Identificador único del examen.
        materia (str): Materia del examen.
        fecha (str): Fecha del examen en formato YYYY-MM-DD.
    """
    def __init__(self, id, materia, fecha):
        super().__init__(id)
        self.materia = materia
        self.fecha = fecha

    def mostrar_examen(self):
        """
        Retorna una cadena con la información del examen.
        """
        return f"Examen {self.id}: {self.materia} en {self.fecha}"

    def to_dict(self):
        """
        Convierte el objeto Examen a un diccionario.

        Returns:
            dict: Diccionario con los atributos del examen.
        """
        return {"id": self.id, "materia": self.materia, "fecha": self.fecha}

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Examen a partir de un diccionario.

        Args:
            data (dict): Diccionario con las claves 'id', 'materia' y 'fecha'.

        Returns:
            Examen: Instancia de Examen.
        """
        return Examen(data["id"], data["materia"], data["fecha"])
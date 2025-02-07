# -*- coding: utf-8 -*-
"""
Módulo que define la clase Clase.
"""

from .registro import Registro

class Clase(Registro):
    """
    Representa una clase impartida en el sistema de gestión.

    Attributes:
        id (str): Identificador único de la clase.
        tema (str): Tema o materia de la clase.
        dia (str): Día en que se imparte la clase.
        profesor_id (str): Identificador del profesor asignado.
    """
    def __init__(self, id, tema, dia, profesor_id):
        super().__init__(id)
        self.tema = tema
        self.dia = dia
        self.profesor_id = profesor_id

    def mostrar_clase(self):
        """
        Retorna una cadena con la información de la clase.
        """
        return f"Clase {self.id}: {self.tema} el {self.dia}, Profesor ID: {self.profesor_id}"

    def to_dict(self):
        """
        Convierte el objeto Clase a un diccionario.

        Returns:
            dict: Diccionario con los atributos de la clase.
        """
        return {"id": self.id, "tema": self.tema, "dia": self.dia, "profesor_id": self.profesor_id}

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Clase a partir de un diccionario.

        Args:
            data (dict): Diccionario con las claves 'id', 'tema', 'dia' y 'profesor_id'.

        Returns:
            Clase: Instancia de Clase.
        """
        return Clase(data["id"], data["tema"], data["dia"], data["profesor_id"])
# -*- coding: utf-8 -*-
"""
Módulo que define la clase Profesor.
"""

from .registro import Registro

class Profesor(Registro):
    """
    Representa a un profesor en el sistema de gestión.

    Attributes:
        id (str): Identificador único del profesor.
        nombre (str): Nombre del profesor.
        especialidad (str): Especialidad del profesor.
    """
    def __init__(self, id, nombre, especialidad):
        super().__init__(id)
        self.nombre = nombre
        self.especialidad = especialidad

    def mostrar_profesor(self):
        """
        Retorna una cadena con la información del profesor.
        """
        return f"Profesor {self.id}: {self.nombre}, Especialidad: {self.especialidad}"

    def to_dict(self):
        """
        Convierte el objeto Profesor a un diccionario.

        Returns:
            dict: Diccionario con los atributos del profesor.
        """
        return {"id": self.id, "nombre": self.nombre, "especialidad": self.especialidad}

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Profesor a partir de un diccionario.

        Args:
            data (dict): Diccionario con las claves 'id', 'nombre' y 'especialidad'.

        Returns:
            Profesor: Instancia de Profesor.
        """
        return Profesor(data["id"], data["nombre"], data["especialidad"])
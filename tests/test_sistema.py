# tests/test_sistema.py
# -*- coding: utf-8 -*-
import unittest
from sistema_gestion import SistemaGestion
from models.examen import Examen

class TestSistemaGestion(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaGestion()
        # Limpiamos la lista de examenes para las pruebas
        self.sistema.examenes = []

    def test_crear_examen(self):
        examen = Examen("1", "Matemáticas", "2025-03-15")
        self.sistema.examenes.append(examen)
        self.assertEqual(len(self.sistema.examenes), 1)
        self.assertEqual(self.sistema.examenes[0].materia, "Matemáticas")

if __name__ == '__main__':
    unittest.main()
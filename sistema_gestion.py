# -*- coding: utf-8 -*-
"""
Módulo principal del sistema de gestión.
Este módulo contiene la clase SistemaGestion, que administra examenes, clases, horarios y profesores.
"""

import json
import datetime
from models.examen import Examen
from models.clase import Clase
from models.horario import Horario
from models.profesor import Profesor

class SistemaGestion:
    """
    Sistema de gestión que administra examenes, clases, horarios y profesores.

    Attributes:
        examenes (list): Lista de objetos de la clase Examen.
        clases (list): Lista de objetos de la clase Clase.
        horarios (list): Lista de objetos de la clase Horario.
        profesores (list): Lista de objetos de la clase Profesor.
        archivo (str): Ruta al archivo JSON de persistencia.
    """
    def __init__(self):
        self.examenes = []
        self.clases = []
        self.horarios = []
        self.profesores = []
        self.archivo = "data/datos.json"
        self.cargar_datos()

    def menu_principal(self):
        """
        Muestra el menú principal y redirige a las diferentes gestiones.
        """
        while True:
            try:
                print("\n--- Menú Principal ---")
                opcion = int(input(
                    "1. Gestionar Examenes\n"
                    "2. Gestionar Clases\n"
                    "3. Gestionar Horarios\n"
                    "4. Gestionar Profesores\n"
                    "5. Informes\n"
                    "6. Salir\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida. Intente nuevamente.")
                continue

            if opcion == 1:
                self.menu_examenes()
            elif opcion == 2:
                self.menu_clases()
            elif opcion == 3:
                self.menu_horarios()
            elif opcion == 4:
                self.menu_profesores()
            elif opcion == 5:
                self.menu_informes()
            elif opcion == 6:
                self.guardar_datos()
                print("Datos guardados. Saliendo del sistema.")
                break
            else:
                print("Opción no disponible.")

    def menu_examenes(self):
        """
        Muestra el menú de gestión de examenes.
        """
        while True:
            try:
                print("\n--- Gestión de Examenes ---")
                opcion = int(input(
                    "1. Crear Examen\n"
                    "2. Listar Examenes\n"
                    "3. Regresar\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida.")
                continue

            if opcion == 1:
                self.crear_examen()
            elif opcion == 2:
                self.listar_examenes()
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")

    def crear_examen(self):
        """
        Crea un examen solicitando los datos al usuario, validando el formato de fecha.
        """
        try:
            id = input("Ingrese ID del examen: ")
            materia = input("Ingrese materia: ")
            while True:
                fecha_str = input("Ingrese fecha (YYYY-MM-DD): ")
                try:
                    fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Formato de fecha inválido. Por favor, use YYYY-MM-DD.")
            examen = Examen(id, materia, str(fecha))
            self.examenes.append(examen)
            print("Examen creado exitosamente.")
        except Exception as e:
            print("Error al crear examen:", e)

    def listar_examenes(self):
        """
        Lista todos los examenes registrados.
        """
        if not self.examenes:
            print("No hay examenes registrados.")
        else:
            for examen in self.examenes:
                print(examen.mostrar_examen())

    def menu_clases(self):
        """
        Muestra el menú de gestión de clases.
        """
        while True:
            try:
                print("\n--- Gestión de Clases ---")
                opcion = int(input(
                    "1. Crear Clase\n"
                    "2. Listar Clases\n"
                    "3. Regresar\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida.")
                continue

            if opcion == 1:
                self.crear_clase()
            elif opcion == 2:
                self.listar_clases()
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")

    def crear_clase(self):
        """
        Crea una clase solicitando los datos al usuario.
        """
        try:
            id = input("Ingrese ID de la clase: ")
            tema = input("Ingrese tema: ")
            dia = input("Ingrese día de la clase: ")
            profesor_id = input("Ingrese ID del profesor asignado: ")
            clase = Clase(id, tema, dia, profesor_id)
            self.clases.append(clase)
            print("Clase creada exitosamente.")
        except Exception as e:
            print("Error al crear clase:", e)

    def listar_clases(self):
        """
        Lista todas las clases registradas.
        """
        if not self.clases:
            print("No hay clases registradas.")
        else:
            for clase in self.clases:
                print(clase.mostrar_clase())

    def menu_horarios(self):
        """
        Muestra el menú de gestión de horarios.
        """
        while True:
            try:
                print("\n--- Gestión de Horarios ---")
                opcion = int(input(
                    "1. Crear Horario\n"
                    "2. Listar Horarios\n"
                    "3. Regresar\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida.")
                continue

            if opcion == 1:
                self.crear_horario()
            elif opcion == 2:
                self.listar_horarios()
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")

    def crear_horario(self):
        """
        Crea un horario solicitando los datos al usuario.
        """
        try:
            id = input("Ingrese ID del horario: ")
            hora_inicio = input("Ingrese hora de inicio (HH:MM): ")
            hora_fin = input("Ingrese hora de fin (HH:MM): ")
            horario = Horario(id, hora_inicio, hora_fin)
            self.horarios.append(horario)
            print("Horario creado exitosamente.")
        except Exception as e:
            print("Error al crear horario:", e)

    def listar_horarios(self):
        """
        Lista todos los horarios registrados.
        """
        if not self.horarios:
            print("No hay horarios registrados.")
        else:
            for horario in self.horarios:
                print(horario.mostrar_horario())

    def menu_profesores(self):
        """
        Muestra el menú de gestión de profesores.
        """
        while True:
            try:
                print("\n--- Gestión de Profesores ---")
                opcion = int(input(
                    "1. Crear Profesor\n"
                    "2. Listar Profesores\n"
                    "3. Regresar\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida.")
                continue

            if opcion == 1:
                self.crear_profesor()
            elif opcion == 2:
                self.listar_profesores()
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")

    def crear_profesor(self):
        """
        Crea un profesor solicitando los datos al usuario.
        """
        try:
            id = input("Ingrese ID del profesor: ")
            nombre = input("Ingrese nombre: ")
            especialidad = input("Ingrese especialidad: ")
            profesor = Profesor(id, nombre, especialidad)
            self.profesores.append(profesor)
            print("Profesor creado exitosamente.")
        except Exception as e:
            print("Error al crear profesor:", e)

    def listar_profesores(self):
        """
        Lista todos los profesores registrados.
        """
        if not self.profesores:
            print("No hay profesores registrados.")
        else:
            for profesor in self.profesores:
                print(profesor.mostrar_profesor())

    def menu_informes(self):
        """
        Muestra el menú de informes con diferentes algoritmos de cálculo.
        """
        while True:
            try:
                print("\n--- Informes ---")
                opcion = int(input(
                    "1. Total de Examenes\n"
                    "2. Clases en un Día\n"
                    "3. Clases por Profesor\n"
                    "4. Horarios Disponibles\n"
                    "5. Regresar\n"
                    "Seleccione una opción: "
                ))
            except ValueError:
                print("Opción inválida.")
                continue

            if opcion == 1:
                print("Total de examenes:", len(self.examenes))
            elif opcion == 2:
                dia = input("Ingrese el día a consultar: ")
                total = sum(1 for clase in self.clases if clase.dia.lower() == dia.lower())
                print("Clases programadas para {}: {}".format(dia, total))
            elif opcion == 3:
                if not self.profesores:
                    print("No hay profesores registrados.")
                else:
                    for profesor in self.profesores:
                        total = sum(1 for clase in self.clases if clase.profesor_id == profesor.id)
                        print("{}: {} clases asignadas".format(profesor.nombre, total))
            elif opcion == 4:
                if not self.horarios:
                    print("No hay horarios registrados.")
                else:
                    for horario in self.horarios:
                        print(horario.mostrar_horario())
            elif opcion == 5:
                break
            else:
                print("Opción no válida.")

    def guardar_datos(self):
        """
        Guarda los datos actuales en un archivo JSON.
        """
        data = {
            "examenes": [examen.to_dict() for examen in self.examenes],
            "clases": [clase.to_dict() for clase in self.clases],
            "horarios": [horario.to_dict() for horario in self.horarios],
            "profesores": [profesor.to_dict() for profesor in self.profesores]
        }
        try:
            with open(self.archivo, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error al guardar datos:", e)

    def cargar_datos(self):
        """
        Carga los datos desde el archivo JSON si existe.
        """
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.examenes = [Examen.from_dict(item) for item in data.get("examenes", [])]
                self.clases = [Clase.from_dict(item) for item in data.get("clases", [])]
                self.horarios = [Horario.from_dict(item) for item in data.get("horarios", [])]
                self.profesores = [Profesor.from_dict(item) for item in data.get("profesores", [])]
        except FileNotFoundError:
            # Si el archivo no existe, se inicializa sin datos.
            pass
        except Exception as e:
            print("Error al cargar datos:", e)
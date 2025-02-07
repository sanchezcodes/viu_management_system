# Gestor de Exámenes

Esta es una herramienta de gestión por consola para examenes, clases, horarios y profesores.

Detalles:
	•	main.py:
Se encarga de inicializar el sistema y llamar a menu_principal().
	•	sistema_gestion.py:
Contiene la clase SistemaGestion, donde se gestionan las operaciones y menús.
	•	models/:
Se encapsulan las clases del dominio. Cada archivo define una entidad y sus métodos, lo que mejora la modularidad.
	•	data/:
Almacena el archivo datos.json que se utiliza para la persistencia mediante la librería json.
	•	utils/:
Puede incluir funciones de utilidad, como menús personalizados, validadores de entrada o conversores de datos.
	•	tests/:
Carpeta destinada a las pruebas unitarias, que permiten asegurar la calidad y robustez del sistema.
	•	README.md:
Documenta la finalidad, instalación y uso del proyecto.

## Estructura del proyecto
gestor_examenes/
├── main.py
├── sistema_gestion.py
├── models/
│   ├── init.py
│   ├── registro.py
│   ├── examen.py
│   ├── clase.py
│   ├── horario.py
│   └── profesor.py
├── data/
│   └── datos.json
├── utils/
│   ├── init.py
│   └── menu.py
├── tests/
│   ├── init.py
│   └── test_sistema.py
└── README.md

## Uso

Ejecuta `main.py` para iniciar el sistema.

## Pruebas

Desde la raíz del proyecto, ejecuta:

python -m unittest discover tests
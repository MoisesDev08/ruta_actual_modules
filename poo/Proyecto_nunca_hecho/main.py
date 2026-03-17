"""
# --- TIEMPO DE RESOLUCIÓN ---
entre el 07 y el n/a de marzo de 2026, aproximadamente 2-3 + n/a horas.

## 🧩 Reto B1 — Clases abstractas y contratos
**Objetivo:** aprender a diseñar APIs robustas.

### Enunciado
Crea una jerarquía con una clase abstracta que defina un contrato.
Implementa 3 clases concretas que cumplan ese contrato.

### Requisitos
- Uso de `abc.ABC` y `@abstractmethod`.
- Métodos abstractos + métodos concretos.
- Bitácora explicando por qué esto mejora el diseño.

### Bonus
- Añadir un método de plantilla (template method pattern).

"""

"""
Sistema de aprendizaje técnico basado en clases abstractas y el patrón
Template Method. Cada módulo (POO, Stdlib, Commonlib) se modela como una
clase concreta que representa un snapshot del estado del aprendizaje en
el momento de su creación.

Estructura general
------------------
La clase abstracta `AprendizajeTecnico` define el contrato común para
todos los módulos de la ruta de aprendizaje. Este contrato se implementa
mediante el patrón Template Method: el método de alto nivel
`proceso_de_aprendizaje()` ejecuta una secuencia de pasos fijos, pero
delegando los detalles específicos en métodos abstractos que cada módulo
debe implementar.

Cada instancia de un módulo funciona como un snapshot: contiene un
identificador único, una fecha de creación y acceso a los retos
correspondientes del módulo. Los retos existen como ficheros `.py` en el
directorio del módulo, y sus enunciados están centralizados en un archivo
`00_retos.txt`. Los retos pueden incluir tanto el enunciado como la
resolución (si ya tienen progreso), o solo el enunciado si están
pendientes. Los prefijos de los retos siguen una convención por módulo:

- POO: A1–A2, G1–G2
- Stdlib: S1–S33
- Commonlib: CML1 – CML10

Responsabilidades del contrato
------------------------------
El contrato define los pasos esenciales del aprendizaje técnico:

1. `proceso_de_aprendizaje()`
   Método plantilla que define la secuencia general del aprendizaje.
   Llama internamente a varios métodos abstractos que representan pasos
   específicos del módulo (obtención de retos, metodología aplicada,
   validación del entorno, etc.).

2. Métodos abstractos llamados por el template:
   - `obtener_retos()`: devuelve la lista estructurada de retos del módulo.
   - `tiempo_promedio_por_reto()`: define la dificultad base del módulo.
   - `aplicar_metodologia(retos)`: describe cómo se estudian y ejecutan
     los retos del módulo.
   - (Opcionales según diseño) `validar_entorno()`, `preparar_contexto()`,
     `procesar_resultados()`, etc.

3. `estimacion_de_tiempo()`
   Método concreto que calcula el tiempo total estimado del módulo como:
   número de retos × tiempo promedio por reto. Cada módulo puede ajustar
   su dificultad redefiniendo el método abstracto correspondiente.

Snapshots e integración con el sistema de retos
-----------------------------------------------
Cada módulo accede a sus retos leyendo los ficheros del directorio
correspondiente. Los retos con progreso incluyen tanto el enunciado como
la resolución; los retos pendientes contienen únicamente el enunciado.
El archivo `00_retos.txt` actúa como índice y fuente de verdad para los
enunciados.

Este diseño permite:
- Representar cada módulo como un objeto con estado propio.
- Mantener una estructura replicable entre POO, Stdlib y Commonlib.
- Extender el sistema fácilmente añadiendo nuevos módulos o nuevas fases.
- Integrar herramientas externas (como LLMs) para generar resúmenes del
  estado actual del módulo o de cada reto.

Objetivo del diseño
-------------------
El objetivo es crear una API robusta, extensible y coherente que modele
el proceso real de aprendizaje técnico. El uso de clases abstractas y
del patrón Template Method garantiza separación de responsabilidades,
consistencia entre módulos y claridad en la evolución del sistema.
"""
# reto.py, bitacora.txt, enunciado.txt

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent.resolve()
BASE_POO_DIR = Path(__file__).parent.parent.resolve()
BASE_STDLIB_DIR = BASE_DIR / "stdlib"
BASE_COMMONLIB_DIR = BASE_DIR / "commonlib"
print(Path(__file__).absolute())

# todos los archvios 00_retos.txt existen como fuente de los enunciados de los retos, y cada reto (o fusion de retos porque la mayoria 
# se fucionaron para optimizar) tiene su propio archivo .py con su enunciado y resolución (si ya tiene progreso)


from abc import ABC, abstractmethod


# 🧩 PASOS PARA COMPLETAR EL RETO B1 (2–3h)


## 1) Crear estructura de carpetas del reto (10–15 min)

# Crear carpeta reto_B1 con subcarpetas: contrato/, modulos/, utils/
# Añadir __init__.py en cada carpeta para modularizar
# Verificar que reto_B1/ existe y no es archivo
# Crear archivo main.py para pruebas finales


## 2) Diseñar la clase abstracta con contrato completo (20–25 min)

# Crear contrato/aprendizaje_tecnico.py
# Añadir clase AprendizajeTecnico heredando de ABC
# Implementar Template Method proceso_de_aprendizaje() como método concreto
# Añadir métodos abstractos: obtener_retos(), tiempo_promedio_por_reto()
# Añadir métodos abstractos: aplicar_metodologia(), procesar_resultados()
# Añadir método concreto estimacion_de_tiempo() usando num_retos * tiempo_promedio
# Añadir docstrings claros y breves


## 3) Implementar snapshot del módulo (15–20 min)

# Crear clase Snapshot en utils/snapshot.py
# Añadir id único, fecha de creación y estado inicial
# Añadir método registrar_evento() para bitácora
# Añadir método exportar_bitacora() para guardar en archivo
# Validar que snapshot se crea correctamente


## 4) Crear clase Reto + parser de 00_retos.txt (20–25 min)

# Crear utils/retos.py con clase Reto(id, titulo, contenido)
# Añadir parser que lea 00_retos.txt línea por línea
# Validar si archivo existe antes de leerlo
# Validar si archivo no es carpeta
# Crear función cargar_retos(path) que devuelve lista de Reto
# Añadir verificación: si el nombre del reto no existe, lanzar excepción clara




## 5) Implementar ModuloPOO, ModuloStdlib, ModuloCommonlib (25–30 min)

# Crear modulos/modulo_poo.py con clase ModuloPOO
# Implementar obtener_retos() usando parser de utils/retos.py
# Implementar tiempo_promedio_por_reto() con valor fijo del módulo
# Implementar aplicar_metodologia() describiendo pasos del módulo
# Implementar procesar_resultados() generando resumen simple
# Repetir estructura para Stdlib y Commonlib
# Validar que cada módulo carga sus retos correctamente


## 6) Añadir validaciones de existencia de retos y carpetas (10–15 min)

# Añadir función validar_ruta(path) en utils/validaciones.py
# Verificar si path existe y es archivo, no carpeta
# Verificar si carpeta del módulo existe
# Verificar si 00_retos.txt existe antes de cargar
# Añadir mensajes de error claros y cortos


## 7) Integrar hooks mínimos para agentes Groq (15–20 min)


# Añadir método resumir_estado() en AprendizajeTecnico como placeholder
# Añadir método analizar_retos() como hook para agente principal
# No implementar lógica completa, solo estructura para futura integración
# Añadir llamadas opcionales dentro de procesar_resultados()


## 8) Crear bitácora del módulo (10–15 min)

# Añadir atributo self.bitacora = [] en Snapshot
# Añadir método registrar_evento(msg) que agrega timestamp + msg
# Añadir método exportar_bitacora() que guarda en archivo .log
# Añadir llamadas a registrar_evento() dentro del Template Method


## 9) Crear script de prueba main.py (10–15 min)

# Importar ModuloPOO y crear instancia
# Ejecutar proceso_de_aprendizaje() y mostrar resultados
# Mostrar estimacion_de_tiempo()
# Exportar bitácora al final
# Validar que no hay errores de rutas ni de parser


## 10) Revisión final y limpieza (10–15 min)

# Revisar que todos los métodos abstractos están implementados
# Revisar que Template Method llama a los métodos correctos
# Revisar que las rutas de 00_retos.txt son correctas
# Revisar que las excepciones tienen mensajes claros
# Revisar que el código no supera 200–300 líneas totales


class AprendizajeTecnico(ABC):
    """Clase abstracta que define el contrato para el aprendizaje técnico.

    - Notes:
        - El aprendizaje tecnico se refiere a las practicas que llevo a cabo para desarrollar habilidades técnicas
        - Estas prácticas varían según el modulo pero todo se encapsula en la habilidad de programar
        - Los modulos de la ruta actual son;

            - Modulo 1: POO (actual)
            - Modulo 2: Stdlib
            - Modulo 3: Commonlib
            - Modulo 4: Estructura y arquitectura de proyectos + Ecosistema profesional
            - Modulo 5: Portafolio, proyectos y presencia online
            - Modulo 6: Perfiles, propuestas, metodos de pago y monetizacion en general

        - El contrato de esta clase abstracta es que cualquier clase concreta que herede de ella debe implementar el método proceso_de_aprendizaje,
        el cual define la forma y estructura en que se adquieren las habilidades técnicas.
        - El método proceso_de_aprendizaje es un método de plantilla (template method pattern) que establece el proceso general de aprendizaje,
        incluye metodos placeholders que cada modulo debe definir por si mismo

    """

    @abstractmethod
    def proceso_de_aprendizaje(self):
        pass

    @abstractmethod
    def estimacion_de_tiempo(self):
        pass


class ModuloPOO(AprendizajeTecnico):
    """
        Debo decidir que informacion implementare en las clases y como puedo estructurarla de forma replicable para las demás clases concretas

        - Notes:
            - Aqui iran mis decisiones tecnicas;
            # podria añadir mas metodos para funciones varias pero me conviene primero;
            #   delimitar la informacion que quiero manejar y luego expandir el contrato de la clase abstracta para incluir esa nueva informacion
            #   estructurar dicha informacion de manera replicable para las demás clases concretas
    podria añadir la lista de retos como classattr con property para que cada modulo tenga su propia lista de retos
    cada reto tiene una fase de teoria y una fase de practica, el proceso de aprendizaje solo resume los retos y sus temas
    textualmente, y la estimacion de tiempo se basa en la cantidad de retos * un tiempo promedio por reto, el cual puede variar dependiendo del modulo
    cada instancia será un modulo pero con su estado fijado en la fecha en que se crea (se usa datetime y un id por instancia) y con la información de los retos y tiempos de ese momento
    podria dejar que cada modulo tenga acceso a los archivos de cada reto para extraer su enunciado y estado actual ya que cada reto es un fichero individual
    sumado a esto le puedo añadir una llamada a una api de LLM para que haga el resumen de estado actual de cada reto y del modulo en general, esto me permite tener un resumen actualizado
    """

    def proceso_de_aprendizaje(self):
        pass

    def estimacion_de_tiempo(self):
        pass


class ModuloStdlib(AprendizajeTecnico):
    pass


class ModuloCommonlib(AprendizajeTecnico):
    pass

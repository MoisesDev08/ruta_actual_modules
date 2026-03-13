#  4. C1 + S10 + S11

# --- ENUNCIADOS ORIGINALES ---

"""

‎## 🧩 Reto C1 — Iteradores y generadores de objetos
‎**Objetivo:** dominar `__iter__` y `__next__`.
‎
‎### Enunciado  
‎Crea una colección personalizada que sea iterable.  
‎Implementa un iterador interno y uno externo.
‎
‎### Requisitos  
‎- `__iter__` y `__next__`.  
‎- Manejo correcto de `StopIteration`.  
‎- Bitácora explicando el ciclo for → iterador.
‎
‎### Bonus  
‎- Implementar slicing con `__getitem__`.
‎
‎
‎## 🧩 Reto S10 — Protocolos de colección con `collections.abc`  
‎**Objetivo:** entender los protocolos Iterable, Iterator, Sequence, Mapping.
‎
‎### Enunciado  
‎Crea una clase personalizada que se comporte como una secuencia.
‎
‎### Requisitos  
‎- Implementar `__len__` y `__getitem__`.  
‎- Verificar que `isinstance(obj, Sequence)` sea True.  
‎- Añadir un método que devuelva un iterador interno.  
‎- Bitácora explicando qué significa “protocolo”.
‎
‎### Bonus  
‎- Implementar slicing real.  
‎- Añadir validación de índices negativos.
‎
‎---
‎
‎## 🧩 Reto S11 — Pipelines con `itertools`  
‎**Objetivo:** construir pipelines de procesamiento eficientes.
‎
‎### Enunciado  
‎Diseña un pipeline que procese una lista grande de registros sin cargar todo en memoria.
‎
‎### Requisitos  
‎- Usar `itertools.islice`, `chain`, `groupby`, `filterfalse` o equivalentes.  
‎- Procesamiento lazy (sin listas intermedias).  
‎- Bitácora explicando cada etapa del pipeline.
‎
‎### Bonus  
‎- Implementar un generador propio que se integre al pipeline.  
‎- Añadir un modo que procese archivos línea por línea.

"""



# --- Reto fusión ---

"""

El reto unificado queda como un solo desafío integral que combina iteradores, protocolos de colección y pipelines lazy. Mantiene todos los requisitos y bonus, sin omitir nada, y los reorganiza en una estructura coherente y progresiva.

---

🧩 Reto Fusión — Colecciones Personalizadas + Protocolos + Pipelines Lazy

Objetivo general:  
Construir una colección personalizada profesional que:

- Sea iterable y tenga iterador interno y externo.  
- Cumpla el protocolo Sequence de collections.abc.  
- Implemente slicing real, índices negativos y acceso seguro.  
- Se integre en un pipeline lazy usando itertools y un generador propio.  
- Procese datos grandes sin cargar todo en memoria.  
- Incluya bitácoras explicando:  
  - Cómo funciona el ciclo for → iterador.  
  - Qué significa “protocolo” en Python.  
  - Cada etapa del pipeline.

---

🎯 Enunciado unificado

Diseña una colección personalizada llamada LazySequence, capaz de comportarse como una secuencia completa y, además, integrarse en un pipeline de procesamiento eficiente basado en itertools.

La colección debe:

1. Almacenar registros (pueden ser números, dicts, objetos, etc.).  
2. Ser iterable mediante:  
   - Un iterador interno (iter que devuelve un iterador propio).  
   - Un iterador externo (clase separada con next).  
3. Implementar el protocolo Sequence:  
   - len  
   - getitem con slicing real y soporte para índices negativos.  
4. Permitir construir un pipeline lazy que procese sus elementos sin crear listas intermedias.  
5. Integrarse con itertools (islice, chain, groupby, filterfalse, etc.).  
6. Permitir un modo de lectura desde archivo línea por línea.

---

📌 Requisitos obligatorios

1) Iteradores y generadores
- Implementar iter y next.  
- Manejar correctamente StopIteration.  
- Incluir una bitácora explicando:  
  - Cómo el for invoca iter.  
  - Cómo el iterador invoca next.  
  - Qué ocurre cuando se lanza StopIteration.

2) Protocolos de colección (collections.abc)
- Heredar de Sequence o verificar manualmente que isinstance(obj, Sequence) sea True.  
- Implementar len y getitem.  
- Añadir un método que devuelva un iterador interno.  
- Incluir una bitácora explicando:  
  - Qué es un protocolo.  
  - Por qué Python usa duck typing.  
  - Qué métodos exige Sequence.

3) Pipeline lazy con itertools
Construir un pipeline que:

- Procese una lista grande de registros sin cargar todo en memoria.  
- Use al menos tres herramientas de itertools:  
  - islice  
  - chain  
  - groupby  
  - filterfalse  
  - u otras equivalentes  
- No genere listas intermedias (todo debe ser lazy).  
- Incluir una bitácora explicando cada etapa del pipeline.

---

⭐ Bonus (todos integrados)

Bonus de iteradores
- Implementar slicing con getitem.

Bonus de Sequence
- Slicing real (objetos slice).  
- Validación de índices negativos.

Bonus de pipelines
- Crear un generador propio que se integre al pipeline.  
- Añadir un modo archivo:  
  - Procesar archivos línea por línea.  
  - Integrarlo al pipeline sin cargar el archivo completo.

---

🧱 Estructura sugerida del proyecto

`
lazy_sequence/
│
├── lazy_sequence.py
│   ├── class LazySequence(Sequence)
│   ├── class LazyIterator
│   ├── def filelinegenerator(...)
│   └── def pipeline(...)
│
├── examples/
│   ├── examplebasiciteration.py
│   ├── example_slicing.py
│   ├── example_pipeline.py
│   └── examplefilepipeline.py
│
└── bitacoras/
    ├── bitacora_iteradores.md
    ├── bitacora_protocolos.md
    └── bitacora_pipeline.md
`

---

🧠 Criterios de éxito

Tu solución debe:

- Pasar isinstance(obj, Sequence) == True.  
- Permitir:  
  `python
  seq = LazySequence([1,2,3,4,5])
  seq[1:4]        # slicing real
  seq[-1]         # índice negativo
  for x in seq:   # iterador interno
      ...
  `
- Integrarse en pipelines como:  
  `python
  pipeline = chain(
      filterfalse(lambda x: x < 0, seq),
      islice(seq, 10, 20),
      mycustomgenerator(seq)
  )
  `
- Procesar archivos sin cargarlos completos:  
  `python
  for line in filelinegenerator("data.txt"):
      ...
  `

---

Si quieres, puedo generar la versión final del enunciado en PDF, o puedo ayudarte a diseñar la arquitectura del código, o incluso escribir el esqueleto completo del proyecto. ¿Quieres que avancemos hacia el diseño del código o prefieres primero las bitácoras conceptuales?

"""




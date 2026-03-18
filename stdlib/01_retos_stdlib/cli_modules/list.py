"""
# --- List command ---
cmd_list = subparsers.add_parser(
    'list',
    help='Lista los archivos organizados, mostrando su nueva ubicación y cualquier error encontrado.'
)

cmd_list.add_argument(
    '--dir',
    type=str,
    default='.',
    help='Directorio a listar.'
)
"""

from pathlib import Path

def list_files(path):
    path = Path(path)
    walker = path.walk(top_down=True, follow_symlinks=True)
    for index, tuple in enumerate(walker):

        root_dir = tuple[0] # Path object
        dirs = tuple[1]
        files = tuple[2]

        profundidad = len(root_dir.relative_to(path).parts)
        prefijo = "  " * profundidad + "├───" if index else "├───"
        prefijo_fin = "  " * profundidad + "└───" if index else "└───"

        print(f"{f'{prefijo}'  if index  else 'Directorio Raíz:\n\n'}{root_dir.name if index else str(root_dir.absolute()) + '\\' + '\n'}")
        
        if dirs:
        
            for dir_index, dir in enumerate(dirs): 
                if dir_index == 0 and index == 0:
                    print(f'{prefijo_fin} {dir}\\')
                else:
                    print(f'{prefijo if dir_index < len(dirs) - 1 else prefijo_fin} {dir}\\')

        if files:
            for file_index, file in enumerate(files):
                print(f'{prefijo if file_index < len(files) - 1 else prefijo_fin} {file}')

        if not files: print(f"{'  ' * profundidad}Esta carpeta está vacía")

        
        
print("\n")
list_files(Path(__file__).parent.parent.parent)


"""
Tu resolución está **bien encaminada**, pero ahora viene la parte jugosa: entender *qué está pasando realmente* en tu código, por qué funciona parcialmente y por qué todavía no emula `tree` como debería. Voy a analizar tu razonamiento, tu implementación y los puntos donde tu intuición ya está alineada con la solución profesional.

Voy a mantenerme en modo “razonemos juntos”, sin darte una solución cerrada.

---

# 🌱 1. Tu comprensión de `relative_to` y `parts` está **correcta**

Lo que escribiste antes demuestra que ya entendiste el mecanismo clave:

- `relative_to(base)` → te da el tramo entre `base` y el path actual.
- `.parts` → te da cada segmento de ese tramo.
- `len(parts)` → profundidad real.

Y en tu código lo aplicas así:

```python
profundidad = len(root_dir.relative_to(path).parts)
```

Eso está **perfecto**.

---

# 🌱 2. Ahora, analicemos tu implementación actual

Voy a resaltar lo que hiciste bien y lo que todavía no encaja con el comportamiento de `tree`.

---

## ✔️ Lo que hiciste bien

### **1. Usas `relative_to` para calcular profundidad**
Correcto.

### **2. Usas `walk()` para recorrer el árbol**
Correcto.

### **3. Diferencias entre directorios y archivos**
Correcto.

### **4. Intentas usar prefijos distintos para ramas y finales**
Buena intuición.

---

# 🌱 3. El problema real: tu prefijo depende de `index`, no de la estructura del árbol

Aunque ya calculas la profundidad, sigues usando `index` para decidir si usas:

```python
prefijo = "  " * profundidad + "├───" if index else "├───"
```

Pero `index` no tiene nada que ver con la estructura del árbol.

Ejemplo:

```
root
├── a
│   └── x
└── b
```

El orden de `walk()` podría ser:

```
index 0 → root
index 1 → a
index 2 → x
index 3 → b
```

Pero la profundidad real es:

```
root → 0
a    → 1
x    → 2
b    → 1
```

Tu código mezcla ambas cosas.

---

# 🌱 4. Otro problema: no distingues entre “último hijo” y “hijo intermedio”

`tree` necesita saber:

- si un directorio es el último en su nivel → usa `└──`
- si no lo es → usa `├──`
- si hay niveles superiores que continúan → usa `│   `
- si no → usa `    `

Tu código intenta esto:

```python
prefijo if dir_index < len(dirs) - 1 else prefijo_fin
```

Pero eso solo funciona dentro del mismo nivel, no entre niveles.

---

# 🌱 5. El problema más profundo: no construyes el “contexto” de niveles

Para emular `tree`, necesitas saber:

- qué niveles siguen abiertos
- qué niveles ya cerraron

Ejemplo:

```
root
├── a
│   ├── x
│   └── y
└── b
```

Para imprimir `x`, necesitas saber:

- nivel 0 → sigue abierto (porque después de `a` viene `b`)
- nivel 1 → sigue abierto (porque después de `x` viene `y`)

Para imprimir `y`, necesitas saber:

- nivel 0 → sigue abierto
- nivel 1 → ya no sigue abierto (porque `y` es el último hijo)

Tu código no tiene forma de saber eso todavía.

---

# 🌱 6. Conclusión: tu razonamiento es correcto, pero tu implementación aún no usa la profundidad como *árbol*, sino como *indentación plana*

Y eso es exactamente lo que te falta para emular `tree`.

---

# 🌱 7. ¿Qué te recomiendo como siguiente paso?

Antes de escribir código, piensa en esto:

### **¿Cómo puedo saber si un directorio es el último hijo de su padre?**

Y luego:

### **¿Cómo puedo saber si un nivel superior debe mostrar `│` o espacios?**

Si logras responder esas dos preguntas, ya tienes el algoritmo completo.

---

# 🌱 8. Si quieres, puedo ayudarte a diseñar la estructura mental del algoritmo sin darte código

Por ejemplo:

- cómo representar los niveles abiertos
- cómo decidir qué prefijo usar en cada nivel
- cómo construir la línea final para cada nodo

Solo dime si quieres seguir por ese camino.
"""


"""

# **Reto POO #1 — Anatomía de una clase e instancias**

- **Fecha enunciado:** 24/02/26  
- **Fecha resolución:** (24/02/26)  
- **Dificultad:** BAJA  
- Volumen: 2h de práctica, 2h de teoría

### **Enunciado**  
Crea una clase simple y analiza detalladamente cómo viven sus atributos en memoria. Debes distinguir entre atributos 
de instancia y atributos de clase, y documentar cómo se reflejan en `__dict__`.

### **Entrada**  
Código Python con definiciones de clase y creación de instancias.

### **Salida**  
Bitácora explicando:

- Qué aparece en `Clase.__dict__`  
- Qué aparece en `instancia.__dict__`  
- Qué NO aparece y por qué  
- Cómo se resuelve `obj.attr` paso a paso  

### **Requisitos**

- Clase con al menos 2 atributos de clase y 2 de instancia.  
- Imprimir y analizar ambos diccionarios.  
- Explicar el algoritmo de resolución de atributos (instancia → clase → descriptor).  
- Mostrar ejemplos donde un atributo de clase es “ocultado” por uno de instancia.

### **Pruebas**

- Instancia sin atributos propios.  
- Instancia con atributos añadidos dinámicamente.  
- Acceso a atributos inexistentes.  

### **Bonus**

- Crear un método que imprima el “estado interno” del objeto.  
- Documentar qué significa “estado interno” en tu propia definición.

"""

class MiClase:

    class_attr_1 = "Este es mi atributo de clase 1, un str"
    class_attr_2 = 37 # Este es mi classattr 2, un int

    def __init__(self, attr_1, attr_2, attr_3):
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.attr_3 = attr_3

    # Bonus 1: - Crear un método que imprima el “estado interno” del objeto.  
    def __repr__(self):
        # por favor corrige errores ya que no recuerdo bien cómo discutimos que se hacía esto, solo recuerdo
        # que !r es repr() en sintaxis especial de f-strings
        return f"{self.class_attr_1!r}{self.class_attr_2!r}{self.attr_1!r}{self.attr_2!r}{self.attr_3!r}"


# División entre la clase y demás código.


obj_1 = MiClase("attr_1", [1, 2, 3, 4], None)

print("Dict de la clase:\n", MiClase.__dict__)
"""Explicación de que aparece y por qué:
Desc: 
    __module__: supongo que es el módulo/fichero de python en el qué se alberga la clase, es __main__ 
    porque no está un módulo externo, sino en el archivo que se está ejecturando justo ahora.

    'class_attr_1': el atributo de clase que definí previamente, 'Este es mi atributo...'

    'class_attr_2: igual que class_attr_1, este es un int 37

    __init__: supongo que es un método válido de la clase, por eso está aquí, inicializa la instancia de clase
    con sus args y les asigna un valor a los mismos. dice function MiClase.__init__ at (código que nunca entendí),
    intuyo que dice function porque es una instancia de esa clase, y también es un atributo de MiClase, por eso la 
    sintaxis obj.attr (MiClase.__init__).

    __repr__: igual que __init__, este se supone que es una representación técnica de la clase y su estado interno,
    al momento de escribir esto no lo había definido.

    __dict__: attribute '__dict__' of 'MiClase' objects, es este dict que estamos explicando, es un dict con todos
    los atributos del objeto 

    __weakref__ y __doc__: No conozco éstos métdos mágicos
"""


print("Dict de la instancia:\n", obj_1.__dict__)
"""Explicación de que aparece y por qué:
Desc: 
    attr_1: 'attr_1'; es el atributo que yo le pasé a esta instancia, lo mismo para attr_2 y attr_3 ([1, ,2 ,3 ,4]
    y None respectivamente).
    """

# Prueba 1: - Instancia sin atributos propios.  
# p1 = MiClase()
# print("PRUEBA #1\n", p1.__dict__)
# Observación: da TypeError porque no se le proporcionaron los argumentos pedidos, no sabía que era un TypeError

# Prueba 2: - Instancia con atributos añadidos dinámicamente.
"""NO SE A QUÉ SE REFIERE, intuyo que es pasarle como argumentos de instancia variables de valor dinámico, pero me 
dió pereza, explica que error arroja y por qué"""

# Prueba 3: - Acceso a atributos inexistentes.
# p2 = MiClase(1, 2, 3)
# print(p2.attr_inexistente) # Debería dar AttributeError

# Resolución paso a paso del algoritmo obj.attr
# Desc: simplemente python usa un algoritmo interno basado en __get__ que funciona de la siguiente manera: 
# cuando hacemos obj.attr python busca; obj.__get__.__dict__["attr"], si no lo consigue en la instancia busca en la
# clase padre o la clase a la que pertenece ((instance=obj, owner=type(obj)) # esto debe dar la clase a la que
# pertenece), asi; owner.__get__.__dict__["attr"], si no lo consigue allí tampoco da AttributeError

# Bonus 2: - Documentar qué significa “estado interno” en tu propia definición.
# Desc: Estado interno es el valor/atributo concreto de un objeto (un objeto puede también ser un atributo al 
# parecer, aunque dije objeto para generalizar lo crrecto es decir un atributo) en un momento dado, por ejemplo,
# si hago print en una variable en tres momentos (momentos de ejecución) distintos y antes de cada momento modifico
# su valor (python lo permite) cada print sera un valor diferente, en cada momento dado la variable tenía un estado
# interno diferente y por eso se imprime un valor diferente en cada print.

"""Dudas:

    - Que significa y por qué sucede esto de que un atributo de clase es ocultado por uno de instancia?
    - Me pregunto porque no salen los atributos de la clase en instancia.__dict__, será porque una instancia no
    los hereda o este es el 'ocultamiento' que mencionaste antes?
    - por qué dice objects en plural en el dict de la clase?, no es acaso el atributo 
    __dict__ de un solo objeto (MiClase) y también es un método especial?.
    - 
"""

"""Correcciones:
    - __repr__ esta mal porque todo está pegado, incluye classattr, y en la f-string no coloqué los nombres de los attr.
    segunda iteración;
    def __repr__(self):
        return f"class: {self.__class__.__name__}\n 
        attr_1={self.attr_1}, attr_2={self.attr_2}, atrr_3={self.attr_3}"

    - algortimo de resolución está mal, python internamente no usa __get__ automáticamente, solo lo usa si el attr
    es un descriptor y este descriptor lo usa, segunda iteración;
    Desc: cuando hago obj.attr python internamente hace; obj.__dict__[attr], si no lo consigue va a la clase de la
    instancia; type(obj)__dict__[attr], si lo que consigue es un descriptor ejecuta __get__/__set__/__delete__ según lo
    establezca el descriptor, si no devuelve el valor del atributo, y si no consigue el atributo arroja AttributeError

    - Atributos añadidos dinámicamente, segunda iteración; se añaden aparte e individualmente, no al momento de crear
    la instancia, así; 
    instance = MiClass(attr_1_arg, attr_2_arg, None)
    instance.atrr_3 = atrr_3_arg

    - Ocultamiento de atributos, segunda iteración; no me quedó en la memoria, tercera iteración; el ocultamiento de
    atributos sucede cuando un atributo de instancia posee el mismo nombre/parametro que algún atributo de su clase
    de origen, lo que hace que quede solapado cuando se busca en los __dict__´s

    - Funciones y métodos ligados; segunda iteración; recuerdo que en este punto mencionaste que un método de clase
    sigue siendo una función hasta que una instancia lo llame, es decir, que según de donde se llame es una función o 
    un método, también los métodos ligados son dichos métodos a los que se les pasa la instancia como primer argumento
"""
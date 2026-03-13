"""
Perfecto, Moisés. Aquí tienes **el Reto POO #2**, listo para que lo copies en tu bitácora y empieces la práctica.  
Lo redacto exactamente en el **formato profesional** que estás usando, con claridad, precisión y sin mezclar teoría adicional.

---

# **Reto POO #2 — Encapsulación y control del estado**

- **Fecha enunciado:** 25/02/26  
- **Fecha resolución:** (por completar)  
- **Dificultad:** MEDIA  

---

## **Enunciado**  
Implementa una clase `CuentaBancaria` que mantenga un saldo siempre válido (nunca negativo).  
El saldo debe ser accesible como atributo público (`obj.saldo`), pero su almacenamiento y validación deben 
estar completamente encapsulados mediante `@property`.

La clase debe permitir depósitos y retiros, manteniendo el invariante fundamental:

> **El saldo nunca puede ser negativo.**

---

## **Entrada**  
Código Python que defina la clase y cree varias instancias para pruebas.

---

## **Salida**  
Bitácora explicando:

- Cómo encapsulaste el estado interno.  

Desc: Se almacena únicamente la variable _saldo por cada instancia, ésta variable contiene el saldo actual de cada
una y se accede mediante el atributo self.saldo (descriptor que controla el comportamiento de asignación y getting)
que es el que modifica _saldo

- Por qué el atributo real se llama `_saldo`.

Desc: Lo hicimos así para dar a entender que es un atributo interno, el atributo self.saldo realmente es el descriptor
que controla el acceso y asignación de este último, esto hace en cierta manera las instancias más robustas siempre
y cuando la clase padre sea robusta, ya que es esta la que se encarga del comportamiento de los descriptores

- Cómo funciona el getter y el setter. 

Desc: el getter retorna el valor de _saldo cada vez que se llama al atributo self.saldo, el setter asigna el argumento
dado a _saldo o lanza ValueError si este argumento es menor que cero

- Cómo se mantiene el invariante saldo ≥ 0.

Desc: cada vez que se le asigna un valor a self.saldo ese valor pasa por el setter que valida que el argumento no sea
menor que cero

- Qué ocurre cuando se intenta violar el invariante.  

Desc: no lo sé, supongo que lanza el ValueError, pero me pregunto que pasa si intento self._saldo = valor, supongo
que si se asignaría el nuevo valor rompiendo el código, me vendría bien una explicación

---

## **Requisitos**

- Atributo privado `_saldo` (no debe existir `saldo` en `self.__dict__`).  
- Getter `saldo` que devuelva `_saldo`.  
- Setter `saldo` que valide:  
  - si el valor es negativo → `ValueError`.  
- Métodos:  
  - `depositar(monto)`  
  - `retirar(monto)`  
  Ambos deben usar el setter para actualizar el saldo.  
- `__repr__` profesional (una sola línea, técnica, clara).  

---


---

## **Bonus**

- Añadir un atributo privado `_historial` que registre cada operación.  
- Crear una property `historial` de solo lectura.  
- Registrar:  
  - depósitos,  
  - retiros,  
  - errores (opcional).  

---

## **Notas de calidad**

- No uses `print` dentro de la clase (solo en pruebas).  
- No expongas `_saldo` directamente.  
- Usa el setter incluso dentro del constructor.  
- Mantén el invariante en TODO momento.  

---

Cuando termines, me envías:

- tu código,  
- tu bitácora,  
- y cualquier duda conceptual que surja durante la práctica.

Estoy listo para acompañarte en este Día 2.
"""

class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = 0
        self.saldo = saldo
        # Bonus:
        self._historial = list()
        self._mov_id = 0

    @property
    def historial(self):
        return self._historial
        
    @property
    def saldo(self):   
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def retirar(self, monto):
        
        if monto > self.saldo:
            raise ValueError("No dispones del saldo suficiente para realizar esta operación")
        if monto == 0:
            raise ValueError("Ingrese un monto")
        
        self.saldo -= monto
        self._mov_id += 1
        self._historial.append(f"MOV{self._mov_id} TIPO DE OPERACIÓN: RETIRO MONTO: {monto}")


    def depositar(self, monto):
      
        if monto == 0:
            raise ValueError("Ingrese un monto para depositar")
        
        self.saldo += monto
        self._mov_id += 1
        self._historial.append(f"MOV{self._mov_id} TIPO DE OPERACIÓN: DEPOSITO MONTO: {monto}")

    def __repr__(self):
        return (
            f"Clase: {self.__class__.__name__!r}\n"
            f"Attr: _saldo={self._saldo!r}"
        )
    

## **Pruebas**

# 1. Crear una cuenta con saldo inicial válido.  
cuenta_valida = CuentaBancaria(203)
print("\nReproduce\n",cuenta_valida.__repr__())

cuenta_valida.depositar(297)
assert cuenta_valida.saldo == 500

cuenta_valida.retirar(250)
assert cuenta_valida.saldo == 250

# 2. Intentar crear una cuenta con saldo negativo → debe fallar.  

# cuenta_invalida = CuentaBancaria(-1)
# esperado: ValueError, no se como expresarlo en código sencillo sin pytest
# obtenido: ValueError("El saldo no puede ser negativo")

# 3. Depositar valores válidos. Hecho en la prueba 1  
# 4. Retirar valores válidos. Hecho en la prueba 1

# 5. Intentar retirar más de lo disponible → debe fallar.

# cuenta_valida.retirar(300)
# esperado: ValueError, no se como expresarlo en código sencillo sin pytest
# obtenido: ValueError: No dispones del saldo suficiente para realizar esta operación

# 6. Verificar que `_saldo` aparece en `obj.__dict__` y `saldo` NO.  

print("\nDict de instancia\n")
print(cuenta_valida.__dict__)

print("\nDict de clase\n")
print(type(cuenta_valida).__dict__)


"""Preguntas:

    - si cuando no hay properties hay asginación con descriptores por defecto, cuales son éstos? debería conocerlos
    o debería posponer su estudio? acaso es __setattr__?
    
    - cada vez que hay asignación python relega la tarea al property que hice siempre que se trate de un atributo
    que hace referencia al property (instance.saldo)? ya que mi setter tiene un invariante por allí van a pasar
    cualquier asignación (incluso las de los métodos depositar/retirar)?
    
    - que flujo/resolución exacta siguen las líneas self.saldo += monto/self.saldo -= monto? intuyo que hacen algo
    así; self.saldo == descriptor ´n descriptor setter dice que mientras monto no sea cero se asigna el valor a
    _saldo ´n el valor a asignar es self.saldo +/- monto ´n self.saldo es un descritpor y llama al getter que devuelve
    _saldo como valor, monto es un int ´n self.saldo =_saldo - monto, donde self.saldo es el property que llama
    al setter y asigna ese valor a _saldo
    
    - si en el constructor solo inicializo saldo que será el property y _saldo que será el estado interno privvado,
    cada instancia tendrá unicamente el atributo _saldo ya que el atributo saldo que es un objeto solo se define
    en la clase, a las instancias se les hereda el acceso con la línea self.saldo = saldo, pero saldo no estará en
    la instancia y se buscará en la clase padre donde si está definido, cierto?"""

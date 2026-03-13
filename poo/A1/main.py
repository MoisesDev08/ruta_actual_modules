"""
# POO (retos A > D), huecos → stdlib → commonlib → arquitectura y estructura de proyectos + ecosistema profesional
#  → portafolio → propuestas
"""

# Bonus2
# Desc: no hay mucho relevante que decir aparte del orden y determinismo que trajo la implementación del C3
# eliminando bastantes problemas cuando se trata de herencia compleja/anidada (supongo que se puede decir anidada verdad?)
# Bonus1
class MixinDePractica:
    def __init__(self):
        # lo dejo vacío porque según entiendo los mixins solo añaden lógica complementaria, es decir que si no necesito
        # ningun attr para dicha logica no debo crearlo aquí, y de necesitarlo debería crearlo como privado, con name
        # mangling o controlar su acceso con descriptores
        pass

    def imprimir_mro(self):
        print(self.__class__.mro())
        pass # me quedé sin ideas para que no fuese trivial


class Dueño(MixinDePractica):

    def __init__(self):
        self.status = "Ownership"

    def saludar(self):
        return f"Hola, tengo responsabilidades en el área de {self.status}"
    
    def __repr__(self):
        return (
            f"class={self.__class__.__name__!r}, "
            f"args(self.status={self.status!r})"
        )

class Gerente(Dueño):

    def __init__(self):
        super().__init__()
        self.status = "Managment" # Según tengo entendido esto hace inútil el super() ya que si sobreescribe el attr
        # de modo que en la resolucion de attrs no busca en la clase padre xq ya lo encuentra en esta clase

    def saludar(self):
        return super().saludar() # quiero ver si esta herencia busca el attr self.status en la clase padre o en la hija
        # ya que las clases heredan acceso lógico y no los attrs, debería imprimir Managment porque python pasa el obj como
        # primer arg

    def __repr__(self):
        return super().__repr__()

class Administrador(Gerente, Dueño):
    def __init__(self):
        super().__init__()
        self.status = "Admin"
    
    def saludar(self):
        return super().saludar() # Debería retornar Admin, ya que en el saludar de su siguiente clase en el MRO (a donde apunta super)
        # es Gerente, y el saludar() de esa clase apunta al de la clase Dueño (no porque sea la sucesora de este, sino porque sigue el 
        # orden del MRO de la clase Administrador, que fué la que originó la llamada)

    def __repr__(self):
        return super().__repr__()

class Usuario(Administrador):
    
    def __init__(self):
        super().__init__()
        self.status = "User"
        pass

    def saludar(self):
        return super().saludar()
    
    def __repr__(self):
        return super().__repr__()
    
owner1 = Dueño()
manager1 = Gerente()
admin1 = Administrador()
user1 = Usuario()

print(owner1.imprimir_mro())
print(manager1.imprimir_mro())
print(admin1.imprimir_mro())
print(user1.imprimir_mro())

assert owner1.status == "Ownership"
assert manager1.status == "Managment"
assert admin1.status == "Admin"
assert user1.status == "User"

print(user1.saludar(), user1.__class__.mro())

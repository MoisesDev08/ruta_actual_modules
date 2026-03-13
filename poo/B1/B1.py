from abc import ABC, abstractmethod
from datetime import datetime

class SendError(Exception):
  def __init__(self, *args):
    super().__init__(*args)

class LoggingError(Exception):
  def __init__(self, *args):
    super().__init__(*args)

class NotifyError(Exception):
  def __init__(self, *args):
    super().__init__(*args)

class DestinationError(Exception):
  def __init__(self, *args):
    super().__init__(*args)
#  hay alguna forma de reemplazar todos los nombres de un atributo/variable desde su definicion con pocos clics en vs code sin necesidad de
#  modificar manualmente cada llamada que se le hace?


class Notificador(ABC):
  """Clase abstracta que define el contrato de la interfaz del notificador.
  El notificador se encarga de la lógica de negocio interna de envio y recepción de mensajes/notificaciones
  """

  @abstractmethod
  def enviar(self, mensaje, destinatario) -> str: # estado y datos para el log en string
    try:
      pass
    except Exception as e:
      print(e)
      raise SendError('Error de envío')
    

  @abstractmethod
  def validar_destinatario(self, destinatario) -> bool:
    pass

  def registrar_intento(self, mensaje, destinatario, exito) -> None:
    
    try:
      # escribe un log interno
      pass
    except Exception as e:
      print(e)
      raise LoggingError('Error de logging de intentos')

  def notificar(self, mensaje, destinatario):
    # método que válida, envía y registra, template method, hacerlo más elaborado que el resto
    """Notificar debe ser el método que llame a los demás metodos y que además tenga error handling"""
    try:
      if self.validar_destinatario():
        pass
        self.enviar()
        self.registrar_intento()
      else:
        raise DestinationError('Error de destinatario')

    except:
      # que cada clase reescriba a su necesidad y gusto este metodo plantilla y su error handling
      pass

class EmailFormatError(Exception):
  def __init__(self, *args):
    super().__init__(*args)

class NotificadorEmail(Notificador):
  """Clase encargada de la notificación exclusiva en cuanto a e-mails se refiere, encapsula la lógica de mensajería e historial de mensajes"""

  def __init__(self, usuario_nombre, usuario_email, id_usuario, notiyf_historial, mensaje, id_mensaje, destinatario_numero, destinatario_nombre):
    pass

  def enviar(self, mensaje, destinatario):
    """envía la notificación"""
    try:
      pass

    except:
      pass

  def validar_destinatario():
    pass


class PhoneNumberError(Exception):
  def __init__(self, *args):
    super().__init__(*args)
class NotificadorSMS(Notificador):
  """ Docs """
  # TODO...
  def __init__(self):
    super().__init__()
    pass

class NotificadorPush(Notificador):
  """ Docs """
  # TODO...
  pass


# Corrígeme si me equivoco pero creo que, terminando de completar todo lo que hice pass, tal vez usando algunas funciones recursivas internas y/o properties, y simulando un flujo de notificaciones, tal vez desde otro módulo que llame a este, usando importación e instanciación, ya cumpliría con el reto al 100%, cierto?
# Añadir tests aunque sean básicos, algunos errores personalizados que hereden de Exception, hacer parsing/validación en cada clase hija (tal vez también se le pueda aplicar template method pattern)
from abc import ABC, abstractmethod
from datetime import datetime
import re


class SendingError(Exception):
    pass


class LoggingError(Exception):
    pass


class NotifyError(Exception):
    pass


class DestinationError(Exception):
    pass


class EmailFormatError(Exception):
    pass


class PhoneNumberError(Exception):
    pass


class PushDestinationError(Exception):
    pass


class Notificador(ABC):
    """
    Clase abstracta que define el contrato de la interfaz del notificador.
    El notificador se encarga de la lógica de negocio interna de envío y
    registro de mensajes/notificaciones.
    """

    def __init__(self) -> None:
        # Historial común para todos los notificadores
        self._historial: list[dict] = []

    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> str:
        """Envía la notificación y devuelve un string con el estado."""
        pass

    @abstractmethod
    def validar_destinatario(self, destinatario: str) -> bool:
        """Valida el destinatario según el tipo de notificador."""
        pass

    def registrar_intento(
        self,
        mensaje: str,
        destinatario: str,
        exito: bool,
        error: str | None = None,
    ) -> None:
        """Registra el intento de envío en un historial interno."""
        try:
            entry = {
                "timestamp": datetime.now().isoformat(),
                "canal": self.__class__.__name__,
                "destinatario": destinatario,
                "mensaje": mensaje[:80],
                "exito": exito,
                "error": error,
            }
            self._historial.append(entry)
        except Exception as e:
            # Si incluso el logging falla, lo elevamos explícitamente
            raise LoggingError(f"Error al registrar intento: {e}") from e

    def notificar(self, mensaje: str, destinatario: str) -> str:
        """
        Template Method:
        - valida destinatario
        - intenta enviar
        - registra intento
        - maneja errores
        """
        try:
            if not self.validar_destinatario(destinatario):
                self.registrar_intento(
                    mensaje,
                    destinatario,
                    exito=False,
                    error="Destinatario inválido",
                )
                raise DestinationError("Destinatario inválido")

            resultado = self.enviar(mensaje, destinatario)
            self.registrar_intento(
                mensaje,
                destinatario,
                exito=True,
                error=None,
            )
            return resultado

        except Exception as e:
            # Cualquier error durante validación o envío se registra aquí
            self.registrar_intento(
                mensaje,
                destinatario,
                exito=False,
                error=str(e),
            )
            # Podrías wrappear en NotifyError si quisieras unificar
            raise NotifyError(f"Error en notificación: {e}") from e

    @property
    def historial(self) -> list[dict]:
        return self._historial


class NotificadorEmail(Notificador):
    """
    Notificador específico para e-mails.
    Encapsula la lógica de validación y envío de correos.
    """

    EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    def __init__(self, remitente_email: str) -> None:
        super().__init__()
        self.remitente_email = remitente_email

    def _parser_de_destinatario(self, destinatario: str) -> str:
        """
        Valida el formato del destinatario (e-mail) y lo normaliza.
        Lanza EmailFormatError si es inválido.
        """
        if not isinstance(destinatario, str) or not destinatario.strip():
            raise EmailFormatError(
                "Destinatario debe ser una cadena no vacía."
            )

        email_normalizado = destinatario.strip().lower()

        if not re.match(self.EMAIL_PATTERN, email_normalizado):
            raise EmailFormatError(f"Formato de e-mail inválido: {destinatario}")

        return email_normalizado

    def validar_destinatario(self, destinatario: str) -> bool:
        # Si el parser no lanza error, el destinatario es válido
        try:
            self._parser_de_destinatario(destinatario)
            return True
        except EmailFormatError:
            return False

    def enviar(self, mensaje: str, destinatario: str) -> str:
        """
        Simulación de envío de correo electrónico.
        En un caso real, aquí iría la integración con smtplib u otro servicio.
        """
        try:
            destinatario_normalizado = self._parser_de_destinatario(destinatario)
            # Simulación de envío
            print(f"[EMAIL] Enviando desde {self.remitente_email} a {destinatario_normalizado}")
            print(f"Mensaje:\n{mensaje}")
            return f"Email enviado a {destinatario_normalizado}"
        except Exception as e:
            raise SendingError(f"Error al enviar e-mail: {e}") from e


class NotificadorSMS(Notificador):
    """
    Notificador específico para SMS.
    """

    PHONE_PATTERN = r"^\d{10,15}$"

    def __init__(self, remitente_numero: str) -> None:
        super().__init__()
        self.remitente_numero = remitente_numero

    def validar_destinatario(self, destinatario: str) -> bool:
        if not isinstance(destinatario, str) or not destinatario.strip():
            return False
        if not re.match(self.PHONE_PATTERN, destinatario.strip()):
            return False
        return True

    def enviar(self, mensaje: str, destinatario: str) -> str:
        try:
            if not self.validar_destinatario(destinatario):
                raise PhoneNumberError(f"Número inválido: {destinatario}")
            print(f"[SMS] Enviando desde {self.remitente_numero} a {destinatario}")
            print(f"Mensaje:\n{mensaje}")
            return f"SMS enviado a {destinatario}"
        except Exception as e:
            raise SendingError(f"Error al enviar SMS: {e}") from e


class NotificadorPush(Notificador):
    """
    Notificador específico para notificaciones push.
    """

    def __init__(self, app_id: str) -> None:
        super().__init__()
        self.app_id = app_id

    def validar_destinatario(self, destinatario: str) -> bool:
        # Para este ejemplo, consideramos válido cualquier ID no vacío
        return isinstance(destinatario, str) and bool(destinatario.strip())

    def enviar(self, mensaje: str, destinatario: str) -> str:
        try:
            if not self.validar_destinatario(destinatario):
                raise PushDestinationError(f"ID de dispositivo inválido: {destinatario}")
            print(f"[PUSH] Enviando desde app {self.app_id} a device {destinatario}")
            print(f"Mensaje:\n{mensaje}")
            return f"Push enviado a dispositivo {destinatario}"
        except Exception as e:
            raise SendingError(f"Error al enviar push: {e}") from e

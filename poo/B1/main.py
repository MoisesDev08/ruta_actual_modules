# Ejemplo de uso desde otro módulo (simulación rápida):
from B1.main import NotificadorEmail, NotificadorPush, NotificadorSMS


if __name__ == "__main__":
    email_notifier = NotificadorEmail(remitente_email="no-reply@miapp.com")
    sms_notifier = NotificadorSMS(remitente_numero="04141234567")
    push_notifier = NotificadorPush(app_id="mi_app_push")

    email_notifier.notificar("Hola por correo", "usuario@example.com")
    sms_notifier.notificar("Hola por SMS", "04141234567")
    push_notifier.notificar("Hola por push", "device_123")

    print("\nHistorial EMAIL:")
    for h in email_notifier.historial:
        print(h)
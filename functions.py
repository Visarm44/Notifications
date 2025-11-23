from plyer import notification

def invia_notifica(title, description, icon):
    notification.notify(
        title=title,
        message=description,
        app_icon=icon,
        # app_name="Il Mio Notifier", # Opzionale
        timeout=10 # La notifica resta per 10 secondi
    )

from engine.events.dto_events import DTOEvents


class _ManagerEvents:
    def __init__(self):
        self.list_subscribers = []
        self.function_start_backend = None

    # --- Métodos para el Backend ---
    def activate_backend(self) -> None:
        if self.function_start_backend:
            self.function_start_backend()

    # --- Métodos para la Interfaz (UI) ---
    def add_suscribers(self, subscriber) -> None:
        self.list_subscribers.append(subscriber)

    def send_events(self, data: DTOEvents):
        if not self.list_subscribers:
            return

        for subscriber in self.list_subscribers:
            subscriber(data)


# Para la comunicacion entre modulos
manager_events = _ManagerEvents()

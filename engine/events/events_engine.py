import threading

# ? Se puede hacer esto gracias al __init__ de actions
from engine.events.actions import EventBasic, EventHalf, EventHard
from engine.events.dto_events import DTOEvents


class EventsEngine:
    def __init__(self, manager_events):
        # self.manager_events = manager_events
        self.progress_hackback = 0
        self.manager_events = manager_events
        self.data: DTOEvents

    def event_randomice(self, progress) -> None:

        if progress >= 10 and progress < 30:
            return
        elif progress >= 30 and progress < 60:
            return
        elif progress >= 60 and progress <= 100:
            return

        return

    def iniciar_simulacion(self):
        self.progress_hackback = 0
        self.tick_simulacion()

    def tick_simulacion(self):
        # Este método se ejecuta en bucle haciendo avanzar el juego
        response = None

        if self.progress_hackback < 100:
            self.progress_hackback += 1

            # Eventos "basicos"
            if self.progress_hackback > 0 and self.progress_hackback <= 30:
                response = EventBasic.event_basic()

            # Eventos "medios"
            elif self.progress_hackback > 30 and self.progress_hackback <= 70:
                response = EventHalf.event_mid()

            # Eventos "dificiles"
            elif self.progress_hackback > 70 and self.progress_hackback <= 100:
                response = EventHard.event_hard()

        data = DTOEvents(
            f"{response} {self.progress_hackback}%",
            self.progress_hackback,
        )

        if data is not None:
            # Envia los datos al gestor
            self.manager_events.send_events(data)

        # Nota: Es importante que no se cierre la funcion con () porque entonces se ejecuta
        threading.Timer(1.0, self.tick_simulacion).start()

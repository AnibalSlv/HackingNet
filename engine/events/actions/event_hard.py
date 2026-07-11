from engine.events.dto_events import DTOEvents


class EventHard:
    # Se preaparan los datos para el envio

    progress_x = "funciona"

    @classmethod
    def event_hard(cls):
        data = DTOEvents(
            event=f"Hackeando servidores... {cls.progress_x}%",
            progress=300,
        )
        return data

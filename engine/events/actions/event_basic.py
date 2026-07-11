from engine.events.dto_events import DTOEvents


class EventBasic:
    # Se preaparan los datos para el envio

    progress_x = "funciona"

    @classmethod
    def event_basic(cls):
        data = DTOEvents(
            event=f"Hackeando servidores... {cls.progress_x}%",
            progress=100,
        )
        return data

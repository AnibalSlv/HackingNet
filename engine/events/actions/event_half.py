from engine.events.dto_events import DTOEvents


class EventHalf:
    # Se preaparan los datos para el envio

    progress_x = "funciona"

    @classmethod
    def event_mid(cls):
        data = DTOEvents(
            event=f"Hackeando servidores... {cls.progress_x}%",
            progress=200,
        )
        return data

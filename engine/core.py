from engine.player import Player

# El core vendria siendo como el "motor" del juego aqui adentro tendra todas sus leyes
# toda la logica como tal pues
class Core: 
    def __init__(self):
        self.player = Player() # Aqui supongo que lo sabes como tal xd agarramos la clase player y
        # la guardamos para poder modificarla

    def buy_item(self) -> None:
        self.player.money -= 10  # Esto modifica el dinero del player
        # .money es un atributo de la clase player 

        #ya xd o bueno esto que es lo viejo
        #entendible xd
        # si tienes dudas

#! ESTA PARTE LA ACABO DE COPIAR ES POR SI SE ME OLVIDA Y NO LO BORRO
class Player: # este es el jugador 
    def __init__(self):
        self.name = "Anibal" # el jugador tiene un nombre
        self.money = 100 # dinero
        self.prestige = 1 # puntos de prestigio algo asi como reconocimiento  
        self.tools = ["pinch.exe", "troyano.exe"] # herramientas para usar en el game
        self.ip_current = "localHost" # su ip actual en donde esta conectado (no se en que nos sirva xd)
        # aqui dentro de player estara todo su "esqueleto"
        #como tal es la info que forma al jugardor como tal xd?
        # yeah
        #se le define los atributos y estos pues se usa a su favor el .tools es la lista que
        #tiene adentro los items xd que actualmente tiene o ha comprado
        #correcion: no se usa a su favot como tal, son atributos que lo definen, estos se pueden cambiar
        # y si con lo de los tools, lo que pasa es que lo hice estatico en el momento para salir de eso
        # pero deberia de ser una lista vacia o 'items' que tenga de primeras al iniciar
        #xd pues deberia ser asi osea item basicos y mediocres para iniciar la run como tal
        # yeah

        #bueno mas dudas con esto xd ?
        #nada blo todo claro :3
        # ok xd te dejo esto o no se para que  
        #dejalo xd ya si luego lo hago con capturas un tipo de documentacion
        # ok, no mas recuerda borrarlo antes de subirlo
        # que otra parte te cuesta ?
        #pues vamos viendo cada archivo si claro puedes quitando los mios xd
        # esto esta en una rama git ?
        #nop si no estoy mal xd

        # ok xd vamos a main
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, TabbedContent, TabPane, Static
from render.render_red import RenderRed
from render.render_profile import RenderProfile
from render.game.render_game import RenderGame

from commands.global_commands import command_global

from engine.core import Core

class AppNavegacionPorTexto(App): # el (app) es algo de la libreria para que funcione
    # aqui se medio complica un poco no mas
    # es mas engorroso en el actualizado que tengo 

    # Añadimos un poco de margen para que la interfaz respire visualmente
    CSS = """
    TabbedContent ContentTabs {
        display: none;
    }
    Input {
        margin: 1 2;
    }
    TabbedContent {
        margin: 1 2;
    }
    """

    #veras este CSS = es como un archivo .tcss pero hardcodeado osea directo en el codigo
    #es como poner un <style > en el html 

    def __init__(self):
        super().__init__() # este super().__init__() es de la libreria para heredar cosas (no lo tengo muy claro como tal)
        self.game = Core() # aqui recibimos el Core() para poder utilizarlo, porque recordemos que main:
        """x
            - SIRVE UNICAMENTE PARA LA COMUNICACION DEL PROGRAMA EN TERMINOS GLOBALES
            - no deberia de contener frontend a no ser que de ese elemento sea utilizado en todo el programa
            - igual con el backend 

            - esto tatuatelo si es necesario
            %porque es tan importante si se puede saber? xd


            - es facil, con que archivo ejecutas el proyecto xd ?
            %con el main uwu

            - exacto, si ejecutas el main y el main no tiene comunicacion con algun archivo que pasa?
            - por ejemplo con el archivo render_red()
            %tengo entendido que si no hay comunicacion de los archivos,con el main el main es solo un xd archivo mas
            %ya que este sirve como comunicacion con los otros supo
            %Bueno tiene sentido al fin y al cabo sin este xd no haria mucho mayormente el main es para el orden
            - yeah, bueno vas entendiendo la idea xd, el main por lo general deberia de mantenerse limpio
            - y como mencione anteriormente solo se utiliza si se tienen que manejar cosas de manera global en el programa
            - pero tambien depende de ciertas cosas pq 
            - ahorita estamos utilizando el main para tener comunicacion con los comandos 'cd, ls, etc' y para los render
            - pero en otros framework o librerias, hay archivos que ya manejan esas cosas sin tener que tocar el main para los render
            - por ejemplo, y asi
            - es medio complicado de explicar o bueno se me medio dificulta, pero lo vas entendiendo con la practica

        """
    def compose(self) -> ComposeResult: # esta funcion es de textual, permite renderizar widgets
        yield Header() # bueno xd no hay mucho que explicar aqui carga el header 
                
        # El contenedor de pestañas con sus IDs definidos
        #! INITIAL ABRE POR DEFECTO LA PESTANA CON ESA ID

        # esto es un manejador de vistas de textual por asi decirlo
        # el determina que se ve y que no, todo con el metodo .activate
        # este si es true activa xd las pestana por ponerle un nombre
        with TabbedContent(initial="profile", id="windows"): 
            yield RenderRed()
            # aqui si te fijas estamos pasando el player al profile
            # esto permite renderizar sus atributos
            # igual no te fijes mucho en el "back" porque la mayoria lo cambie 
            yield RenderProfile(self.game.player) 
            yield RenderGame()
                
        yield Footer()
        
    """
        - alguna duda xd ?
        %mayor mente mi duda es el yield xd es como algo?

        - toma el yield como: muestrame [elemento]
        - sirve solo para renderizar (o hasta donde recuerdo y se)
        - piensalo asi:
        - el yield es algo de textual, permite mostrar elementos en su interfaz 
        %tambien puede ser tomado como un print? xd

        - como a un print? que le colocas algo en los () y lo muestra ?
        %entiendo como que es un print pero muestra o bueno renderiza lo que le pides no creo 
        %que puedas poner print RenderGame()
        - en realidad si no mal recuerdo pero no confies mucho creo que si puedes
        - pero solamente si la funcion devuelve algo como tal, pq no te va a mostrar todo los comandos xd
        - ve para explicarte mejor esto vamos a render_profile un momento
    """

    # Evento que se dispara al presionar Enter en el Input
    
    #- este lo explico con comentarios a si que aqui dime que no entiendes o desde donde xd
    #dale cuando haya dudas xd pues usamos las comillas
    #- osea dime desde donde de esta funcion no entiendes como tal xd
    #ah pense que iriamos xd explicando cada una viendo la complejidad
    #- a bueno dale 

    #- Interrumpeme si no entiendes algo asi voy un poco mas rapido

    # on_input_submitted(self, event: Input.submitted) es una funcion de textual de nuevo
    # este permite obtener un evento que venga del usuario, sabes que son eventos no ?
    #% los eventos no son los que da el usuario a hacer algun opcion como enter y etc?
    # - si, existe el evento click, touch (en pantallas tactil), hover, focus, etc
    # - en una guia de eventos en JS te va a mostrar a detalles todos xd es por si quieres
    # - profundizar en eventos pero eso es para web pues, es un ejemplo no mas 

    # el parametro event permite que la funcion identifique el evento que se va a hacer para que la 
    # funcion se ejecute, en este caso nosotro pasamos como tipo de dato (por los dos puntos :)
    # Input.submitted, este evento se ejecuta unicamente cuando el usuario le da enter al input
    #%ya veo lo cambia todo y habra tambien opciones o bueno evento que auto destruya el programa como tal?
    #- pues no se me ocurre un evento que autodestruya el programa, osea, alt + F4 supongo xd 

    def on_input_submitted(self, event: Input.Submitted) -> None:

        # aqui estamos accediento al evento y al valor que contiene el evento
        # recordemos que el usuario le dio enter al input
        # el valor que tenia el input en el momento es decir lo que escribio el usuario
        # es el valor que conteine event ahora
        # y lo siguiente es lo tipico .strip().lower() para limpiar los datos 
        # el .split() es para separa el texto introducido por el usuario en un arreglo es decir:
        # si el usuairo escribio:
        # hola mundo
        # el split lo convierte en 
        # ["hola", "mundo"]
        
        #%a lo que te refieres con limpiar datos es? xd o pq doble limpiar datos 
        #- ve, si el usaurio escribiera:
        #-     hOlA muNdo                          
        #- y el programa valida si el usaurio escribio "hola mundo"
        #- que va a pasar al recirbir estos datos del usaurio?
        # digamos que tenermos:
        """
            input_user = "   HoLa mUndo             "

            if input_user == "hola mundo":
                print("si")
            else:
                print("no es un hola mundo")
        """
        #%ya veo xd ya le entendi grax 
        #- el .lower() convierte todo a minusculas
        #- el .strip() elimina los espacios en blanco del inicio y final de la cadena de caracteres
        #- si juntas todos entonces hacen lo mismo en una linea xd
        #% okey listo la aclaracion
        #- es por si acaso no mas xd
        inputUser = event.value.strip().lower().split()

        # 2. Obtenemos el widget de las pestañas
        
        # sabes usar JS ? 
        # dime que si porque te gusta el front
        # me dices que no y te cambio de area 
        #% aja suelo usar el JS pq?

        # Bueno el atributo de clase: self.query_one() funciona exactemente igual que el de JS
        # permite buscar un elemento por su id o clase (osea el # y .)

        # el TabbedContent si no mal recuerdo decia: el primer elemento TabbedContect con la id #windows
        # esto permite obtener ese elemento
        tabbed_content = self.query_one("#windows", TabbedContent)
        
        # 3. Definimos cuáles son los IDs válidos para evitar errores

        # Esto es para definir las ventanas como tal, osea cuales estan disponibles
        # asi el programa es inteligente solo busca en un sitio cuales son las disponibles
        # y devolver o no un error para que el usuario sepa
        # si te das cuenta render_profile tiene en el __init__ un argumento llamado id="profile"
        # colocando el nombre exacto del id en esta lista podemos hacer algo que te explico despues
        pestanas_disponibles = ["red", "profile"]

        # aqui recordemos que split() dividio la cadena de caractes del usuario en una lista
        # lo que hacer command es obtenre el primer elemento de esta lista
        # lo llame command porque se supone que ese elemento debe de ser un comando
        command = inputUser[0]

        # Verifica si el comando se encuentra entre los comandos globales 
        
        # NOTA: todo esto fue cmabiado te lo explico igual xd ? 
        #% Pues si te animas a explicar lo cambiado blo
        # - osea me refiero a que todo este "bloque" fue cambiado, si te explico este o 
        # - te explico el cambiado ? 
        #pues deberia ser el nuevo si tiene cosas xd que agrega
        # - bueno entonces no te explico esto xd
        # - de todos modos intenta leerlo y dime que linea no entiendes porque esto lo escribi yo
        # - el nuevo lo saque de un video gringos porque si estaba complicado xd 
        if command in command_global:
            if command == "cd":
                if len(inputUser) < 2:
                    self.notify("Debes especificar un destino. Ejemplo: cd perfil", severity="error")
                    return
                
                # destination es lo que escribio el usuario despues del comando es decir
                # cd profile <-------- en este caso seria profile
                # quedate con lo del profile que lo usaremos de ejemplo
                destination = inputUser[1]
                
                # destination no esta dentro de pestanas_disponibles? 
                # recordemos que pestanas disponible es:
                # pestanas_disponibles = ["red", "profile"]

                # como el usuario escribio profile, quiere decir que si esta dentro de esa lista
                # entonces devuelve un True pero el not lo transforma en false entonces salta al else
                # esto se hace por algo llamado not secure (o algo asi), es para cuando hay
                # muchos if, colocar primero el error y luego lo que se deberia de ejecutar
                # facilita la lectura

                # --------------- Regresa a la linea 233 --------------------
                if destination not in pestanas_disponibles: 
                    self.notify(
                        f"Destino '{destination}' no válido. Prueba con el comando ls para ver los directorios.", 
                        severity="warning"
                    )
                else:

                    # Esta linea
                    # recuerdas que guarmos tal cual las id que mencione antes de profile y red en 
                    # una lista ? 
                    # bueno eso fue para esto
                    
                    #tabbed_content es el widget que contiene los render al inicio 
                    # el .active es lo que explique que muestra la "pestana" que se le asigne
                    # esta pestana la ubica por el id

                    # entoces:
                    # ------- para explicar mejor ponte en la linea 198 --------
                    tabbed_content.active = destination
                    # --------- Retomando ---------------
                    # tabbed_content.active = lo que coloco el usuario
                    # como ya se verifico que el destino si existe lo que ve esa linea es:
                    # tabbed_content.active = profile
                    # como si existe lo que hace es mostar la "ventana" con la ide profile

                    #fin de la explicacion
                    #% ya ya le voy agarrando la onda xd

                    #- si entendiste la explicacion ?
                    #% si blo claro como el agua xd sencillo cuando le das 
                    #- con el tiempo te acostumbras xd
                    #% bueno sera la costumbre para escribirlo sin xd ver o algo que recuerde
                    #- tuve una extensa conversacion con gemenis por eso
                    #- al final por lo que me dijo y por lo que vi
                    #- en realidad ningun senior se sabe todo de memoria xd
                    #- por lo generar todos buscamos en google como se hace tal cosa
                    #- al final lo importante es el como lo resuelves 
                    #- no en que te sepas todo de memoria para hacerlo
                    #- si piensas que la mejor manera de resolver algun problema es por ejemplo:
                    #- tienes que repetir 100 veces las entradas del usuario
                    #- a ti se te ocurre que quizas con un for, pero puede que mejor sea con una 
                    #- funcion recursiva, pero no recuerdas el como se hace una funcion recursiva
                    #- lo buscas en internet xd

                    #- no sabes como hacerlo?, lo buscas en internet, al  final lo importante es resolverlo
                    #- si lo buscas en internet Y lo entendiste, eso es lo que cuenta
                    #- que no cuenta? que lo busques en internet, lo copies y pegues y no sepas como funciona
                    #- porque si tu mismo lo puedes replicar despues de verlo y entenderlo entonces 
                    #- aprendiste un poquito mas 
                    #- entiendes el punto xd ?
                    #%si blo bueno seria todo por hoy xd pq ire a cenar
                    #- dale blo, cualquier cosa escribeme por mess de alguna duda o algo
                    #% dale blochacho
            else:
                execute_command = command_global[command]
                execute_command(self)

        # 4. Limpiamos el input para que pueda volver a escribir cómodamente
        event.input.value = ""
        
if __name__ == "__main__":
    app = AppNavegacionPorTexto()
    app.run()
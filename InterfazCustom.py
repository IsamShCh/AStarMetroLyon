import customtkinter
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageDraw, ImageTk

import math
import re

import subprocess

import socket
import json

#   _   __         _      __   __      
#  | | / /__ _____(_)__ _/ /  / /__ ___
#  | |/ / _ `/ __/ / _ `/ _ \/ / -_|_-<
#  |___/\_,_/_/ /_/\_,_/_.__/_/\__/___/
#         __     __        __          
#   ___ _/ /__  / /  ___ _/ /__ ___    
#  / _ `/ / _ \/ _ \/ _ `/ / -_|_-<    
#  \_, /_/\___/_.__/\_,_/_/\__/___/    
# /___/                                
# Aqui las variables globales importantes
global_tiempo = 0 # valor del tiempo estimado en llegar al destino
global_ruta = [] # resultado del calculo de la ruta
value_izq="" #valor de la estacion de origen
value_der="" # valor de la estacion de destino

estado = False # valor que alterna entre origen y destino

# Bindeado al canvas. Detecta si estamos pulsando sobre alguna estacion.
def seleccionar_en_canvas(event):
    global estado
    global value_izq
    global value_der

    sel_x = int(canvas.canvasx(event.x))
    sel_y = int(canvas.canvasy(event.y))
    radio = 20
    print("Se ha seleccionado un punto en las coordenadas", sel_x, sel_y)
    for station, (x, y) in stations.items():
        distancia = int(math.sqrt((x - sel_x)**2 + (y - sel_y)**2))
        print("La distancia es: "+ str(distancia))
        if distancia <= radio:
            if estado == False:
                value_izq = station
                print("Seleccionado punto " + value_izq)
                estado = True
                dibujarPuntoA()
                break
            else:
                value_der = station
                print("Seleccionado punto " + value_der)
                dibujarPuntoB()
                estado = False
                break

            
# Dibuja sobre la estacion de origen seleccionada un pequeño punto rojo
def dibujarPuntoA():
    x,y = stations[value_izq]
    canvas.delete("puntoA")
    dibujarPuntoA_anim()

# Variables globales relativas al metodo dibujarPuntoA_anim
contador_frames_dibujarPuntoA_anim = 0
size_A_anim = 5
# Ejecuta la animacion de dibujado del punto A (origen)
def dibujarPuntoA_anim():
    x,y = stations[value_izq]
    global contador_frames_dibujarPuntoA_anim
    global size_A_anim
    canvas.delete("puntoA_anim")

    print("Tamaño del boton es " + str(size_A_anim) + " en el frame numero " + str(contador_frames_dibujarPuntoA_anim))
    if (contador_frames_dibujarPuntoA_anim < 5):
        contador_frames_dibujarPuntoA_anim += 1
        size_A_anim -=1
        offset = 1
        canvas.create_oval(x-size_A_anim-offset,y-size_A_anim-offset,x+size_A_anim+offset,y+size_A_anim+offset, fill="red", tags="puntoA_anim")

        canvas.after(10,dibujarPuntoA_anim)
    elif( contador_frames_dibujarPuntoA_anim >= 5 and contador_frames_dibujarPuntoA_anim <= 10):
        contador_frames_dibujarPuntoA_anim += 1
        size_A_anim -=1
        canvas.create_oval(x-size_A_anim,y-size_A_anim,x+size_A_anim,y+size_A_anim, fill="red", tags="puntoA_anim")

        canvas.after(10,dibujarPuntoA_anim)
    else:
        contador_frames_dibujarPuntoA_anim = 0
        size_A_anim = 5
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="red", tags="puntoA")

# Dibuja sobre la estacion de origen seleccionada un pequeño punto rojo
def dibujarPuntoB():
    x,y = stations[value_der]
    canvas.delete("puntoB")
    dibujarPuntoB_anim()
# Variables globales relativas al metodo dibujarPuntoB_anim
contador_frames_dibujarPuntoB_anim = 0
size_B_anim = 5
# Ejecuta la animacion de dibujado del punto A (origen)
def dibujarPuntoB_anim():
    x,y = stations[value_der]
    global contador_frames_dibujarPuntoB_anim
    global size_B_anim
    canvas.delete("puntoB_anim")

    print("Tamaño del boton es " + str(size_B_anim) + " en el frame numero " + str(contador_frames_dibujarPuntoB_anim))
    if (contador_frames_dibujarPuntoB_anim < 5):
        contador_frames_dibujarPuntoB_anim += 1
        size_B_anim -=1
        offset = 1
        canvas.create_oval(x-size_B_anim-offset,y-size_B_anim-offset,x+size_B_anim+offset,y+size_B_anim+offset, fill="blue", tags="puntoB_anim")

        canvas.after(10,dibujarPuntoB_anim)
    elif( contador_frames_dibujarPuntoB_anim >= 5 and contador_frames_dibujarPuntoB_anim <= 10):
        contador_frames_dibujarPuntoB_anim += 1
        size_B_anim -=1
        canvas.create_oval(x-size_B_anim,y-size_B_anim,x+size_B_anim,y+size_B_anim, fill="blue", tags="puntoB_anim")
        canvas.after(10,dibujarPuntoB_anim)
    else:
        contador_frames_dibujarPuntoB_anim = 0
        size_B_anim = 5
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue", tags="puntoB")



# Dibuja las lines entre los puntos que representan las estaciones
def dibujar_conexiones():
    #conexiones
    for station1, station2 in connections:
        x1, y1 = stations[station1]
        x2, y2 = stations[station2]
        size = 10
        color = "#dfdfdf"
        if (station1[-1] == station2[-1]):
            if(station1[-1] == "A"):
                color = color_A
            elif(station1[-1] == "B"):
                color = color_B
            elif(station1[-1] == "C"):
                color = color_C
            elif(station1[-1] == "D"):
                color = color_D

        canvas.create_line(x1+2, y1+2, x2+2, y2+2, fill=ajustar_color(color,0.6), width=size, tags="conexiones_sombra", smooth=TRUE, stipple='gray75')

        canvas.create_line(x1, y1, x2, y2, fill=color, width=size, tags="conexiones", smooth=TRUE)
        
# Dibuja los puntos que representan las estaciones
def dibujar_estaciones():
     # Estaciones
    for station, (x, y) in stations.items():
        silueta = 1
        #normal
        size = 10
        # LAs estaciones que tienen transbornos son fusionadas
        if station in correspondencias : 
            size = 13
            canvas.create_oval(x-size, y-size, x+size, y+size, fill="#feffff", outline="#001526", width=silueta, tags="estaciones")        
        else:
            canvas.create_oval(x-size, y-size, x+size, y+size, fill="#feffff", outline="#001526", width=silueta, tags="estaciones")
            

# Dibuja los nombres de las estaciones
def dibujar_nombres():
    # nombres 
    for station, (x, y) in stations.items():
        if station in global_ruta:
            canvas.create_text(x+50, y-25, text=station[:-2], fill=color_nombres, font=("Helvetica", 12, "bold"),  anchor="center", justify="center", width=100, tags= "nombres")
        else:
            canvas.create_text(x+50, y-25, text=station[:-2], fill=color_nombres, font=("Helvetica", 12, "bold"),  anchor="center", justify="center", width=100, tags= "nombres")


# Coloca de un color distinto el nombre de las estaciones que conforman la ruta generada
def dibujar_nombres_ruta():
    # nombres 
    for station, (x, y) in stations.items():
        if station in global_ruta:
            canvas.create_text(x+50, y-25, text=station[:-2], fill=color_nombres_ruta, font=("Helvetica", 12, "bold"),  anchor="center", justify="center", width=100, tags= "nombres ruta")
   


# Se ejecuta cuando seleccionamos una estacion de origen en la BoxList
def on_select_izq(event):
    global value_izq
    value_izq=listbox1.get()
    dibujarPuntoA()

# Se ejecuta cuando seleccionamos una estacion de destino en la BoxList
def on_select_der(event):
    global value_der
    value_der=listbox2.get()
    dibujarPuntoB()

# Establece el punto de referencia en el canvas a la hora de hacer scroll
def scroll_start(event):
    canvas.scan_mark(event.x, event.y) # guarda las coordenadas sobre las que hemos hecho click para tomarlas como referencia despues en scroll_move

# Funcion para mover el lienzo
def scroll_move (event):
    canvas.scan_dragto (event.x, event.y, gain=1)

# Funcion para hacer zoom (SIN USAR PORQUE DA PROBLEMAS QUE NO SE COMO ARREGLAR //> cambia las coordenadas de todos los puntos y vuelve disfuncionales todas las demas funciones)
def zoom (event):
    canvas.scan_mark(event.x, event.y)
    if event.delta > 0:
        scale = 1.1
    elif event.delta < 0:
        scale = 0.9
    else:
        scale = 1
    canvas.scale ("all", event.x, event.y, scale, scale)

# Llama al socket y calcula la ruta
def calculate_route():
    global global_tiempo
    global global_ruta
    global value_izq
    global value_der

    origen = value_izq
    destino = value_der

    print(origen)
    print(destino)
   
    data = {"origen": origen, "destino": destino}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('localhost', 12345))
            s.sendall(json.dumps(data).encode())
            response = s.recv(4096).decode()
            print(response)
        except Exception as e:
            print(f"Error: {e}")

    input_str = response
    print(input_str)

    try:
        response_dict = json.loads(response)
        global_tiempo = response_dict["tiempo"]
        global_ruta = response_dict["ruta"]

        print(f"Tiempo: {global_tiempo}")
        print(f"Ruta: {global_ruta}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
    except KeyError as e:
        print(f"Clave no encontrada en la respuesta: {e}")
    
    tiempo.configure(text=" ⏳ Tiempo estimado: " + str(global_tiempo) + " minutos  ")

    textbox_estacion_origen.configure(text="     Origen: " + value_izq[:-2] + "  ")
    textbox_estacion_origen_O.configure(text=" ◉", text_color="red")

    textbox_estacion_destino.configure(text="     Destino: " + value_der[:-2] + "  ")
    textbox_estacion_destino_O.configure(text=" ◉", text_color="blue")
    dibujar_ruta()


def dibujar_ruta():
    canvas.delete("ruta")
    canvas.delete("nombre ruta")


    dibujar_nombres_ruta() 
    contador = 1
    for station in global_ruta:
        if (contador < len(global_ruta)):
            x1, y1 = stations[station]
            x2, y2 = stations[global_ruta[contador]]
            color = "#ffffff"
            contador = contador + 1
        
            # Calculamos numero de segmentos y la longitud de cada segmento
            num_segmentos = 10
            dx = (x2 - x1) / num_segmentos
            dy = (y2 - y1) / num_segmentos

            # Dibujamos las lineas en tiras
            for i in range(num_segmentos):
                canvas.create_line(x1 + dx * i, y1 + dy * i, x1 + dx * (i + 1), y1 + dy * (i + 1), fill=color, width=5, smooth=True, tags="ruta_temp", stipple="gray25")
                canvas.tag_raise("puntoA")
                canvas.tag_raise("puntoB")
                canvas.tag_raise("nombres")
                canvas.tag_raise("nombres ruta")
                canvas.update()
                canvas.after(1)  # espera 1 ms
            canvas.delete("ruta_temp")
            canvas.create_line(x1,y1,x2,y2,fill=color, width=5, tags="ruta", smooth=True, stipple="gray25")
            canvas.tag_raise("puntoA")
            canvas.tag_raise("puntoB")
            canvas.tag_raise("nombres")
            canvas.tag_raise("nombres ruta")
            canvas.update()

    return

# Metodo auxiliar para convertir hex a rgb
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Este metodo calcula el gradiente que usamos de fondo
def radial_gradient(size, start_color, end_color, radius):

    img = Image.new("RGB", (size, size))
    draw = ImageDraw.Draw(img)

    max_dist = radius
    r_step = (end_color[0] - start_color[0]) / max_dist
    g_step = (end_color[1] - start_color[1]) / max_dist
    b_step = (end_color[2] - start_color[2]) / max_dist

    for x in range(size):
        for y in range(size):
            dist = ((x - size//2)**2 + (y - size//2)**2)**0.5
            if dist <= radius:
                r = int(start_color[0] + (r_step * dist))
                g = int(start_color[1] + (g_step * dist))
                b = int(start_color[2] + (b_step * dist))
                draw.point((x, y), fill=(r, g, b))
            else:
                draw.point((x, y), fill=end_color)

    return img

# Este metododo ajusta el color en base a un facto (>1 aclarar, <1 oscurece, =1 no cambiar)
def ajustar_color(color, factor):
    # Convertir el color hexadecimal a RGB
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

    # Ajustar los valores RGB
    r = min(max(int(r * factor), 0), 255)
    g = min(max(int(g * factor), 0), 255)
    b = min(max(int(b * factor), 0), 255)

    # Convertir los valores RGB a hexadecimal y devolver el color ajustado
    return "#{:02x}{:02x}{:02x}".format(r, g, b)



#    ____    __           _                 
#   / __/__ / /____ _____(_)__  ___  ___ ___
#  / _/(_-</ __/ _ `/ __/ / _ \/ _ \/ -_|_-<
# /___/___/\__/\_,_/\__/_/\___/_//_/\__/___/
                                        
stations = {
    #Linea A
    
    "Vaulx-en-Velin La Soie A": (1881,788),
    "Laurent Bonnevay Atroballe A": (1672,746),
    "Cusset A": (1539,713),
    "Flachet A": (1408,675),
    "Gratte-Ciel A": (1276,636),
    "Republique Villeurbanne A": (1186,614),
    "Charpennes Charles Hernu A": (1005,624),
    "Massena A": (906,629),
    "Foch A": (786,647),
    "Hotel de Ville Louis Pradel A": (648,675),
    "Cordeliers A": (649,758),
    "Bellecour A": (607,882),
    "Ampere Victor Hugo A": (547,972),
    "Perrache A": (517,1052),

    #Linea C
    "Cuire C" :(605,280), 
    "Henon C" :(527,455), 
    "Croix-Rousse C" :(587,530), 
    "Croix-Paquet C" :(644,596), 
    "Hotel de Ville Louis Pradel C" :(648,675), 


    #Linea B
    "Oullins Gare B" : (350,1728),
    "Stade de Gerland B" : (579,1521),
    "Debourg B" : (619,1419),
    "Place Jean Jaures B" : (687,1255),
    "Jean Mace B" : (736,1124),
    "Saxe Gambetta B" : (813,949),
    "Place Guichard Bourse de Travail B" : (822,850),
    "Gare Part-Dieu Vivier Merle B" : (947,784),
    "Brotteaux B" : (985,694),
    "Charpennes Charles Hernu B" : (1005,624),

    #Linea D
    "Gare de Vaise D": (199,405),
    "Valmy D": (213,521),
    "Gorge de Loup D": (216,690),
    "Vieux Lyon Cathedrale St Jean D": (504,822),
    "Bellecour D": (607,882),
    "Guillotiere D": (750,923),
    "Saxe Gambetta D" : (813,949),
    "Garibaldi D": (921,1014),
    "Sans-Souci D": (1063,1085),
    "Monsplaisir-Lumiere D": (1152,1128),
    "Grange Blanche D": (1272,1185),
    "Laennec D": (1348,1244),
    "Mermoz Pincel D": (1375,1458),
    "Parilly D": (1381,1620),
    "Gare de Venissieux D": (1389,1919)
}

connections = [
    #Linea A
    ("Vaulx-en-Velin La Soie A","Laurent Bonnevay Atroballe A"),
    ("Laurent Bonnevay Atroballe A","Cusset A"),
    ("Cusset A","Flachet A"),
    ("Flachet A","Gratte-Ciel A"),
    ("Gratte-Ciel A","Republique Villeurbanne A"),
    ("Republique Villeurbanne A","Charpennes Charles Hernu A"),
    ("Charpennes Charles Hernu A","Massena A"),
    ("Massena A","Foch A"),
    ("Foch A","Hotel de Ville Louis Pradel A"),
    ("Hotel de Ville Louis Pradel A","Cordeliers A"),
    ("Cordeliers A","Bellecour A"),
    ("Bellecour A","Ampere Victor Hugo A"),
    ("Ampere Victor Hugo A","Perrache A"),

    
    #Linea C
    ("Cuire C","Henon C"),
    ("Henon C","Croix-Rousse C"),
    ("Croix-Rousse C","Croix-Paquet C"),
    ("Croix-Paquet C","Hotel de Ville Louis Pradel C"),


    #Linea B
    ("Oullins Gare B","Stade de Gerland B"),
    ("Stade de Gerland B","Debourg B"),
    ("Debourg B","Place Jean Jaures B"),
    ("Place Jean Jaures B","Jean Mace B"),
    ("Jean Mace B","Saxe Gambetta B"),
    ("Saxe Gambetta B","Place Guichard Bourse de Travail B"),
    ("Place Guichard Bourse de Travail B","Gare Part-Dieu Vivier Merle B"),
    ("Gare Part-Dieu Vivier Merle B","Brotteaux B"),
    ("Brotteaux B","Charpennes Charles Hernu B"),

    
    #Linea D
    ("Gare de Vaise D", "Valmy D"),
    ("Valmy D", "Gorge de Loup D"),
    ("Gorge de Loup D", "Vieux Lyon Cathedrale St Jean D"),
    ("Vieux Lyon Cathedrale St Jean D", "Bellecour D"),
    ("Bellecour D", "Guillotiere D"),
    ("Guillotiere D", "Saxe Gambetta D"),

    ("Saxe Gambetta D", "Garibaldi D"),
    ("Garibaldi D", "Sans-Souci D"),
    ("Sans-Souci D", "Monsplaisir-Lumiere D"),
    ("Monsplaisir-Lumiere D", "Grange Blanche D"),
    ("Grange Blanche D", "Laennec D"),
    ("Laennec D", "Mermoz Pincel D"),
    ("Mermoz Pincel D", "Parilly D"),
    ("Parilly D", "Gare de Venissieux D"),

    #Correspondencias
    ("Saxe Gambetta D", "Saxe Gambetta B"),
    ("Charpennes Charles Hernu B", "Charpennes Charles Hernu A"),
    ("Bellecour A", "Bellecour D"),
    ("Hotel de Ville Louis Pradel C","Hotel de Ville Louis Pradel A")
    ]

correspondencias=["Saxe Gambetta D", "Saxe Gambetta B", "Charpennes Charles Hernu B", "Charpennes Charles Hernu A", "Bellecour A",  "Bellecour D",  "Hotel de Ville Louis Pradel C", "Hotel de Ville Louis Pradel A"]


#    _      _     _                    ___         
#   (_)__  (_)___(_)__    _______  ___/ (_)__ ____ 
#  / / _ \/ / __/ / _ \  / __/ _ \/ _  / / _ `/ _ \
# /_/_//_/_/\__/_/\___/  \__/\___/\_,_/_/\_, /\___/
#                                       /___/      



                                  
#  ___________ ___ _____            
# / __/ __/ -_) _ `/ __/            
# \__/_/  \__/\_,_/_/               
#  _  _____ ___  / /____ ____  ___ _
# | |/ / -_) _ \/ __/ _ `/ _ \/ _ `/
# |___/\__/_//_/\__/\_,_/_//_/\_,_/     
# Creamos la ventana principal
root = ctk.CTk()
root.configure(background='#f7f7f7')  # Set the background color to black
root.title("Sistema De Busqueda De Rutas Para Metro de Lyon")
#root.iconbitmap(".\images\logo.ico")
# root.attributes('-fullscreen', True)

customtkinter.set_appearance_mode("dark")

# Obtenemos la resolucion de la pantalla del usuario
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f'{screen_width}x{screen_height}')
                                    
#    ____    __                
#   / __/__ / /_               
#  _\ \/ -_) __/               
# /___/\__/\__/_               
#  / ___/__  / /__  _______ ___
# / /__/ _ \/ / _ \/ __/ -_|_-<
# \___/\___/_/\___/_/  \__/___/
# Establecemos algunos colores principales
color_canvas = "#171b26"
color_nombres = "#888888"
color_nombres_ruta = "#E3E9AA"

color_A="#e92221"
color_B="#00a6df"
color_C="#f5a400"
color_D="#009d46"

factor = 0.6
color_A=ajustar_color(color_A,factor)
color_B=ajustar_color(color_B,factor)
color_C=ajustar_color(color_C,factor)
color_D=ajustar_color(color_D,factor)

####################################
color1 = hex_to_rgb("#191919")  # #213d49
color2 = hex_to_rgb("#191919")  # #ff0000
color3 = hex_to_rgb("#191919")  # #00ff00
color_degradado = hex_to_rgb("#4d5a80")  # azulito

color_fondo = hex_to_rgb(color_canvas)

tamaño_rectangulo = 1990


#    ____                                
#   /  _/_ _  ___ _                      
#  _/ //  ' \/ _ `/                      
# /___/_/_/_/\_, (_) ___          __     
#  / ___/___/___/___/ (_)__ ___  / /____ 
# / (_ / __/ _ `/ _  / / -_) _ \/ __/ -_)
# \___/_/  \_,_/\_,_/_/\__/_//_/\__/\__/ 
# Creamos la imagen de gradiente que va en el fondo (o la cargamos)
# gradient_img = radial_gradient(1990,color_degradado,color_fondo, 1000)
gradient_img = Image.open(r".\images\bg.png") #NO HACE FALTA CREARLA TODO EL RATO SI PODEMOS CARGARLA
gradient_photoimg = ImageTk.PhotoImage(gradient_img)
gradient_img.save("bg.png", "png")


#  ___________ ___ _____              
# / __/ __/ -_) _ `/ __/              
# \__/_/  \__/\_,_/_/                 
#  _______ ____ _  _____ ____         
# / __/ _ `/ _ \ |/ / _ `(_-<         
# \__/\_,_/_//_/___/\_,_/___/         
# Creamos el canvas sobre el que ira dibujado nuestro mapa
canvas = ctk.CTkCanvas(root, bg=color_canvas,  highlightbackground=color_canvas)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor="nw", image=gradient_photoimg)

# Establecemos el punto de inicio del desplazamiento
canvas.scan_mark(0, 0)

# Movemos el lienzo a las coordenadas más centradas
canvas.scan_dragto(0, -400, gain=1)


#    ___  _ __          _         
#   / _ \(_) /  __ __  (_)__ _____
#  / // / / _ \/ // / / / _ `/ __/
# /____/_/_.__/\_,_/_/ /\_,_/_/   
#   __ _  ___ ____|___/ _         
#  /  ' \/ _ `/ _ \/ _ `/         
# /_/_/_/\_,_/ .__/\_,_/          
#           /_/                   
dibujar_conexiones()
dibujar_estaciones()
dibujar_nombres()

                        
#  ___________ ___ _____  
# / __/ __/ -_) _ `/ __/  
# \__/_/  \__/\_,_/_/     
#   / _/______ ___ _  ___ 
#  / _/ __/ _ `/  ' \/ -_)
# /_//_/  \_,_/_/_/_/\__/ 
# Creamos un marco donde iran contenidos las listas y el boton de "Calcular Ruta"
frame = ctk.CTkFrame(root, bg_color='#f7f7f7')
frame.pack()




#   _____                                
#  / ___/______ ___ _____                
# / /__/ __/ -_) _ `/ __/                
# \___/_/  \__/\_,_/_/                   
#  ______        __  __                  
# /_  __/____ __/ /_/ /  ___ __ _____ ___
#  / / / -_) \ / __/ _ \/ _ \\ \ / -_|_-<
# /_/  \__/_\_\\__/_.__/\___/_\_\\__/___/
# Creamos las textboxes
#canvas.create_text(x+50, y-25, text=station[:-2], fill=color_nombres, font=("Helvetica", 12, "bold"),  anchor="center", justify="center", width=100, tags= "nombres")
fuente = ("Roboto", 12, "bold")
tiempo = CTkLabel(root, text=" ⏳ Tiempo estimado: ", text_color="white", bg_color="transparent", font=fuente)
textbox_estacion_origen = CTkLabel(root, text="     Origen: ", text_color="white", bg_color="transparent", font=fuente)
textbox_estacion_origen_O = CTkLabel(root, text=" ◉", text_color="red", bg_color="transparent", font=fuente)


textbox_estacion_destino = CTkLabel(root, text="     Destino: ", text_color="white", bg_color="transparent", font=fuente)
textbox_estacion_destino_O = CTkLabel(root, text=" ◉", text_color="blue", bg_color="transparent", font=fuente)



# consola_error = CTkLabel(root, text="", text_color="white", bg_color="transparent")
tiempo.place(relx=0.01, rely=0.03, anchor="w")
textbox_estacion_origen.place(relx=0.01, rely=0.07, anchor="w")
textbox_estacion_origen_O.place(relx=0.01, rely=0.07, anchor="w")

textbox_estacion_destino.place(relx=0.01, rely=0.11, anchor="w")
textbox_estacion_destino_O.place(relx=0.01, rely=0.11, anchor="w")
# consola_error.place(relx=0.5, rely=0.5, anchor="ne")



#   _____     _                 
#  / ___/_ __(_)__ _            
# / (_ / // / / _ `/            
# \___/\_,_/_/\_,_/        _    
#  __ _____ __ _____ _____(_)__ 
# / // (_-</ // / _ `/ __/ / _ \
# \_,_/___/\_,_/\_,_/_/ /_/\___/


click_derecho_label = CTkLabel(root, text="  🡲 Click Derecho para seleccionar estación   ", text_color="white", bg_color="transparent", font=fuente)
click_derecho_label.place(relx=0.01, rely=0.95-0.02, anchor="w")

click_izquierdo_label = CTkLabel(root, text="  🡰 Click Izquierdo y arrastrar para desplazarte por el mapa   ", text_color="white", bg_color="transparent", font=fuente)
click_izquierdo_label.place(relx=0.01, rely=0.91-0.02, anchor="w")



#   _____                        
#  / ___/______ ___ _____        
# / /__/ __/ -_) _ `/ __/        
# \___/_/  \__/\_,_/_/           
#    __   _     __  __           
#   / /  (_)__ / /_/ /  ___ __ __
#  / /__/ (_-</ __/ _ \/ _ \\ \ /
# /____/_/___/\__/_.__/\___/_\_\ 
# Creamos listbox
arry = []
for est in stations.keys():
    arry.append(est)

listbox1 = CTkComboBox(frame, values=arry, command=on_select_izq)
listbox2 = CTkComboBox(frame,values=arry, command=on_select_der)

listbox1.pack(side="left")
listbox2.pack(side="left")

#   _____                  
#  / ___/______ ___ _____  
# / /__/ __/ -_) _ `/ __/  
# \___/_/  \__/\_,_/_/     
#   / _ )___  / /____  ___ 
#  / _  / _ \/ __/ _ \/ _ \
# /____/\___/\__/\___/_//_/
# Boton Crear Ruta
button = ctk.CTkButton(frame, text="Calcular Ruta", command=calculate_route)
button.pack(side="left")



#    ___  _         __        
#   / _ )(_)__  ___/ /        
#  / _  / / _ \/ _  /         
# /____/_/_//_/\_,_/          
#  / ___/__ ____ _  _____ ____
# / /__/ _ `/ _ \ |/ / _ `(_-<
# \___/\_,_/_//_/___/\_,_/___/
# Bindeamos los eventos del ratón a las funciones
canvas.bind ("<ButtonPress-1>", scroll_start)
canvas.bind ("<B1-Motion>", scroll_move)
canvas.bind ("<Button-3>", seleccionar_en_canvas)


#    ____     _     _         
#   /  _/__  (_)___(_)__ _____
#  _/ // _ \/ / __/ / _ `/ __/
# /___/_//_/_/\__/_/\_,_/_/   
#   / /  ___  ___  ___        
#  / /__/ _ \/ _ \/ _ \       
# /____/\___/\___/ .__/       
#               /_/           
# Iniciamos el loop.
root.state('zoomed')
root.mainloop()
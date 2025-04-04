playlist={} #diccionario vacío
playlist['canciones']=[] #lista vacía

#funcion principal
def app():
    #agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist=input('\n¿Cómo deseas llamar tu playlist?\n')
        if nombre_playlist:
            playlist['nombre']=nombre_playlist

            #Ya tiene nombre desactica True
            agregar_playlist=False
            # Mandamos a llamar agregar canciones
            agregar_canciones()

def agregar_canciones(): 
     #Bandera para agregar canciones
     agregar_cancio = True

     while agregar_cancio:
        #Preguntar que canción desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgregar canciones a la playlist {nombre_playlist}:\n' 
        pregunta += '\nEscribe "X" para dejar de agregar canciones\n'

        cancion = input(pregunta)
        if cancion == 'x':
             #dejar de agregar canciones 
             agregar_cancio = False

             #mostrar playlist
             mostar_resumen()
        else:
             playlist['canciones'].append(cancion) 
def mostar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\n')
    print('Canciones:\n')      
    for cancion in playlist['canciones']:
        print(cancion)            
app()

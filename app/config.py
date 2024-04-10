class Config:

    #Nom de la fenêtre 
    WINDOW_NAME = 'Transition 50 ans CSUD'

    # largeur de l'écran (et des images)
    SCREEN_WIDTH = 3840

    # hauteur de l'écran (et des images)
    SCREEN_HEIGHT = 2160
    
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # nombre de FPS (normalement, 1)
    desired_fps = 1
    
    # On fait la transition de puis l'image 1 vers l'image 2, situées dans le
    # dossier `data`
    image1 = 'route.jpg'
    image2 = 'lac.jpg'

    # heure de départ
    start_dt = "2024-04-03 20:00:00"
    end_dt = "2024-04-03 20:01:00"
    
    # sauvegarde de l'ordre de transition des pixels
    coords_file = 'coords.json'

    # Proportion du temps alloué aux points:
    dot_time_proportion = 80


    #Danger : ne pas toucher
    cross_width = 3
    cross_height = 3



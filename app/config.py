class Config:
    # largeur de l'écran (et des images)
    SCREEN_WIDTH = 3840
    # hauteur de l'écran (et des images)
    SCREEN_HEIGHT = 2160
    
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # nombre de FPS (normalement, 1)
    desired_fps = 60
    
    # On fait la transition de puis l'image 1 vers l'image 2, situées dans le
    # dossier `data`
    image1 = 'image1.jpg'
    image2 = 'image2.png'
    
    # heure de départ
    start_dt = "2024-03-07 08:00:00"
    end_dt = "2024-03-07 0:24:00"
    
    # sauvegarde de l'ordre de transition des pixels
    coords_file = 'coords.json'

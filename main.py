from game import Game

juego = Game()
#Game().init()
salir = False
while not salir:
    #juego.__init__()
    juego.initialize()
    salir = juego.menurun()
juego.salirgame()        
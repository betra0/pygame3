class Padre:
    def __init__(self):
        print("Esto es del init del Padre")

class Hijo(Padre):
    def __init__(self):
        
        print("Esto es del init del Hijo")
        super().__init__()



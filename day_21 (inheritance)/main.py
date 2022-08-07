class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale...")
    

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water...")


nemo = Fish()
coco = Animal()

# coco.breathe()
# print(f"Coco has {coco.num_eyes} eyes")

# nemo.breathe()
nemo.swim()
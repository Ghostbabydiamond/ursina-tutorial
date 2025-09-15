from ursina import *
from ursina.prefabs import Button
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina
player = FirstPersonController

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube'=(j,o,j),
                     texture='grass cool.png', parent=scene, origin_y=0.5)
        boxes.append(box)
        
app.run()
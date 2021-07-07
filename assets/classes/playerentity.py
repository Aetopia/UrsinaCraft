from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#grass = load_texture('assets/textures/grass.png')
#bricks = load_texture('assets/textures/bricks.png')
class Player(FirstPersonController):
	def __init__(self):
            super(Player, self).__init__()
            self.cursor = Entity(parent=camera.ui, model='sphere', scale = 0.0115, color=color.black)
            camera.fov = 110
            self.height = 1
            self.scale = 0.75
            self.jump_duration = 0.4
            self.jump_height = 0.75
            self.origin_x=30
            self.origin_z=30
            self.origin_y=-2.5
            
class Hand(Entity):
    def __init__(self):
            super().__init__(
            parent = camera.ui,
            model = 'assets/models/block.obj',
            scale = 0.2,
            position = Vec2(0.5, -0.5),
            rotation = Vec3(-12.25,-48,-15)
            )

    def active(self):
        self.rotation = Vec3(50,-48,-15)
        self.position = Vec2(0.3, -0.6)
    
    def passive(self):
        self.rotation = Vec3(-12.25,-48,-15)
        self.position = Vec2(0.5, -0.5)

    def switchactive(self):
            self.position = Vec2(0.5, -0.8)

    def switchpassive(self):
            self.position = Vec2(0.5, -0.5)    
       

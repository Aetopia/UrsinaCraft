import argparse
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("UrsinaCraft Console")

#Default Launch Options 
config = 0
layout = 0
fps = 0
run = 0
#Commands
parser = argparse.ArgumentParser()
parser.add_argument("-layout", action = "store_true", help = "Changes the control layout from WASD to IJKL")
parser.add_argument("-fpsdisplay", action = "store_true", help = "Enables the ingame FPS display")
args = parser.parse_args()
if args.layout == True:
    layout = 1
    run = 1
if args.fpsdisplay == True:
    fps = 1
    run = 1    
#Console    
if run == 0:    
    print("UrsinaCraft v1.0")
    while config == 0:
        control = input()
        if control == str("layout wasd"):
            layout = 0
        elif control == str("layout ijkl"):
            layout = 1
        elif control == str("run"):
            config = 1
            run = 1
        elif control == str("fps on"):
            fps = 1
        elif control == str("fps off"):
            fps = 0
        else:
            print("Invaild syntax!")

#Game
import ursina.application
from ursina import *

app = Ursina()

#Classes
from assets.classes.playerentity import *

#Window
window.fullscreen = False
window.title = 'UrsinaCraft'
window.exit_button.visible = False
window.center_on_screen = True

#Launch Options
if layout == 1:
    input_handler.rebind('i', 'w')
    input_handler.rebind('j', 'a')
    input_handler.rebind('k', 's')
    input_handler.rebind('l', 'd')
if fps == 1:
    window.fps_counter.enabled = True
if fps == 0:
    window.fps_counter.enabled = False    
    
#Resources
grass = load_texture('assets/textures/grass.png')
bedrock = load_texture('assets/textures/bedrock.png')
bricks = load_texture('assets/textures/bricks.png')
planks = load_texture('assests/textures/planks.png')
base = load_texture('assets/textures/base.png')
barrier = load_texture('assets/textures/barrier.png')
baseui = load_texture('assets/textures/baseui.png')
grassui = load_texture('assets/textures/grassui.png')
bricksui = load_texture('assets/textures/bricksui.png')
planksui = load_texture('assest/textures/planksui.png')


#UI
blockid = 1
def update():
    global blockid
    #Animations
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['5'] or held_keys['6'] or held_keys['7'] or held_keys['4'] or held_keys['3'] or held_keys['8'] or held_keys['`']:
        hand.switchactive()
    else:
        hand.switchpassive()
        
    #Block List    
    if layout == 0:
        global blockid
        if held_keys['5']:
            blockid = 1
            blockui.texture = 'grassui'
            hand.texture = 'grass'
            
        if held_keys['4']:
            blockid = 2
            blockui.texture = 'bricksui'
            hand.texture = 'bricks'
            
        if held_keys ['3']:
            blockid = 3
            blockui.texture = 'planksui'
            hand.texture = 'planks' 
          
        if held_keys['`']:
            blockid = x
            blockui.texture = 'baseui'
            hand.texture = 'base'
  
    if layout == 1:
        if held_keys['6']:
            blockid = 1
            blockui.texture = 'grassui'
            hand.texture = 'grass'
            
        if held_keys['7']:
            blockid = 2
            blockui.texture = 'bricksui'
            hand.texture = 'bricks'
            

        if held_keys ['8']:
            blockid = 3
            blockui.texture = 'planksui'
            hand.texture = 'planks'     
     
        if held_keys['`']:
            blockid = x
            blockui.texture = 'baseui'
            hand.texture = 'base'
            
blockui = Entity(model='quad', color=color.color(0,0,random.uniform(1,1)) ,origin_x = -10, origin_y = -5, scale=0.08, texture = 'grassui', parent = camera.ui)
        
#Blocks
class Voxel_Block(Button):
    def __init__(self, position = (0,0,0), texture = 'grass'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/models/block.obj',
            origin_y = 1,
            origin_x = 10,
            origin_z = 10,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.gray,
            scale=0.5)
        
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if blockid == x:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'base')
                if blockid == 1:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'grass')
                if blockid == 2:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'bricks')
                if blockid == 3:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'planks')    
            if key == 'left mouse down':
                destroy(self)  
                
class Voxel_Block_Unbreakable(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/models/block.obj',
            origin_y = 1,
            origin_x = 10,
            origin_z = 10,
            texture = bedrock,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.gray,
            scale=0.5)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if blockid == x:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'base')
                if blockid == 1:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'grass')
                if blockid == 2:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'bricks')
                if blockid == 3:
                    voxel = Voxel_Block(position = self.position + mouse.normal, texture = 'planks')     
                    
                
#World Generation
Barrier = Entity(model = 'assets/models/block.obj',origin_y=-0.5,origin_x= -0.45,origin_z= -0.45,scale=10,texture = 'barrier')
Barrier.collider = 'box'
for z in range(20):
    for x in range(20):
        voxel = Voxel_Block(position = (x,-3,z))
        voxel_unbreakable = Voxel_Block_Unbreakable(position = (x,-4,z))
        
#Player
player = Player()
hand = Hand()        
hand.texture = 'grass'

app.run()



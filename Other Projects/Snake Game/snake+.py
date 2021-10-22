from ursina import *
from ursina.texture_importer import load_texture
import time
import random

def update():
  snake.y += held_keys['w'] * .1
  snake.y -= held_keys['s'] * .1
  snake.x += held_keys['d'] * .1
  snake.x -= held_keys['a'] * .1

app = Ursina()

s = Sprite('Snake_map')
print(s.aspect_ratio)

snake = Entity(
  model ='quad', 
  color = color.green, 
  scale = (5,1), 
  position = (-3,0), 
  collider = 'box'
  #texture = 'snake textures.png'
)

manzana = Entity(
  model ='circle', 
  color = color.red, 
  scale = (1,1), 
  position = (3,0), 
  collider = 'box'
)
app.run()


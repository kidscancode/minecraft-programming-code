import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random

mc = minecraft.Minecraft.create()

def draw_cube(x,y,z,length,b):
    mc.setBlocks(x,y,z,x+length,y+length,z+length,b)

x = 0
y = 10
z = 0
xspeed = 1
#zspeed = 1
yspeed = 1

while True:
    draw_cube(x,y,z,1,block.AIR)
    if x >= 20:
        xspeed = -1
    if x <= -20:
        xspeed = 1
    #if z >= 20:
    #    zspeed = -1
    #if z <= -20:
    #    zspeed = 1
    if y >= 20:
        yspeed = -1
    if y <= 0:
        yspeed = 1
    x += xspeed
    #z += zspeed
    y += yspeed
    draw_cube(x,y,z,1,block.GOLD_BLOCK)
    time.sleep(0.1)

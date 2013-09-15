import minecraft.minecraft as minecraft
import minecraft.block as block
import random

mc = minecraft.Minecraft.create()

block_types = [49, 82, 247, 22, 24, 41, 57, 89]

for i in range(50):
    x = random.randrange(-20,20)
    y = random.randrange(0, 20)
    z = random.randrange(-20,20)
    b = random.choice(block_types)
    mc.setBlocks(x,y,z,x+1,y+1,z+1,b)

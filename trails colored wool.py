import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y-1, pos.z)
    if blockBelow != 0:
        color = random.randrange(16)
        mc.setBlock(pos.x, pos.y-1, pos.z, 35,color)
    time.sleep(0.1)

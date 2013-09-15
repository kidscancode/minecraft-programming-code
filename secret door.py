import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

#build house
mc.setBlocks(5,0,5,10,2,10,block.WOOD)
mc.setBlocks(6,0,6,9,1,9,block.AIR)
mc.setBlock(4,-1,5,247)

while True:
    b = mc.getBlock(4,0,5)
    if b == 41:
        mc.setBlocks(5,0,6,5,1,6,block.AIR)
    elif b > 0:
        mc.postToChat("Intruder!")
        mc.player.setPos(0,0,0)
        mc.setBlock(4,0,5,block.AIR)
    else:
        mc.setBlocks(5,0,6,5,1,6,block.WOOD)
    time.sleep(0.5)

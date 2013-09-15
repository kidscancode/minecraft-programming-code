import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y-1, pos.z)
    if blockBelow != 0:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GOLD_BLOCK)
    time.sleep(0.1)

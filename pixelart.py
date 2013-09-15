import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()

pixelArt = [[0,0,1,0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,1,0,0,0],
            [0,0,1,1,1,1,1,1,1,0,0],
            [0,1,1,0,1,1,1,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1],
            [1,0,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,1],
            [0,0,0,1,1,0,1,1,0,0,0]]

onBlock = block.OBSIDIAN
offBlock = block.WOOL

for row in range(len(pixelArt)):
    for pixel in range(len(pixelArt[row])):
        if pixelArt[row][pixel] == 1:
            mc.setBlock(10, 8-row, 10+pixel, onBlock)
        elif pixelArt[row][pixel] == 0:
            mc.setBlock(10, 8-row, 10+pixel, offBlock)

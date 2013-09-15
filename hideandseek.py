import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import random
import math

mc = minecraft.Minecraft.create()
mc.postToChat("Welcome to Minecraft Hide & Seek!")

def distance(point1, point2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    dz = point2.z - point1.z
    return math.sqrt(dx*dx + dy*dy + dz*dz)

x = random.randrange(-50,50)
y = random.randrange(-5, 10)
z = random.randrange(-50,50)
randomBlock = mc.player.getTilePos()
randomBlock.x += x
randomBlock.y += y
randomBlock.z += z
mc.setBlock(randomBlock.x, randomBlock.y, randomBlock.z, block.DIAMOND_BLOCK)
mc.postToChat("A diamond block has been hidden - go find it!")
print randomBlock

seeking = True
lastPlayerPos = mc.player.getPos()
lastDistance = distance(randomBlock, lastPlayerPos)
timeStarted = time.time()

while seeking == True:
    playerPos = mc.player.getPos()
    if lastPlayerPos != playerPos:
        distanceFromBlock = distance(randomBlock, playerPos)
        print distanceFromBlock
        if distanceFromBlock < 2:
            seeking = False
        else:
            if distanceFromBlock < lastDistance:
                msg = "Warmer: " + str(int(distanceFromBlock)) + " blocks away"
            if distanceFromBlock > lastDistance:
                msg = "Colder: " + str(int(distanceFromBlock)) + " blocks away"
            mc.postToChat(msg)

        lastDistance = distanceFromBlock
    time.sleep(2)

timeTaken = time.time() - timeStarted
msg = "Well done - " + str(int(timeTaken)) + " seconds to find it!"
mc.postToChat(msg)

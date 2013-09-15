import minecraft.minecraft as minecraft
import minecraft.block as block
import random

mc = minecraft.Minecraft.create()

mc.postToChat("WARNING! TNT is live!")

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        blockType = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
        if blockType == 46:
            mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, 46, 1)
            mc.postToChat("Armed!")

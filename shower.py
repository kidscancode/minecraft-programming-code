import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

x = 10
z = 10

mc.setBlocks(x,-1,z, x+2,-1,z+2, block.STONE)
mc.setBlocks(x-1,0,z-1, x+3,0,z+3, block.STONE_SLAB)
mc.setBlocks(x,0,z, x+2,0,z+2, block.AIR)

while True:
    pos = mc.player.getTilePos()
    onx = pos.x >= 10 and pos.x <= 12
    onz = pos.z >= 10 and pos.z <= 12

    if onx and onz and pos.y == 0:
        mc.setBlock(11,2,11, block.WATER)
    else:
        mc.setBlock(11,2,11, block.AIR)




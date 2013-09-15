import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

mc.setBlocks(0,0,0,10,10,10,block.AIR)

h = 0
w = 10
for i in range(6):
mc.setBlocks(i,h,i,w-i,h,w-i,block.CLAY)
    h += 1

import minecraft.minecraft as minecraft
import minecraft.block as block

mc = minecraft.Minecraft.create()

mc.postToChat("Flattening world - this will take some time.")

#remove everything above sea level
mc.setBlocks(-127,0,-127, 127,63,127, block.AIR)

#create a stone area for building
mc.setBlocks(-20,-1,-20, 20,-1,20, block.STONE)

#mark the origin
mc.setBlock(0,-1,0, block.GLOWING_OBSIDIAN)
mc.setBlock(1,-1,0, block.GLOWING_OBSIDIAN)
mc.setBlock(0,-1,1, block.GLOWING_OBSIDIAN)

mc.postToChat("Finished - happy building!")

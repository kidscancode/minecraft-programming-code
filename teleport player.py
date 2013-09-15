import minecraft.minecraft as minecraft
import minecraft.block as block


mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
mc.player.setTilePos(pos.x,pos.y+10,pos.z)
mc.setBlock(pos.x,pos.y+8,pos.z,block.DIAMOND_BLOCK)

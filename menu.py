
#
#
#
#
import nuke
import platform
import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()


#-----Define nuke directory

Win_Dir = 'C:\Users\sgadsden\.nuke'
Mac_Dir = ''
Linux_Dir = '/home/sgadsden/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = Mac_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None


#------Know Defaults
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")



# Create Utilities menu & assign items
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"/icons/myGizmos_icon.png")
myGizmosMenu.addCommand('bm_CameraShake', 'nuke.createNode("bm_CameraShake")', icon="bm_CameraShake_icon.png")
myGizmosMenu.addCommand('bm_EdgeMatte', 'nuke.createNode("bm_EdgeMatte")')
myGizmosMenu.addCommand('Bloom', 'nuke.createNode("Bloom")')
myGizmosMenu.addCommand('Aberration', 'nuke.createNode("Aberration")')
myGizmosMenu.addCommand('bm_OpticalGlow', 'nuke.createNode("bm_OpticalGlow")')





mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")
mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Add.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="From.png", shortcutContext=2)

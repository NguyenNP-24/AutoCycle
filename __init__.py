bl_info = {
    "name": "Walk Cycle Generator",
    "author": "Nguyen Phuc Nguyen",
    "version": (1, 0),
    "blender": (4, 3, 2),
    "location": "View3D > N Panel > WalkCycle",
    "description": "Tạo walk cycle tự động với preset và auto bone detect",
    "category": "Animation",
}

import bpy

# Import các module con
from . import ui_panel
from . import walk_generator
from . import bone_autodetect

# --------------------------------------
# Register / Unregister
# --------------------------------------
modules = [ui_panel, walk_generator, bone_autodetect]

def register():
    for module in modules:
        if hasattr(module, "register"):
            module.register()

def unregister():
    for module in reversed(modules):
        if hasattr(module, "unregister"):
            module.unregister()

if __name__ == "__main__":
    register()

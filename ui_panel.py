import bpy
from bpy.types import Panel
from bpy.props import FloatProperty

# Tạo panel trong 3D View
class WalkCyclePanel(Panel):
    bl_label = "Walk Cycle Generator"
    bl_idname = "VIEW3D_PT_walk_cycle"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Walk Cycle"  # Tab trong sidebar

    def draw(self, context):
        layout = self.layout

        # Đặt tiêu đề
        layout.label(text="Walk Cycle Settings123000")

        # Tạo trường nhập cho tốc độ
        layout.prop(context.scene, "walk_cycle_speed", text="Speed")

        # Tạo trường nhập cho tần suất
        layout.prop(context.scene, "walk_cycle_frequency", text="Frequency")

        # Tạo trường nhập cho chiều cao bước đi
        layout.prop(context.scene, "walk_cycle_step_height", text="Step Height")

        # Nút tạo walk cycle
        layout.operator("object.generate_walk_cycle", text="Generate Walk Cycle")


# Các thuộc tính người dùng có thể chỉnh sửa trong panel
def register():
    from . import walk_generator  # Import operator từ file riêng

    bpy.utils.register_class(WalkCyclePanel)

    # Thêm các thuộc tính cho scene
    bpy.types.Scene.walk_cycle_speed = FloatProperty(
        name="Speed",
        description="Speed of the walk cycle",
        default=1.0,
        min=0.1,
        max=10.0
    )
    
    bpy.types.Scene.walk_cycle_frequency = FloatProperty(
        name="Frequency",
        description="Frequency of the walk cycle",
        default=1.0,
        min=0.1,
        max=5.0
    )
    
    bpy.types.Scene.walk_cycle_step_height = FloatProperty(
        name="Step Height",
        description="Height of the step in the walk cycle",
        default=0.5,
        min=0.1,
        max=2.0
    )


def unregister():
    bpy.utils.unregister_class(WalkCyclePanel)

    # Xóa các thuộc tính scene khi hủy
    del bpy.types.Scene.walk_cycle_speed
    del bpy.types.Scene.walk_cycle_frequency
    del bpy.types.Scene.walk_cycle_step_height

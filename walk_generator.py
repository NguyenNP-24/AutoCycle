import bpy

class GenerateWalkCycleOperator(bpy.types.Operator):
    bl_idname = "object.generate_walk_cycle"
    bl_label = "Generate Walk Cycle"
    
    def execute(self, context):
        # Lấy giá trị từ scene
        speed = context.scene.walk_cycle_speed
        frequency = context.scene.walk_cycle_frequency
        step_height = context.scene.walk_cycle_step_height
        
        # Thực hiện logic tạo walk cycle ở đây
        self.report({'INFO'}, f"Generating walk cycle with speed: {speed}, frequency: {frequency}, step height: {step_height}")
        
        # Ví dụ: logic giả tạo một walk cycle
        # Bạn sẽ thay thế phần này bằng code thực tế của mình
        # Để tính toán, tạo keyframes, chuyển động, v.v.

        return {'FINISHED'}


# Đăng ký operator
def register():
    bpy.utils.register_class(GenerateWalkCycleOperator)


def unregister():
    bpy.utils.unregister_class(GenerateWalkCycleOperator)

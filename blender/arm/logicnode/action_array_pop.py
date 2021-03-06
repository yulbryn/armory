import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ArrayPopNode(Node, ArmLogicTreeNode):
    '''Array pop node'''
    bl_idname = 'LNArrayPopNode'
    bl_label = 'Array Pop'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', 'Array')
        self.outputs.new('NodeSocketShader', 'Value')

add_node(ArrayPopNode, category='Action')

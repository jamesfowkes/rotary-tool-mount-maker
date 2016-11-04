import logging
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader

from rtmmapp.util.geometry import Point, Dimension, Circle

env = Environment(loader=FileSystemLoader('.'))

def get_module_logger():
    return logging.getLogger(__name__)

def create_rotary_tool_holder(lip_outer_diameter, lip_inner_diameter, bottom_diameter, material_thickness, help_text):

    assert(lip_outer_diameter > lip_inner_diameter)

    highest_diameter = max([80, lip_outer_diameter, bottom_diameter])

    document_size = Dimension((highest_diameter * 4) + 50, highest_diameter+5)
    document_centre = Point(document_size.w /2, document_size.h/2) 

    part_spacing = highest_diameter + 5
    
    tailstock_mount_centre_x = highest_diameter / 2
    lip_mount_centre_x = tailstock_mount_centre_x + part_spacing
    bottom_ring_centre_x = lip_mount_centre_x + part_spacing
    jaw_mount_centre_x = bottom_ring_centre_x + part_spacing

    tailstock_mount_radius = (lip_outer_diameter + 6)/2
    lip_mount_radius = lip_inner_diameter/2
    bottom_ring_radius = bottom_diameter/2

    template = env.get_template("template.svg")

    tailstock_mount = Circle(tailstock_mount_centre_x, document_centre.y, tailstock_mount_radius)
    lip_mount = Circle(lip_mount_centre_x, document_centre.y, lip_mount_radius)
    bottom_ring = Circle(bottom_ring_centre_x, document_centre.y, bottom_ring_radius)
    jaw_mount = Point(jaw_mount_centre_x, document_centre.y)


    adapters = [
        Point(document_size.w - 20, document_centre.y + 20 + material_thickness),
        Point(document_size.w - 20, document_centre.y),
        Point(document_size.w - 20, document_centre.y - 20 - material_thickness)
        ]

    adapter_top_slot_centre = Point(jaw_mount_centre_x, document_centre.y - 12.4)
    
    adapter_top_slot_points = [
        Point(adapter_top_slot_centre.x - material_thickness/2, adapter_top_slot_centre.y + 7.5),
        Point(adapter_top_slot_centre.x - material_thickness/2, adapter_top_slot_centre.y - 7.5),
        Point(adapter_top_slot_centre.x + material_thickness/2, adapter_top_slot_centre.y - 7.5),
        Point(adapter_top_slot_centre.x + material_thickness/2, adapter_top_slot_centre.y + 7.5)
    ]

    rotation_origin = jaw_mount

    adapter_left_slot_points = [p.rotate(rotation_origin, degrees=120) for p in adapter_top_slot_points]
    adapter_right_slot_points = [p.rotate(rotation_origin, degrees=-120) for p in adapter_top_slot_points]

    adapter_slots = [
        adapter_top_slot_points,
        adapter_left_slot_points,
        adapter_right_slot_points
    ]
    
    return template.render(
        document_size=document_size,
        tailstock_mount=tailstock_mount,
        lip_mount=lip_mount,
        bottom_ring=bottom_ring,
        jaw_mount=jaw_mount,
        adapters=adapters,
        adapter_slots=adapter_slots,
        material_thickness=material_thickness,
        help_text=help_text
        )
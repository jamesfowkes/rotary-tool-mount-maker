""" rotary-tool-mount-maker.py

Usage:
    rotary-tool-mount-maker.py <lip_outer_diameter> <lip_inner_diameter> <bottom_diameter> [--material_thickness=<mm>] [-v]

Options:
  <lip_outer_diameter>        Name of the SVG to produce
  <lip_inner_diameter>        XY dimensions of the board
  <bottom_diameter>           XY spacing of the holes
  --material_thickness=<mm>   Material thickness in mm [default: 3]
  -v --verbose                Turn on verbose output
"""

import docopt
import logging

import svg

HELP_TEXT = [
    "Cut black paths. Engrave or fast cut blue paths for positioning guides.",
    "Glue part #2 centrally onto part #1 using engraved/cut guide.",
    "Glue ring #3 centrally onto part #4 using engraved/cut guide",
    "Glue 3x mounting parts into slots in #4 on opposite side to ring."
]

def get_module_logger():
    return logging.getLogger(__name__)

if __name__ == "__main__":

    args = docopt.docopt(__doc__)

    if args["--verbose"]:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    lip_outer_diameter = float(args["<lip_outer_diameter>"])
    lip_inner_diameter = float(args["<lip_inner_diameter>"])
    bottom_diameter = float(args["<bottom_diameter>"])
    material_thickness = float(args["--material_thickness"])

    print(svg.create_rotary_tool_holder(lip_outer_diameter, lip_inner_diameter, bottom_diameter, material_thickness, HELP_TEXT))

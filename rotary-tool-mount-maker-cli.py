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

import sys
import docopt
import logging

import rtmmapp.util.util
import rtmmapp.util.svg

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

    error = rtmmapp.util.util.validate_diameters(lip_outer_diameter, lip_inner_diameter, bottom_diameter)
    if error is None:
      print(rtmmapp.util.svg.create_rotary_tool_holder(
        lip_outer_diameter, lip_inner_diameter, bottom_diameter, material_thickness, rtmmapp.util.util.get_help_text()))
    
    else:
      sys.exit("Error: {}".format(error))

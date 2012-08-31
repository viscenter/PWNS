# This program is specially formated to work with Calib3.0
#
# The purpose of this program is to duplicate the vertices of a partial section
#   to it's mirror side Horizontally without modifying the quantity of vertices
#   on the calibration/configuration file.
#
# Author: Karlo Luis Martinez Martos (VisU Program, UKY)

import sys

filename = sys.argv[1]

origin_row = sys.argv[2]

manip_row = sys.argv[3]

def Row_Symm (filename, origin_row, manip_row):

    #Open Specified File
    f = codecs.open(filename, 'rU', 'utf-8')

    #Capture File Content


    #Content Manipulation Arguments


    #Re-insert Content (manipulated)

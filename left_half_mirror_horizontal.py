# This program is specially formated to work with Calib3.0
#
# The purpose of this program is to duplicate the vertices of a partial section
#   to it's mirror side Horizontally without modifying the quantity of vertices
#   on the calibration/configuration file.
#
# Author: Karlo Luis Martinez Martos (VisU Program, UKY)

#Exit solution   sys.exit(0)

import sys
#OS and other commands
#

filename = sys.argv[1]

def left_mirror_h(filename) :

    #Vertice dimensions
    
    
    f = codecs.open(filename, 'rU', 'utf-8')

    for line in f:
        print line,

        
        dimensions = re.search(r'\d+ x \d+', line)
        
    vertice_list = re.findall(r'[\d+ \d+\.*\d+ \d+\.*\d+ \d+\.*\d+ \d+\.*\d+ \d+\.*\d+]+', f)
        

    f.close()



if __name__ == '__main__':
    left_mirror_h()

#if __name__ == '__main__':
#    main()

    

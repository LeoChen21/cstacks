from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]

parse_file( 'script.txt', edges, polygons, csystems, screen, color )

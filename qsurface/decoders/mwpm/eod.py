from typing import List, Tuple
from ...codes.elements import AncillaQubit
from .._template import Sim
import networkx as nx
from numpy.ctypeslib import ndpointer
import ctypes
import os
import numpy as np

LA = List[AncillaQubit]

######### I'm going to implement 2D and unweighted EOD first ##########

# This function returns a list of adjacent edges with respect to the given ancilla qubit
def adjacent_edges(vertice: AncillaQubit, lattice_size: int):
    elist = []
    (i, j) = vertice.loc
    elist.append(lattice_size * j + i)
    elist.append(lattice_size * j + i - 1)
    elist.append(lattice_size * lattice_size + (lattice_size - 1) * i + j - 1)
    elist.append(lattice_size * lattice_size + (lattice_size - 1) * i + j)

    return elist

# This function performs MWPM with Edge On Demand matching
def match_eod(vertices: LA, lattice_size: int):
    E = np.zeros(2 * lattice_size * lattice_size) # E is the list of lattice edges, and it is used to support alternating tree growths. 0 if edge is unoccupied, 1 if half-occupied, and 2 if fully occupied
    matching = []
    # Copy the given vertices into the list of unmatched vertices
    V_u = vertices[:]

    # Iterate unless V_u is empty
    while V_u:
        root = V_u.pop()
        boundary = []              # Boundary refers to the boundary of an alternating tree
        boundary.append(root)
        while True:
            pass
    

    return matching

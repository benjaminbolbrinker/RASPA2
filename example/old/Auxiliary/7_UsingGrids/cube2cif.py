#!/bin/python3

from ase.io import write
from ase.io.cube import read_cube


with open('grid.cube', 'r') as fp:
    atoms = read_cube(fp, read_data=False)['atoms']

write('grid.cif', atoms)

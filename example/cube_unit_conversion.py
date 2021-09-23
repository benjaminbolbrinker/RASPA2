#!/usr/bin/python3.8

import ase
from ase.io.cube import write_cube

import argparse

from pathlib import Path

parser = argparse.ArgumentParser(
        description='Convert cube or xsf grid to cube file with RASPA units.')
parser.add_argument(
        'input_file',
        help='File containing the energy grid.')
parser.add_argument(
        'output_file',
        default='grid.cube',
        help='Name for the cube file.')
parser.add_argument(
        '--unit',
        type=str,
        help='Energy unit in the input file (default: kjmol).',
        default='kjmol'
        )

args = parser.parse_args()
in_path = Path(args.input_file)
out_path = Path(args.output_file)
if in_path.suffix == '.xsf':
    atoms = ase.io.read(in_path, read_data=False)
    data = ase.io.read(in_path, read_data=True)
elif in_path.suffix == '.cube':
    with open(in_path, 'r') as fp:
        cube_data = ase.io.cube.read_cube(fp)
        atoms = cube_data['atoms']
        data = cube_data['data']

# Convert to J / mol
if args.unit == 'ev':
    data = data*96485.30749925794
elif args.unit == 'ry':
    data = data*0.018374652475604065
elif args.unit == 'kjmol':
    data = data*1e3
else:
    raise ValueError

data = data / 10  # convert to 10 J / mol (RASPA energy unit)

with open(out_path, 'w') as fp:
    write_cube(fp, atoms, data)

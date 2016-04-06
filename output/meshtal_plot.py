from pyne import mcnp
from itaps import iBase, iMesh
import h5py
import sys


def convert_meshtal(argv):
    """simple convert meshtal to vtk via h5m """
    in_path = argv[0]
    out_path = argv[1]
    
    meshtal1 = mcnp.Meshtal(in_path)
    meshtal1.tally[14].mesh.save(out_path + ".vtk")

   
if __name__ == "__main__":
    convert_meshtal(sys.argv[1:])

from pyne import mcnp
from itaps import iBase, iMesh
import h5py
import sys
from subprocess import call


def convert_meshtal(argv):
    """simple convert meshtal to vtk via h5m """
    in_path = argv[0]
    out_path = argv[1]
    tnum = int(argv[2])
    
    meshtal1 = mcnp.Meshtal(in_path)
    meshtal1.tally[tnum].mesh.save(out_path + ".vtk")


    #call(["expand_tags.py", out_path+".h5m" , "-o", out_path+".vtk"])
    #call(["rm", out_path+".h5m"])

   
if __name__ == "__main__":
    convert_meshtal(sys.argv[1:])

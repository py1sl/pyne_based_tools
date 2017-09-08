from pyne import mcnp
from itaps import iBase, iMesh
import h5py
import sys
from subprocess import call
import argparse


def convert_meshtal(in_path, tnum, out_path="meshtal"):
    """simple convert meshtal to vtk via h5m """
        
    meshtal1 = mcnp.Meshtal(in_path)
    print(meshtal1.tally)
    meshtal1.tally[tnum].mesh.save(out_path + ".vtk")


    #call(["expand_tags.py", out_path+".h5m" , "-o", out_path+".vtk"])
    #call(["rm", out_path+".h5m"])

   
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MCNP mesh tally to vtk format")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("tally", help="tally number to convert", default=1, type=int )
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file without filetype")

    args = parser.parse_args()    

    if args.output:
        convert_meshtal(args.input, args.tally, args.output)
    else:
        convert_meshtal(args.input, args.tally)

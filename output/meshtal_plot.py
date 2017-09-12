from pyne import mcnp
from itaps import iBase, iMesh
import h5py
import sys
from subprocess import call
import argparse


def convert_meshtal(in_path, tnum, out_path="meshtal", tags=False):
    """simple convert meshtal to vtk via h5m """
        
    meshtal1 = mcnp.Meshtal(in_path)
    print(meshtal1.tally)
    print(meshtal1.tally[tnum].mesh.tag)
    if tags:
        meshtal1.tally[tnum].mesh.save(out_path + ".h5m")
        call(["expand_tags.py", out_path+".h5m" , "-o", out_path+".vtk"])
        call(["rm", out_path+".h5m"])

    else:
        meshtal1.tally[tnum].mesh.save(out_path + ".vtk")



   
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MCNP mesh tally to vtk format")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("tally", help="tally number to convert", default=1, type=int )
    parser.add_argument("-o", "--output", action="store", dest="output",  
                        help="path to the output file without filetype")
    parser.add_argument("-t", "--tags", action="store_true", dest="tags",  
                        help="use this if want all tags to be expanded and results for all")

    args = parser.parse_args()    

    if args.output:
        if args.tags:
            convert_meshtal(args.input, args.tally, args.output, True)
        else:
            convert_meshtal(args.input, args.tally, args.output)
    else:
        if args.tags:
            convert_meshtal(args.input, args.tally, "meshtal", True)
        else:
            convert_meshtal(args.input, args.tally)

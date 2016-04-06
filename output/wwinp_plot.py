from pyne import mcnp
from itaps import iBase, iMesh
import h5py
import sys
from subprocess import call


def convert_wwinp(argv):
    """simple conversion of wwinp to vtk via h5m """
    in_path = argv[0]
    out_path = argv[1]

    wwinp_mesh = mcnp.Wwinp()
    wwinp_mesh.read_wwinp(in_path)
    wwinp_mesh.mesh.save(out_path+".h5m")

    call(["expand_tags.py", out_path+".h5m" , "-o", out_path+".vtk"])
    call(["rm", out_path+".h5m"])


if __name__ == "__main__":
    convert_wwinp(sys.argv[1:])

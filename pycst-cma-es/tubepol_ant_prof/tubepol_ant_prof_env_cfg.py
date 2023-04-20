import sys


ENV = "win"
# ENV = "hpc"

# Add dependent paths on HPC
if "hpc" == ENV:
    # Add dependency directories on HPC
    sys.path.append('/data/scratch/eex181/pycst-master/pycst-master/pycst')
    # sys.path.append('/data/scratch/eex181/TubePolAntProfileGroup/pycst_hpc/deepem')
    # sys.path.append('C:/Users/WayneJu/Desktop/Project/pycst-master/pycst-master/pycst')

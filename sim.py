import sys

pathto = sys.argv[1]
sys.path.append(pathto)

from lib.lammps_generator import * 


import numpy as np 

system_parameters = {
    "sigma0": 0.626,
    "mass0": 44,
    "eps0": 1.0,
    "rho_real": 0.0003,
    "nchain": 20,
    "nmonomers": 168,
    "phi_hs": 0.01,
    "filename": "rho_0_004_phi_hs_0_05",
    "num_files":    5,
    "type_simulation": True,
    "number_of_steps": 10000,
    "number_of_steps_equilibration": 10000
}
        
simulation = PolymerSimulation(system_parameters,pathto)

# phi_hs = np.arange(0.005,0.31,0.01)
# print(phi_hs)
# for phis in phi_hs:
#     system_parameters.update({'phi_hs': phis})
#     system_parameters.update({'filename': "rho_0_004_phi_hs_"+str(np.round(phis,3))})
#     simulation = PolymerSimulation(system_parameters,pathto)        

import os

from ase.calculators.aims import Aims

model_abs_dir = os.path.abspath(os.path.dirname(__file__))

FHIAIMS_PATH = "PATH_TO_FHIAIMS"

FHIAIMS_EXECUTABLE = 'aims.171019.mpi.x'
SPECIES_SETTINGS = "tight"
MPI_NP_PROC = 4

AIMS_EXECUTABLE = os.path.join(FHIAIMS_PATH, "bin", FHIAIMS_EXECUTABLE)
AIMS_OUTPUT = "FHI.out"
AIMS_COMMAND = "mpirun -np {} {} > {}".format(MPI_NP_PROC, AIMS_EXECUTABLE, AIMS_OUTPUT)

os.environ['AIMS_SPECIES_DIR'] = os.path.join(FHIAIMS_PATH,
                                              'documentation/species_defaults',
                                              SPECIES_SETTINGS)

fhiaims_parameters = {'sc_iter_limit': '500',
                      'relativistic': 'atomic_zora scalar',
                      'sc_accuracy_forces': '1E-4',
                      'occupation_type': 'gaussian 0.10',
                      'sc_accuracy_etot': '1E-7',
                      'sc_accuracy_eev': '1E-3',
                      'sc_accuracy_rho': '1E-5',
                      'spin': 'none',
                      'xc': 'pbe'}

no_checkpoint = True

def start(test_name):
    global calculator
    calculator = Aims(aims_command=AIMS_COMMAND,
                      label=test_name,
                      outfilename=AIMS_OUTPUT,
                      kpts=1 / 0.15,
                      **fhiaims_parameters
                      )

import os

from ase.calculators.aims import Aims

model_abs_dir = os.path.abspath(os.path.dirname(__file__))

os.environ['AIMS_SPECIES_DIR'] = 'PATH_TO_FHIAIMS/documentation/species_defaults/light'

no_checkpoint = True

def start(test_name):
    global calculator
    calculator = Aims(aims_command="PATH_TO_FHIAIMS/bin/aims.171019.serial.x",
                      label=test_name,
                      outfilename="FHI.out",
                      xc="pbe",
                      k_grid="1 1 1"
                      )

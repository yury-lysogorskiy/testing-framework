from pyace import PyACECalculator
import os
import glob

model_dir = os.path.dirname(os.path.realpath(__file__))
pot_name = glob.glob(os.path.join(model_dir,"*.ace"))[0]

calculator = PyACECalculator(pot_name)

no_checkpoint = True

name = "ACE"

import matplotlib.pyplot as plt
from geothermal_orc_design import single_parameter_influence
from collections import OrderedDict

import itertools

import json
import sys


with open(sys.argv[1], 'r') as f:
    input_data = json.load(f)
    f.close()

result = single_parameter_influence(**input_data)

print(result)

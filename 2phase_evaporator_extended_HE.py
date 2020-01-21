from tespy import con, nwk, cmp, hlp, cmp_char
#from matplotlib import pyplot as plt
import numpy as np
from tespy.tools import logger
import logging
mypath = logger.define_logging(
log_path=True, log_version=True, timed_rotating={'backupCount': 4},
screen_level=logging.WARNING, screen_datefmt = "no_date")

fluids = ['water', 'Isopentane']

nw = nwk.network(fluids=fluids)
nw.set_attr(p_unit='bar', T_unit='C', h_unit='kJ / kg')
nw.set_printoptions(print_level='info')
# components
# main components
evaporator = cmp.evaporator('evaporator')
# working fluid
source_wf = cmp.source('working fluid source')
sink_wf = cmp.sink('working fluid sink')
#brine
source_s = cmp.source('steam source')
source_b = cmp.source('brine source')
sink_s = cmp.sink('steam sink')
sink_b = cmp.sink('brine sink')
# connections
# main cycle
evaporator_wf_in = con.connection(source_wf, 'out1', evaporator, 'in3', m=243.72)
evaporator_wf_out = con.connection(evaporator, 'out3', sink_wf, 'in1')

evaporator_steam_in = con.connection(source_s, 'out1', evaporator, 'in1')
evaporator_sink_s = con.connection(evaporator, 'out1', sink_s, 'in1')
evaporator_brine_in = con.connection(source_b, 'out1', evaporator, 'in2')
evaporator_sink_b = con.connection(evaporator, 'out2', sink_b, 'in1')
nw.add_conns(evaporator_wf_in, evaporator_wf_out, evaporator_steam_in, evaporator_sink_s, evaporator_brine_in, evaporator_sink_b)
# parametrization of components
evaporator.set_attr(pr1=0.93181818, pr2=0.970588, pr3=1)

# parametrization of connections
evaporator_wf_in.set_attr(T=111.6, fluid={'water': 0, 'Isopentane': 1})
evaporator_wf_out.set_attr(T=119.8, p=10.8, state='g')

evaporator_steam_in.set_attr(T=146.6, p=4.4, state='g', fluid={'water': 1, 'Isopentane': 0})
evaporator_sink_s.set_attr(T=132.5)

evaporator_brine_in.set_attr(T=146.6, p=10.2, m=191, fluid={'water': 1, 'Isopentane': 0})
evaporator_sink_b.set_attr(T=118.6)
# solving
mode = 'design'
file = 'yangyi_evaporator_new'
# solve the network, print the results to prompt and save
nw.solve(mode=mode)
nw.print_results()
nw.save(file)

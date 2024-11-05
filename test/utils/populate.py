import sys
import os
import numpy as np

SIMULATOR_PATH=""
sys.path.insert (0, SIMULATOR_PATH + '/include/')
sys.path.insert (0, SIMULATOR_PATH + '/src/') 
sys.path.insert (0, SIMULATOR_PATH +'/')

THIS_PATH = os.getcwd()


from src.data_convert import *
import src.ima as ima
from src.instrn_proto import *
import config as cfg
from data_config import datacfg


#path = 'coreMvm_test/'
#wt_path = path
#inst_file = path + 'imem1.npy'
#trace_file = path + 'trace.txt'
#dump_file = path + 'memsim.txt'

datamem_off = cfg.datamem_off # each matrix has 6 memory spaces (1 for f/b, 2 for d)
#phy2log_ratio = cfg.phy2log_ratio # ratio of physical to logical xbar
xbar_size = cfg.xbar_size

weight_files =[]

for i in os.listdir(THIS_PATH):
    if i.endswith('.weights'):
        dataset = i.split('-')[0]
        tile_id = i.partition('tile')[2][0]
        core_id = i.partition('core')[2][0]
        mat_id = i.partition('mvmu')[2][0]
        os.system('mkdir -p ' + dataset + '/weights/tile' + tile_id + '/core' + core_id)
        wt_path = dataset + '/weights/tile' + tile_id + '/core' + core_id + '/'
        #print(wt_path)
        os.system('cp '+ i + ' ' + dataset + '/weights/tile' + tile_id + '/core' + core_id)
        with open(i) as f:
            line = f.readline()
            arr = np.fromstring(line, dtype=float, sep=' ')
            log_xbar = np.reshape(arr, (xbar_size, xbar_size))
            phy_xbar = [np.random.randn(xbar_size, xbar_size) for i in range(datacfg.ReRAM_xbar_num)]
#
## NOTE: weights programmed to xbars are stored in terms of their representative floating values
## for use in np.dot (to store bits representation, use fixed point version of np.dot)
            for i in range (xbar_size):
                for j in range (xbar_size):
                    temp_val = float2fixed(log_xbar[i][j], datacfg.int_bits, datacfg.frac_bits)
                    assert (len(temp_val) == 16)
                    for k in range(datacfg.ReRAM_xbar_num):
                        if (k==0):
                            val = temp_val[-1 * datacfg.storage_bit[k + 1]:]
                        else:
                            val = temp_val[-1 * datacfg.storage_bit[k + 1]: -1 * datacfg.storage_bit[k + 1] + int(datacfg.storage_config[k])]
            # augment sign extension (used in MSB xbar only)
                        if (k == (len(phy_xbar)-1)):
                            val = (datacfg.num_bits - datacfg.storage_bit[k])*val[0] + val[0:]
                        phy_xbar[k][i][j] = fixed2float(val, datacfg.int_bits, datacfg.frac_bits)
## save log_xbar and phy_xbar to disc
            np.save (wt_path+'log_xbar'+str(mat_id), log_xbar)
            for k in range (len(phy_xbar)):
                np.save (wt_path+'mat'+str(mat_id)+'-phy_xbar'+str(k), phy_xbar[k])





import sys, os
import numpy as np
import math
sys.path.insert (0, '/home/plinio/puma-simulator/include/')
sys.path.insert (0, '/home/plinio/puma-simulator/src/')
sys.path.insert (0, '/home/plinio/puma-simulator/')
from data_convert import *
from instrn_proto import *
from tile_instrn_proto import *
dict_temp = {}
dict_list = []
i_temp = i_set(d1=513, imm=11552, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10080, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11568, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10112, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=160, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11584, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10144, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=176, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11600, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10176, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=192, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11616, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10208, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=208, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11632, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10240, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=224, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=240, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11680, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10272, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11696, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10304, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=288, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11712, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10336, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=304, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11728, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10368, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=320, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11744, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10400, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=336, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11760, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10432, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=352, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=368, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11808, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10464, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11824, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10496, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=416, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11840, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9024, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=432, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12320, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11856, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9280, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=448, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12352, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11872, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9312, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=464, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12384, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11888, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9344, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=480, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12416, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=496, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11936, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10528, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11952, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10560, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=544, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=11968, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9472, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=560, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12448, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=11984, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9504, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=576, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12480, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12000, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9536, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=592, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12512, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12016, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9568, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=608, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12544, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=624, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12064, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10592, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12080, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10624, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=672, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12096, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9696, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=688, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12576, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12112, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9728, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=704, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12608, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12128, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9760, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=720, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12640, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12144, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9792, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=736, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12672, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=752, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12192, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=529, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=10656, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12208, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10688, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=577, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=545, imm=800, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=545, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12224, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9920, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=816, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12704, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12240, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9952, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=832, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12736, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12256, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=513, r1=513, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=513, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=9984, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=848, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=529, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=529, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=529, r1=529, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=561, imm=12768, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=561, r1=529, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=529, imm=12272, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=529, r1=529, load_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=0, r1=529, vec=16, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_mvm(['10'])
dict_list.append(i_temp.copy())
i_temp = i_copy(d1=545, r1=256, vec=32, src_type=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=577, imm=10016, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=578, imm=864, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=578, r1=513, counter=5, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_load(d1=577, r1=577, load_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_alu('add', d1=545, r1=545, r2=577, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_alu('sig', d1=545, r1=545, vec=32)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=12800, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=545, counter=1, store_width=16, vec=2)
dict_list.append(i_temp.copy())
i_temp = i_set(d1=513, imm=880, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_store(d1=513, r1=529, counter=4, store_width=16, vec=1)
dict_list.append(i_temp.copy())
i_temp = i_hlt()
dict_list.append(i_temp.copy())
filename = 'lenet/tile3/core_imem4.npy'
np.save(filename, dict_list)

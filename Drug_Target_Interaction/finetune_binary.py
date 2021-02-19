import os
os.chdir('./')

from DeepPurpose import oneliner
from DeepPurpose.dataset import *

FILE_PATH = './toy_data/egfr.txt'

oneliner.repurpose(*load_EGFR(), *load_broad_repurposing_hub2(no_cid = True),  *read_file_training_dataset_bioassay(FILE_PATH), \
    split='HTS', convert_y = False, frac=[0.7,0.2,0.1], finetune_batch_size = 128, pretrained = False, agg = 'agg_mean_max')

# Binary 결과 원할 경우 DTI.py line 293 self.binary = True로 바꿔줘야함

import torch
import torch.nn as nn
from collections import OrderedDict

import numpy as np
from netdissect import stylegan

def from_pt_file(filename):
    gen = nn.Sequential(OrderedDict([
        ('g_mapping', stylegan.G_mapping()),
        ('g_synthesis', stylegan.G_synthesis())]))
    gen.load_state_dict(torch.load(filename))
    gen.eval()
    gen.input_shape = (1, 512)
    return gen

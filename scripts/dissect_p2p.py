#! bin/bash/env python3

# run a quick generator test
import sys
sys.path.append('../pytorch-CycleGAN-and-pix2pix')
import torch
import importlib
from models import networks
from torchvision import datasets, transforms
from unet_normalized import UnetNormalized

from netdissect import InstrumentedModel, dissect
from netdissect import GeneratorSegRunner
from netdissect.progress import verbose_progress, print_progress
from netdissect.modelconfig import create_instrumented_model

out_dir = 'dissect/p2p'

layer5 = ('model.model.1.model.3.model.3.model.3.model.1', 'layer5')
layer9 = ('model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.3', 'layer9')
layer12 = ('model.model.1.model.3.model.3.model.3.model.5', 'layer12') 

# these are changes to be added to __main__.py for a custom dissection of pix2pix

#generator = networks.define_G(3, 3, 64, netG='unet_256', norm='batch', use_dropout=False)
generator = UnetNormalized()
#networks.init_weights(generator, init_type='normal', init_gain=0.02)
checkpoint = torch.load('models/pix2pix/churches_lsun_G.pth')

generator.load_state_dict(checkpoint)
#generator.eval()
generator.cuda()
generator.no_grad()

data = datasets.ImageFolder('dataset/Adissect', transform=transforms.Compose(
    [transforms.Resize((256,256), Image.BICUBIC), transforms.RandomCrop((256,256)),
     transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]))

torch.backens.cudnn.benchmark = True

verbose_progress(True)

dataset = data
train_dataset = data

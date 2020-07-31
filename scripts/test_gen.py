#! bin/bash/env python3

# run a quick generator test
import sys
sys.path.append('../pytorch-CycleGAN-and-pix2pix')
import torch
import importlib
from models import networks
from torchvision import datasets, transforms
from torchvision.utils import save_image
from PIL import Image
from netdissect.unet_normalized import UnetNormalized

#generator = networks.define_G(3, 3, 64, netG='unet_256', norm='batch', use_dropout=False)
generator = UnetNormalized()
#networks.init_weights(generator, init_type='normal', init_gain=0.02)
checkpoint = torch.load('models/pix2pix/churches_lsun_G.pth')

generator.load_state_dict(checkpoint)
#generator.eval()
generator.cuda()

data = datasets.ImageFolder('dataset/Adissect', transform=transforms.Compose(
    [transforms.Resize((256,256), Image.BICUBIC), transforms.RandomCrop((256,256)),
     transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]))
loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False)

for idx, (img,_) in enumerate(loader):
    y = generator(img.cuda())
    save_image(y, 'test_dump/testimg%d.png'%idx)
    if idx == 100:
        break

#!bin/bash/env python3

import torch
from torchvision import datasets, transforms
import lmdb
import PIL

from netdissect import segmenter, segviz

data = datasets.LSUN('../lsun/', ['church_outdoor_train'], transform=transforms.Compose([transforms.CenterCrop(256), transforms.ToTensor()]))
data_loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False)

upp = segmenter.UnifiedParsingSegmenter(segdiv=None)

to_img = transforms.ToPILImage()
for idx, (img_batch,_) in enumerate(data_loader):
    to_img(img_batch.squeeze()).save('B/%d.jpeg'%idx, 'JPEG')
    PIL.Image.fromarray(segviz.segment_visualization(upp.segment_batch(img_batch.cuda())[0].cpu().numpy(), size=256)).save('A/%d.jpeg'%idx, 'JPEG')
    if idx % 100 == 0:
        print('percent complete: %f.2'%(100 * (idx / len(data_loader)))) 

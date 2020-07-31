#!/bin/bash env python3
from netdissect.p2pgan import from_pth_file, get_segments_dataset
from netdissect import GeneratorSegRunner
from netdissect import p2pgan
import torch
from torchvision import transforms
from netdissect.nethook import InstrumentedModel
from netdissect.autoeval import autoimport_eval
from netdissect.modelconfig import annotate_model_shapes
from netdissect.segviz import segment_visualization
import PIL
batch_size=1

data = get_segments_dataset('dataset/Adissect_toy')
#model = autoimport_eval("p2pgan.from_pth_file('models/pix2pix/p2p_churches.pth')")
model = from_pth_file('models/pix2pix/p2p_churches.pth')
segmenter = ("netdissect.segmenter.UnifiedParsingSegmenter(segsizes=[256], segdiv='quad')")
segrunner = GeneratorSegRunner(autoimport_eval(segmenter))

layer5 = ('model.model.1.model.3.model.3.model.3.model.1', 'layer5')
layer9 = ('model.model.1.model.3.model.3.model.3.model.3.model.3.model.3.model.3', 'layer9')
layer12 = ('model.model.1.model.3.model.3.model.3.model.5', 'layer12')

model = InstrumentedModel(model)
model.retain_layers([layer5, layer9, layer12])
annotate_model_shapes(model, gen=True, imgsize=None)

segloader = torch.utils.data.DataLoader(data, batch_size=batch_size, pin_memory=True)

to_img = transforms.ToPILImage()
for i, batch in enumerate(segloader):
    to_img(batch[0].squeeze()).save('test/input%d.png'%i, 'PNG')
    outseg, bc, rgb, shape = segrunner.run_and_segment_batch(batch, model, want_bincount=False, want_rgb=True)
    PIL.Image.fromarray(segment_visualization(outseg.squeeze().cpu().numpy(), size=256)).save('test/outseg%d.png'%i, 'PNG')
    to_img(rgb.permute(0, 3, 2, 1).squeeze().cpu()).save('test/output%d.png'%i, 'PNG')
    if i % 100 == 0:
        print('percent complete: %f' %(100 * (i / len(segloader))))

import sys
sys.path.append('../pytorch-CycleGAN-and-pix2pix/')
import importlib
from models import networks

class UnetNormalized(networks.UnetGenerator):
    """
    Subclass of UnetGenerator from pix2pix that also normalizes the output (since I was getting weird results)
    """

    def __init__(self):
        super(UnetNormalized, self).__init__(3, 3, 8, 64, norm_layer=networks.get_norm_layer('batch'), use_dropout=False)

    def forward(self, x):
        x = super(UnetNormalized, self).forward(x)
        #mini = float(x.min())
        #maxi = float(x.max())
        #x.clamp_(min=mini,max=maxi)
        #x.add_(-mini).div_(maxi - mini + 1e-5)
        return x

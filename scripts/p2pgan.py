import torch
from torchvision import transforms, datasets
from netdissect.unet_normalized import UnetNormalized

def from_pth_file(filename):
    state_dict = torch.load(filename)
    model = UnetNormalized()
    model.load_state_dict(state_dict)
    model.cuda()
    return model

def get_segments_dataset(filename):
    dataset = datasets.ImageFolder(filename, transform=transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5,0.5,0.5))]))
    return dataset

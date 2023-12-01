import torch
from typing import Dict, Type
import torch.nn as nn
from model.resnet import ResNetModel
from model.unet import UNet


# Type annotations for model architecture
MODEL_ARCHITECTURE: Dict[str, Type[nn.Module]] = {
    "resnet": ResNetModel,
    'unet': UNet
}

# Type annotations for loss functions
MODEL_LOSS: Dict[str, Type[nn.Module]] = {
    "mse": nn.MSELoss,
    "mae": nn.L1Loss,
}

# Type annotations for optimizers
MODEL_OPTIMIZERS: Dict[str, Type[torch.optim.Optimizer]] = {
    "adam": torch.optim.Adam,
    "sgd": torch.optim.SGD,
    "rmsprop": torch.optim.RMSprop
}

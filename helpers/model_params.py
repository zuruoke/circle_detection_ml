from typing import Any
import torch.nn as nn
from model.resnet import ResNetModel
from model.unet import UNet


MODEL_ARCHITECTUR: dict[str, nn.Module] = {
    "resnet": ResNetModel,
    'unet': UNet
};

MODEL_LOSS = {
    "mse": ,
    "mae":
}

MODEL_OPTIMIZERS = {
    "adam",
    "sgd",
    "rmsprop"
}

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Tuple, List, Type
import numpy as np
from dataset.dataset_utils import CircleParams
from helpers.calculate_iou import iou


def predict(model: nn.Module,
            test_loader: DataLoader,
            criterion: Type[nn.Module]) -> Tuple[List[np.ndarray], float]:
    model.eval()  # Set the model to evaluation mode
    predictions = []
    total_loss = 0.0
    with torch.no_grad():  # No need to track gradients
        for images, labels in test_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            predicted_params = outputs.numpy()
            predictions.extend(predicted_params)
            total_loss += loss.item()
    return predictions, total_loss

def evaluate_model(model: nn.Module,
             test_loader: DataLoader,
             criterion: Type[nn.Module]) -> Tuple[float, float]:
    predictions, loss = predict(model, test_loader, criterion)
    ious = []
    for i, (_, true_params) in enumerate(test_loader):
        predicted_params = CircleParams(*predictions[i])
        # Ensure true_params are correctly unpacked
        true_params = CircleParams(*true_params.numpy().squeeze())
        iou_score = iou(predicted_params, true_params)
        ious.append(iou_score)
    return np.mean(ious), loss/len(test_loader)
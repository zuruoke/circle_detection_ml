import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Type
from tqdm import tqdm
from test import evaluate_model
from dataset.dataset_loader import CircleDataset

def train_model(model: nn.Module,
                train_loader: DataLoader,
                val_loader: DataLoader,
                criterion: Type[nn.Module],
                optimizer: Type[torch.optim.Optimizer],
                num_epochs: int = 100):
    for epoch in range(num_epochs):
        # Training phase
        model.train()
        running_train_loss = 0.0

        # Use tqdm for the progress bar
        train_loader_with_progress = tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs}, Training")

        for images, labels in train_loader_with_progress:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_train_loss += loss.item()
            train_loader_with_progress.set_postfix({"Training Loss": running_train_loss/len(train_loader)})

        # Validation phase
        model.eval()
        ious, val_loss = evaluate_model(model, val_loader, criterion)
        print(f"Epoch [{epoch+1}/{num_epochs}], Validation Loss: {val_loss}")
        print(f"Epoch [{epoch+1}/{num_epochs}], Average Validation IoU: {ious}")
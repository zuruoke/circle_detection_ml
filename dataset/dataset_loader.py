import torch
import numpy as np
from dataset.dataset_utils import circle_params_to_array, generate_examples
from torch.utils.data import DataLoader, Dataset

class CircleDataset(Dataset):
    def __init__(self, dataset_size=1000):
        self.images, self.labels = zip(*[next(generate_examples()) for _ in range(dataset_size)])
        self.images = torch.tensor([self.preprocess_data(img) for img in self.images], dtype=torch.float32)
        self.labels = torch.tensor([circle_params_to_array(label) for label in self.labels], dtype=torch.float32)

    @staticmethod
    def preprocess_data(img):
        return np.expand_dims(img, axis=0) / 255.0

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]
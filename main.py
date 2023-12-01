import os
import torch
from torch.utils.data import DataLoader
from args import args_parser
from dataset.dataset_loader import CircleDataset
from helpers.model_params import MODEL_ARCHITECTURE, MODEL_LOSS, MODEL_OPTIMIZERS
from train import train_model
from test import evaluate_model
from typing import Any

def load_pretrained_model(model, model_weights_loc):
    model.load_state_dict(torch.load(model_weights_loc))

def test_model(model, test_loader):
    average_iou, loss = evaluate_model(model, test_loader)
    print(f"Average IOU: {average_iou}")
    print(f"Average Loss: {loss}")

def train_and_save_model(model, train_loader, val_loader, loss_fn, optimizer, num_epochs, model_weights_loc):
    train_model(model, train_loader, val_loader, loss_fn, optimizer, num_epochs)
    torch.save(model.state_dict(), model_weights_loc)

def main() -> Any:
    args = args_parser()

    noise_level = args.noise_level
    img_shape = args.img_shape
    model_weights_loc = args.model_weight

    loss_fn_ref = MODEL_LOSS[args.loss]
    loss_fn = loss_fn_ref()

    model_ref = MODEL_ARCHITECTURE[args.model]
    model = model_ref()

    if args.mode == "test":
        print("Testing Mode...")
        load_pretrained_model(model, model_weights_loc)

        batch_size = args.test_batchsize
        dataset_size = args.test_dataset_size

        test_dataset = CircleDataset(dataset_size=dataset_size)
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

        test_model(model, test_loader)
        
    else:
        print("Training Mode...")
        num_epochs = args.epochs
        batch_size = args.train_batchsize
        optimizer_ref = MODEL_OPTIMIZERS[args.optimizer]
        optimizer = optimizer_ref(model.parameters())

        train_dataset_size = args.train_dataset_size
        val_dataset_size = 100

        train_dataset = CircleDataset(dataset_size=train_dataset_size)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

        val_dataset = CircleDataset(dataset_size=val_dataset_size)
        val_loader = DataLoader(val_dataset, batch_size=args.test_batchsize, shuffle=True)

        train_and_save_model(model, train_loader, val_loader, loss_fn, optimizer, num_epochs, model_weights_loc)

if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    main()

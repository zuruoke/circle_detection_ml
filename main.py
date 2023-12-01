import os
import torch
from test import evaluate_model
from torch.utils.data import DataLoader
from args import args_parser
from dataset.dataset_loader import CircleDataset
from helpers.model_params import MODEL_ARCHITECTURE, MODEL_LOSS, MODEL_OPTIMIZERS
from train import train_model


def main() -> any:

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
        
        model.load_state_dict(torch.load(model_weights_loc))
        
        batch_size = args.test_batchsize
        dataset_size = args.test_dataset_size
        
        test_dataset = CircleDataset(dataset_size=dataset_size) 
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        
        average_iou, loss = evaluate_model(model, test_loader)
        
        print(f"Average IOU: {average_iou}")
        print(f"Average Loss: {loss}")
        
        

    else:
        print("Training Mode...")
        num_epochs = args.epochs
        batch_size = args.train_batchsize
        optim_ref = MODEL_OPTIMIZERS[args.optimizer]
        optim = optim_ref(model.parameters())
        train_dataset_size = args.train_dataset_size
        val_dataset_size = args.train_dataset_size * 0.1
        
        train_dataset = CircleDataset(dataset_size=train_dataset_size)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        
        val_dataset = CircleDataset(dataset_size=val_dataset_size)
        val_loader = DataLoader(val_dataset, batch_size=args.test_batchsize, shuffle=True)
        
        
        
        train_model(model, train_loader, val_loader, loss_fn, optim, num_epochs)
        torch.save(model.state_dict(), model_weights_loc)


if __name__ == "__main__":
    if not os.path.exists('data'):
        os.makedirs('data')
    main()
import argparse

def args_parser():
    parser = argparse.ArgumentParser(description="Training and testing arguments")

    parser.add_argument("--mode", type=str, default="train", choices=["train", "test"], help="Mode: train or test")
    parser.add_argument("--train_batchsize", type=int, default=4, help="Training batch size")
    parser.add_argument("--test_batchsize", type=int, default=1, help="Testing batch size")
    parser.add_argument("--epochs", type=int, default=100, help="Number of training epochs")
    parser.add_argument("--train_dataset_size", type=int, default=1000, help="Size of the training dataset")
    parser.add_argument("--test_dataset_size", type=int, default=100, help="Size of the testing dataset")
    parser.add_argument("--img_shape", type=int, default=64, help="Image shape")
    parser.add_argument("--noise_level", type=float, default=0.5, help="Noise level")
    parser.add_argument("--loss", type=str, default='mse', choices=["mse", "mae", "cross_entropy"], help="Loss function")
    parser.add_argument("--optimizer", type=str, default='Adam', choices=["Adam", "SGD", "RMSProp"], help="Optimizer")
    parser.add_argument("--model", type=str, default='resnet', choices=["resnet", "unet"], help="Model architecture")
    parser.add_argument("--dropout", type=float, default=0.5, help="Dropout rate")

    args = parser.parse_args()
    return args
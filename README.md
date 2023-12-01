# Circle Detection ML

Circle Detection ML is a machine learning task designed to locate circles in images with arbitrary noise.

## Preview

This project features two custom convolutional neural network (CNN) architectures, including a variant of:

- Unet
- Resnet

Additionally, testing and training scripts are provided for training with various configurations such as model type, image size, batch size, epochs, etc. Configuration parameters can be adjusted in the `args.py` file. Efficient data loaders have been implemented to load and create the dataset.

The main entry point for the project is `main.py`.

## Installation / Setup

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone -q https://github.com/zuruoke/circle_detection_ml.git
   cd circle_detection_ml
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Training

To train the model, use the following command:

```bash
python main.py --mode train --train_batchsize 4  --epochs 100 --train_dataset_size 1000 --img_shape 64 --noise_level 0.5 --loss mse --optimizer adam --model unet --dropout 0.5 --model_weight ./data/model_weights.pth
```

## Testing

You can train your own model and load the weights or get the pretrained model weights from the following link: [Pretrained Model Weights](https://drive.google.com/file/d/1Cp41ehAGLP-ZGN2pumWB6XfOiFd3LeGK/view?usp=sharing)

Put the downloaded file in the root directory's `data` folder, which is created at the start of the project.

To test the model, use the following command:

```bash
python main.py --mode test --test_batchsize 1 --test_dataset_size 100 --img_shape 64 --noise_level 0.5 --loss mse --optimizer adam --model unet --dropout 0.5 --model_weight ./data/model_weights.pth
```

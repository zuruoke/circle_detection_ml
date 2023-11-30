import torch.nn as nn

import torch.nn.init as init

class ResNetModel(nn.Module):
    def __init__(self, n_classes=3):
        super(ResNetModel, self).__init__()

        self.dropout_percentage = 0.5
        self.relu = nn.ReLU()

        # BLOCK-1 (starting block) input=(64x64) output=(32x32)
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
        init.kaiming_normal_(self.conv1.weight, mode='fan_out', nonlinearity='relu')
        self.batchnorm1 = nn.BatchNorm2d(32)
        init.constant_(self.batchnorm1.weight, 1)
        init.constant_(self.batchnorm1.bias, 0)
        self.maxpool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

        # BLOCK-2 (1) input=(32x32) output=(32x32)
        self.conv2_1_1 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        init.kaiming_normal_(self.conv2_1_1.weight, mode='fan_out', nonlinearity='relu')
        self.batchnorm2_1_1 = nn.BatchNorm2d(32)
        init.constant_(self.batchnorm2_1_1.weight, 1)
        init.constant_(self.batchnorm2_1_1.bias, 0)
        self.conv2_1_2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        init.kaiming_normal_(self.conv2_1_2.weight, mode='fan_out', nonlinearity='relu')
        self.batchnorm2_1_2 = nn.BatchNorm2d(32)
        init.constant_(self.batchnorm2_1_2.weight, 1)
        init.constant_(self.batchnorm2_1_2.bias, 0)
        self.dropout2_1 = nn.Dropout(p=self.dropout_percentage)
        # BLOCK-2 (2)
        self.conv2_2_1 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        init.kaiming_normal_(self.conv2_2_1.weight, mode='fan_out', nonlinearity='relu')
        self.batchnorm2_2_1 = nn.BatchNorm2d(32)
        init.constant_(self.batchnorm2_2_1.weight, 1)
        init.constant_(self.batchnorm2_2_1.bias, 0)
        self.conv2_2_2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        init.kaiming_normal_(self.conv2_2_2.weight, mode='fan_out', nonlinearity='relu')
        self.batchnorm2_2_2 = nn.BatchNorm2d(32)
        init.constant_(self.batchnorm2_2_2.weight, 1)
        init.constant_(self.batchnorm2_2_2.bias, 0)
        self.dropout2_2 = nn.Dropout(p=self.dropout_percentage)

        # Final Block input=(16x16)
        self.avgpool = nn.AvgPool2d(kernel_size=(16, 16))
        self.fc = nn.Linear(in_features=32, out_features=n_classes)

        # Initialize FC layer weights and bias
        init.normal_(self.fc.weight, std=0.001)
        init.constant_(self.fc.bias, 0)


    def forward(self, x):
        # block 1 --> Starting block
        x = self.relu(self.batchnorm1(self.conv1(x)))
        op1 = self.maxpool1(x)

        # block2 - 1
        x = self.relu(self.batchnorm2_1_1(self.conv2_1_1(op1)))  # conv2_1
        x = self.batchnorm2_1_2(self.conv2_1_2(x))  # conv2_1
        x = self.dropout2_1(x)
        # block2 - 2
        x = self.relu(self.batchnorm2_2_1(self.conv2_2_1(x)))  # conv2_2
        x = self.batchnorm2_2_2(self.conv2_2_2(x))  # conv2_2
        x = self.dropout2_2(x)
        # op - block2
        op2 = self.relu(x + op1)

        # FINAL BLOCK - classifier
        x = self.avgpool(op2)
        x = x.view(x.size(0), -1)
        x = self.fc(x)

        return x

import torch
import torch.nn as nn
import torch.nn.init as init

class UNet(nn.Module):
    def __init__(self, in_channels=1, num_classes=3):
        super(UNet, self).__init__()

        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=3, padding=1),
            nn.LeakyReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.dropout = nn.Dropout(0.5)

        # Bottleneck
        self.bottleneck = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bottleneck_2 = nn.Conv2d(128, 128, kernel_size=3, padding=1, stride=2)

        # Decoder
        self.decoder = nn.Sequential(
            nn.Conv2d(128, 64, kernel_size=3, padding=1),
            nn.LeakyReLU(inplace=True),
            nn.Upsample(scale_factor=2, mode='bilinear', align_corners=False),
        )

        # Output layer
        self.out_conv = nn.Conv2d(128, num_classes, kernel_size=1, stride=4)

        # Initialize weights
        self.initialize_weights()

    def initialize_weights(self):
        for module in self.modules():
            if isinstance(module, nn.Conv2d):
                init.kaiming_normal_(module.weight, mode='fan_out', nonlinearity='leaky_relu')
                if module.bias is not None:
                    init.constant_(module.bias, 0)

    def forward(self, x):
        # Encoder
        enc = self.encoder(x)

        # Bottleneck
        bottleneck = self.bottleneck(enc)
        bottleneck_2 = self.bottleneck_2(bottleneck)
        bottleneck_2 = self.dropout(bottleneck_2)

        # Decoder with skip connection
        dec = self.decoder(bottleneck_2)
        dec_with_skip = torch.cat([enc, dec], dim=1)  # Concatenate skip connection
        final_output = self.dropout(dec_with_skip)
        final_output = self.out_conv(final_output)
        output = final_output[:, :, 0, 0]
        return output

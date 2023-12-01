from torch.utils.data import DataLoader
from dataset.dataset_loader import CircleDataset


def train_model(model, train_loader, criterion, optimizer, num_epochs=50):
    model.train()
    for epoch in range(num_epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader)}")

# Create dataset and dataloader
# dataset = CircleDataset()
# train_loader = DataLoader(dataset, batch_size=4, shuffle=True)

# # Initialize the model, loss function, and optimizer
# model = UNet(1)
# criterion = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters())

# # Train the model
# train_model(model, train_loader, criterion, optimizer)

from dataset.dataset_utils import CircleParams
import torch
import numpy as np
# test_dataset = CircleDataset(dataset_size=100)  # Adjust dataset_size as needed
# test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

def predict(model, test_loader):
    model.eval()  # Set the model to evaluation mode
    predictions = []
    with torch.no_grad():  # No need to track gradients
        for images, _ in test_loader:
            outputs = model(images)
            predicted_params = outputs.numpy()
            predictions.extend(predicted_params)
    return predictions

def test(model, test_loader, iou_func):
    predictions = predict(model, test_loader)
    ious = []
    for i, (_, true_params) in enumerate(test_loader):
        predicted_params = CircleParams(*predictions[i])
        true_params = CircleParams(*true_params.numpy().squeeze())
        iou_score = iou_func(predicted_params, true_params)
        ious.append(iou_score)
    return np.mean(ious)


# # Example usage
# average_iou = evaluate(model, test_loader, iou)
# print(f"Average IOU: {average_iou}")
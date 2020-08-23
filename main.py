from Data import Data
from model import Net
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import torch.optim as optim

if __name__ == '__main__':
    data = Data()
    featuresTrain, featuresTest, labelsTrain, labelsTest = [
        torch.from_numpy(item) for item in data.getData()
    ]
    print(featuresTrain.shape)
    net = Net(input_size=512,
              hidden_size=512,
              num_layers=1,
              num_classes=2,
              sequence_length=1)

    criterion = nn.BCELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # Pytorch train and test sets
    labelsTrain = labelsTrain.reshape(-1, 1)
    labelsTest = labelsTest.reshape(-1, 1)

    train = TensorDataset(featuresTrain, labelsTrain)
    test = TensorDataset(featuresTest, labelsTest)

    # data loader
    batch_size = 64
    trainloader = DataLoader(train, batch_size=batch_size, shuffle=False)
    testloader = DataLoader(test, batch_size=batch_size, shuffle=False)
    for epoch in range(20):  # loop over the dataset multiple times

        running_loss = 0.0

        for i, data in enumerate(trainloader):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels.to(dtype=torch.float))
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 10 == 0:  # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 100))
                running_loss = 0.0

    print('Finished Training')

    ## Test the accuracy
    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            features, labels = data
            outputs = net(features)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 random features is: %d %%' %
          (100 * correct / total))

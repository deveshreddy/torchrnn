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
    net = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # Pytorch train and test sets
    train = TensorDataset(featuresTrain, labelsTrain)
    test = TensorDataset(featuresTest, labelsTest)

    # data loader
    batch_size = 100
    trainloader = DataLoader(train, batch_size=batch_size, shuffle=False)
    testloader = DataLoader(test, batch_size=batch_size, shuffle=False)
    for epoch in range(200):  # loop over the dataset multiple times

        running_loss = 0.0

        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 200 == 0:  # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')
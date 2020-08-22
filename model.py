import torch
import torch.nn as nn
import torch.autograd as Variable
from torch.utils.data import DataLoader, TensorDataset
import torch.nn as nn

import torch.optim as optim

import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__(
            input_size,
            hidden_size,
        )
        self.rnn1 = nn.RNN(input_size=512, hidden_size=512, num_layers=2)
        self.fc1 = nn.Linear(512, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)
        self.softmax = nn.Softmax(dim=2)

    def forward(self, x):

        #print(x.size())
        #h = torch.zeros(x.size()[1], 512)
        #for i in range(x.size()):
        #   h = self.rnn1(x[i, :], h)
        for feature in x:
            feature = feature.reshape(-1, 1)
            print(feature)

            out = self.rnn1(feature)
            print(out)
            out = F.relu(self.fc1(h))
            out = F.relu(self.fc2(h))
            out = self.softmax(self.fc3(h))
        #out = self.softmax(out)
        #     x = F.relu(self.fc1(x))
        #    x = F.relu(self.fc2(x))
        #   x = self.fc3(x)
        return x
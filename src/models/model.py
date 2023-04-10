import torch.nn as nn
from config import INPUT_DIM , OUTPUT_DIM

class Network(nn.Module):
    def __init__(self) -> None:
        super(Network ,  self).__init__(INPUT_DIM , OUTPUT_DIM)
        self.l1 = nn.Linear(INPUT_DIM , 100 , nn.ReLU)
        self.l2 = nn.Linear(100 , OUTPUT_DIM , nn.Softmax)

    def forward(self , x):
        y_l1 = self.l1(x)
        y_l2 = self.l2(y_l1)

        return y_l2
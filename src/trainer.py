from src.models.model import Network
import torch
from tqdm import tqdm
from config import INPUT_DIM , OUTPUT_DIM , LEARNING_RATE , EPOCHS
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


loss_values = []
model = Network(INPUT_DIM , OUTPUT_DIM).to(device)
criterion =torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
        model.parameters(), lr=LEARNING_RATE)


def trainer( EPOCHS , model , data , target):
    model.train()
    X = torch.tensor(data , dtype=torch.float ).to(device)
    Y = torch.tensor(target , dtype=torch.float ).to(device)

    for epoch in tqdm(range(EPOCHS)):

        loss = criterion(model(X), Y)

        loss_values.append(loss.detach().item())

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()
  
        print(f"Epoch : {epoch} ===> loss is {loss.item()}")


def eval( EPOCHS , model , data_val , target_val):
    model.eval()
    X=torch.tensor(data_val , dtype=torch.float ).to(device)
    Y = torch.tensor(target_val , dtype=torch.float ).to(device)

    for epoch in tqdm(range(EPOCHS)):

        loss = criterion(model(X), Y)

        loss_values.append(loss.detach().item())
  
        print(f"Epoch : {epoch} ===> loss is {loss.item()}")



import torch
import torch.nn as nn
from skorch import NeuralNetRegressor

class LSTMRegressor(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim=6, num_layers=1):
        super(LSTMRegressor, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h, _ = self.lstm(x)
        #out = self.fc(h[:, -1, :])
        out = self.fc(h)
        return out


def create_lstm_model(input_dim, hidden_dim=50, num_layers=1, lr=0.01):

    return NeuralNetRegressor(
        module=LSTMRegressor,
        module__input_dim=input_dim,
        module__hidden_dim=hidden_dim,
        module__num_layers=num_layers,
        max_epochs=20,
        lr=lr,
        optimizer=torch.optim.Adam,
        criterion=nn.MSELoss,
        batch_size=32,
        iterator_train__shuffle=True,
        verbose=0
    )
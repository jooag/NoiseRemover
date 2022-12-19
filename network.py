from torch import nn

class NN(nn.Module):
	def __init__(self):
		super(NN, self).__init__()
		self.operation_sequence = nn.Sequential(
			nn.Linear(5, 10),
			nn.ReLU(),
			nn.Linear(10, 2)
		)

	def forward(self, x):
		result = self.operation_sequence(x)
		return result
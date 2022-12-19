from torch import nn

class NN_b(nn.Module):
	def __init__(self):
		super(NN_b, self).__init__()
		self.operation_sequence = nn.Sequential(
			nn.Linear(5, 32),
			nn.ReLU(),
			nn.Linear(32, 1)
		)

	def forward(self, x):
		result = self.operation_sequence(x)
		return result
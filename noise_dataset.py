from torch.utils.data import Dataset
from torch import Tensor
import pandas as pd

class NoiseDataset(Dataset):

    def __init__(self, csv_path:str = "data.csv", transform=None, target_transform=None):
        self.df = pd.read_csv(csv_path, index_col=False)
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        row = self.df.iloc[index]
        features=Tensor(row[0:len(row)-1])
        target=int(row[-1])
        if self.transform:
            features = self.transform(features)
        if self.target_transform:
            target = self.target_transform(target)
        return (features, target)



def main():
    ds = NoiseDataset()
    for i in range(len(ds)):
        (x, y) = ds[i]
        if len(x) != 5 or len(y) != 1:
            print("ERROR")
if __name__ == "__main__":
    main()

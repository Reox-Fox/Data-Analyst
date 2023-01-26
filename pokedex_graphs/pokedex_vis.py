import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import getcwd

data = pd.read_csv(Path(getcwd(), 'data','pokedex_basic.csv'))

if __name__ == '__main__':
    def dual_type():
        Type_2 = data['Type 2']
        dual_type_count = data['Type 2'].dropna().count()
        plt.bar(['non-dual', 'dual typed'],
        [data['Type 1'].count()-dual_type_count, dual_type_count])
        plt.show()

    def type_damage_avg():
        pass
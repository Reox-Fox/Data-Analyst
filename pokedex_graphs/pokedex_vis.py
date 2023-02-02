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
       print(data['Type 1'].unique())
       # for x in data['Type 1'].unique():
       #     z = np.average(data.loc[data['Type 1' or 'Type 2'] == x]['Attack'])
       #     print(z)

    type_damage_avg()    
    #input('''What do you want to display?
#(1) Dual Type count
#(2) Average of Damage by Type\n''')
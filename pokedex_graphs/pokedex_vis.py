import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import getcwd

data = pd.read_csv(Path(getcwd(), 'data','pokedex_basic.csv'))

if __name__ == '__main__':
    def type_count():
        uni_types = np.sort(pd.unique(data['Type 1']))
        single = data[data['Type 2'].isna()]
        dual = data[~data['Type 2'] .isna()]
        single['Type 1'].value_counts().plot(
            kind='bar', title='Single Type Pokemon by type distribution')
        plt.show()

    def dual_type():
        Type_2 = data['Type 2']
        dual_type_count = data['Type 2'].dropna().count()
        plt.bar(['non-dual', 'dual typed'],
        [data['Type 1'].count()-dual_type_count, dual_type_count])
        plt.show()

    def type_damage_avg():
        types = np.sort(pd.unique(data['Type 1']))
        dam_avg = [np.around(np.average(
            data.loc[data['Type 1' or 'Type 2'] == x]['Attack']))
        for x in types]
        plt.bar(types, dam_avg)
        plt.show()

    type_count()    
#    input('''What do you want to display?
#(1) Dual Type count
#(2) Average of Damage by Type\n''')
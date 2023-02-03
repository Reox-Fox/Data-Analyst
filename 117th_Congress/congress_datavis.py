import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import getcwd


if __name__ == '__main__':
    data = pd.read_csv(Path(getcwd(),'data','congress.csv'))
    z = np.arange(5, 26, 5)

    def age_distribution():
        age = data['Age'].dropna()
        republican = data.loc[data.Party == 'Republican'].Age
        democrat = data.loc[data.Party == 'Democrat'].Age
        other = data.loc[(data.Party != 'Republican') &
            (data.Party != 'Democrat')]
        quartiles = np.quantile(age, [.25, .5, .75])

        plt.bar(age.unique(), age.value_counts(), zorder=z[-2])
        plt.xticks(np.arange(25, 89, 3))
        plt.yticks(np.arange(2, 23, 2))
        
        for x in np.arange(2,23,2):
            plt.axhline(x, zorder=z[0], color='0.9')
        for x in quartiles:
            plt.axvline(x, zorder=z[-1], color='r', ls='--')
        plt.axvline(quartiles[1], ls='--', c='r', label='Quartiles')
        plt.legend()
        
        plt.title('Age Representation in the 117th Congress', fontsize='xx-large')
        plt.xlabel('Age of Members', fontsize='x-large')
        plt.ylabel('Total Members', fontsize='x-large')
        #plt.show()
        print(other)
        
    age_distribution()
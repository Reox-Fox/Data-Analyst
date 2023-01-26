import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from os import getcwd


if __name__ == '__main__':
    data = pd.read_csv(Path(getcwd(),'data','congress.csv'))

    age = data['Age'].dropna()
    unique_age = np.sort(age.unique())
    age_count = [age.value_counts()[x] for x in unique_age]
    age_quartiles = []
    age_quartiles = np.quantile(age,[.25,.5,.75])

    parties = data['Party']
    unique_parties = parties.unique()
    party_count = [parties.value_counts()[x] for x in unique_parties]
    party_count = {k:v for (k,v) in zip(unique_parties, party_count)}


    terms = data['Number of Terms'].dropna()
    unique_terms = np.sort(terms.unique())
    terms_count = [terms.value_counts()[x] for x in unique_terms]


    def age_distribution():
        plt.bar(unique_age,age_count, zorder=5, label='congress age distribution')

        plt.xlabel('Age of Congress')
        plt.xticks(np.arange(25,91,5))

        plt.ylabel('Number of people')
        plt.yticks(np.arange(0,24,2))
    
        plt.axvline(age_quartiles[0], color='r', zorder=10, label="Quartiles")
        for x in age_quartiles[1:]:
            plt.axvline(x, color='r', zorder=10)

        plt.legend()
        plt.show()

    option = input('Which graph do you want to see?\n(1) Age Distribution\n(2) Age by Party\n')
    if option == '1':
        print(max(age_count))
        age_distribution()

    if option == '2':
        #age_pie()
        pass
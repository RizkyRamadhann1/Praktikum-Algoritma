# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:18:52 2022

@author: Rizky Ramadhan
"""

import pandas as p

data = p.read_csv("Negara.csv")

df=p.DataFrame(data)
m= df.groupby(["Benua"]).mean()
s=df.groupby(["Benua"]).std()

m.to_csv('NegaraMean.csv')
s.to_csv("NegaraStandarDeviasi.csv")

print(df)
print(m)
print(s)
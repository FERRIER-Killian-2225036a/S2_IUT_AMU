#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:37:07 2023

@author: user
"""

import pandas
import matplotlib.pyplot as plt

CSV = pandas.read_csv("./owid-covid-data-FRA.csv")

## # Part1 :
"""
print("Exo 2 :")
Exo2 = CSV["new_cases"]
print(Exo2.head(8))

print("Exo 3 :")
Exo3 = CSV.loc[CSV["date"]=="2021-02-01"]
print(Exo3.head(8))

print("Exo 4 :")
print(CSV["hosp_patients"].describe())

print("Exo 5 :")
Exo5 = CSV.loc[CSV["date"]<"2022-01-01"]
Exo5 = Exo5.loc[CSV["date"]>"2020-12-31"]
print(Exo5["hosp_patients"].describe())

print("Exo 6 :")
Exo6 = CSV.loc[CSV["date"]<"2022-01-01"]
Exo6 = Exo6.loc[CSV["date"]>"2020-12-31"]
SerierStat = Exo6["hosp_patients"].describe()
SerierStat.plot.box(whis=[0,100],vert=False)
plt.title("Diagramme en boite de patients hospitalisé")
plt.show()

print("Exo 7 :\n", CSV["new_cases_smoothed"].plot())

print("Exo 8 :")
CSV.loc[CSV["date"]<"2021-11-30"].plot(x="date",y=["new_cases_smoothed","hosp_patients","icu_patients"],secondary_y="icu_patients")

print("Exo 9 :")
Exo9 = CSV.loc[CSV["date"]>="2021-11-01"]
Exo9 = Exo9.loc[CSV["date"]<="2021-12-15"]
Exo9.plot.bar(x="date",y=["new_cases_smoothed","hosp_patients"])

print("Exo 10:")
Exo9 = CSV.loc[CSV["date"]>="2021-11-01"]
Exo9 = Exo9.loc[CSV["date"]<="2021-12-15"]
Exo9.plot.bar(x="date",y=["new_cases_smoothed","hosp_patients","icu_patients"], subplots=True)
"""





















































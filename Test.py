import os
import pandas as pd

files = os.listdir("Innføring ingeniørfag\Power Usage\Power-Usage\data")

               
selceted = int(input("Choose date: 1 = Nov 2020, 2 = Des 2020, 3 = Jan 2021: "))
print(files[selceted-1])

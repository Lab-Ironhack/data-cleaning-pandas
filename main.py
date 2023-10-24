import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir("C:/Users/gdcma/Ironhack/Projects/data-cleaning-pandas/")
import src.cleaning as clean
import src.visualization as visual

clean.cleaningTotal("../attacks.csv")
visual.visualSex("data/df_projectI.csv")
visual.visualHistory("data/df_projectI.csv")
visual.visualDeathSex("data/df_projectI.csv")
visual.kids("data/df_projectI.csv")
visual.lunch("data/df_projectI.csv")
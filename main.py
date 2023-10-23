import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.chdir("C:/Users/gdcma/Ironhack/Projects/Project-I/")
from src.cleaning import cleaningTotal
from src.visualization import visualSex
from src.visualization import visualHistory
from src.visualization import visualDeathSex
from src.visualization import kids
from src.visualization import lunch
from src.visualization import visualSex

cleaningTotal("../attacks.csv")
visualSex("data/df_projectI.csv")
visualHistory("data/df_projectI.csv")
visualDeathSex("data/df_projectI.csv")
kids("data/df_projectI.csv")
lunch("data/df_projectI.csv")
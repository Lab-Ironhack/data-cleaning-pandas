import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir("C:/Users/gdcma/Ironhack/Projects/data-cleaning-pandas/")

# Shark related attacks according to sex
def visualSex(path):
    df = pd.read_csv(path)
    # Total attacks in F and M
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    plt.figure()
    sex_gral = sns.countplot(x=df["Sex"])
    sex_gral.set(title = "Total attacks in men and women")
    sex_gral.bar_label(sex_gral.containers[0])
    sex_gral.figure.savefig("images/sex_gral.jpg", dpi=1000);
    # % attacks in F and M
    plt.figure()
    sex_percentage = df["Sex"].value_counts().plot.pie(autopct="%.1f%%")
    sex_percentage.set(title = "Percentage of attacks in men and women")
    sex_percentage.figure.savefig("images/sex_percentage.jpg", dpi=1000);
    # Attacks from 1880 in M and F
    df_history = df[df["Year"] > 1880]
    plt.figure()
    sex_history1880 = sns.histplot(data=df_history, x="Year", hue="Sex", multiple="stack")
    sex_history1880.set(title = "Attacks in men and women from 1880")
    sex_history1880.figure.savefig("images/sex_history1880.jpg", dpi=1000)
    # Open images:
    os.startfile("images/sex_percentage.jpg")
    os.startfile("images/sex_gral.jpg")
    os.startfile("images/sex_history1880.jpg")

def visualHistory(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    # Attacks throughout history
    plt.figure()
    history = sns.boxplot(x = "Year", data = df); # There is not much information about shark attacks previous to 1880
    history.set(title = "Total attacks throughout time")
    history.figure.savefig("images/history.jpg", dpi=1000);
    # Attacks from 1880
    df_history = df[df["Year"] > 1880]
    plt.figure()
    history1880 = sns.histplot(data=df_history, x="Year")
    history1880.set(title = "Total attacks throughout time from 1880")
    history1880.figure.savefig("images/history1880.jpg", dpi=1000);
    # Deaths from 1880
    plt.figure()
    fatal_history1880 = sns.histplot(data=df_history.loc[df_history["Fatal"] == "Y"], x="Year");
    fatal_history1880.figure.savefig("images/fatal_history1880.jpg", dpi=1000)
    # Open images:
    os.startfile("images/history.jpg")
    os.startfile("images/history1880.jpg")
    os.startfile("images/fatal_history1880.jpg")

# Shark related deaths according to sex
def visualDeathSex(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    # Percentage of attacks that are deadly
    plt.figure()
    deaths = df["Fatal"].value_counts().plot.pie(autopct="%.1f%%");
    deaths.set(title = "Percentage of fatal events")
    deaths.figure.savefig("images/deaths.jpg", dpi=1000);
    # Percentage of attacks that are deadly depending on sex
    df_F = df[df["Sex"] == "F"]
    df_M = df[df["Sex"] == "M"]
    plt.figure()
    fatal_Fem = df_F["Fatal"].value_counts().plot.pie(autopct="%.1f%%");
    fatal_Fem.set(title = "Percentage of deadly attacks in women")
    fatal_Fem.figure.savefig("images/fatal_Fem.jpg", dpi=1000)
    plt.figure()
    fatal_Men = df_M["Fatal"].value_counts().plot.pie(autopct="%.1f%%");
    fatal_Men.set(title = "Percentage of deadly attacks in men")
    fatal_Men.figure.savefig("images/fatal_Men.jpg", dpi=1000)
        # Apparently, men die more from shark attacks than women after suffering an attack
    # Deaths from 1880 in M and F
    df_history = df[df["Year"] > 1880]
    plt.figure()
    fatal_Sexhistory1880 = sns.histplot(data=df_history.loc[df_history["Fatal"] == "Y"], x="Year", hue="Sex", multiple="stack");
    fatal_Sexhistory1880.set(title = "Deaths in men and women throughout time")
    fatal_Sexhistory1880.figure.savefig("images/fatal_Sexhistory1880.jpg", dpi=1000)
    # Open images:
    os.startfile("images/fatal_Fem.jpg")
    os.startfile("images/fatal_Men.jpg")
    os.startfile("images/fatal_Sexhistory1880.jpg")

# Shark related child deaths according to sex throughout history
def kids(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    mask_kids = pd.DataFrame(df.loc[(df["Age"] < 13)])
    mask_kidsfatal = pd.DataFrame(df.loc[(df["Age"] < 13) & (df["Fatal"] == "Y")])
    # Attacks to kids throughout history
    plt.figure()
    kid_attacks = sns.histplot(data=mask_kids, x="Year");
    kid_attacks.set(title = "Attacks suffered by children throughout time")
    kid_attacks.figure.savefig("images/kid_attacks.jpg", dpi=1000)
    # Attacks to kids throughout history according to sex
    plt.figure()
    sexkid_attacks = sns.histplot(data=mask_kids, x="Year", hue="Sex", multiple="stack");
    sexkid_attacks.set(title = "Attacks suffered by boys and girls throughout time")    
    sexkid_attacks.figure.savefig("images/sexkid_attacks.jpg", dpi=1000)
    # Deaths of kids throughout history
    plt.figure()
    kid_deaths = sns.histplot(data=mask_kidsfatal, x="Year");
    kid_deaths.set(title = "Deaths of children throughout time")    
    kid_deaths.figure.savefig("images/kid_deaths.jpg", dpi=1000)
    # Deaths of kids throughout history according to sex
    plt.figure()
    sexkid_deaths = sns.histplot(data=mask_kidsfatal, x="Year", hue="Sex", multiple="stack");
    sexkid_deaths.set(title = "Deaths of boys and girls throughout time")
    sexkid_deaths.figure.savefig("images/sexkid_deaths.jpg", dpi=1000)
    #Age of the deaths throughout history
    plt.figure()
    agekid_deaths = sns.lineplot(data=mask_kidsfatal, x="Year", y="Age");
    agekid_deaths.set(title = "Age of deaths of children throughout time")
    agekid_deaths.figure.savefig("images/agekid_deaths.jpg", dpi=1000)
    plt.figure()
    scatteredagekid_deaths = sns.scatterplot(data=mask_kidsfatal, x="Year", y ="Age"); #Not clear, recategorise the Age
    scatteredagekid_deaths.figure.savefig("images/scatteredagekid_deaths.jpg", dpi=1000)
    # Recateg age of kids
    mask_toddler = (mask_kids["Age"] < 3)
    mask_preschool = (mask_kids["Age"] >= 3) & (mask_kids["Age"] < 6)
    mask_school = (mask_kids["Age"] >= 6) & (mask_kids["Age"] < 12)
    mask_kids.loc[mask_toddler, "Age_categ"] = "Toddler"
    mask_kids.loc[mask_preschool, "Age_categ"] = "Preschooler"
    mask_kids.loc[mask_school, "Age_categ"] = "School-aged"
    mask_fataltoddler = (mask_kidsfatal["Age"] < 3)
    mask_fatalpreschool = (mask_kidsfatal["Age"] >= 3) & (mask_kidsfatal["Age"] < 6)
    mask_fatalschool = (mask_kidsfatal["Age"] >= 6) & (mask_kidsfatal["Age"] < 12)
    mask_kidsfatal.loc[mask_fataltoddler, "Age_categ"] = "Toddler"
    mask_kidsfatal.loc[mask_fatalpreschool, "Age_categ"] = "Preschooler"
    mask_kidsfatal.loc[mask_fatalschool, "Age_categ"] = "School-aged"
    # Category of age of the attacks throughout history
    plt.figure()
    agekid_attacks = sns.histplot(data=mask_kids, x="Year", hue = "Age_categ", multiple="stack");
    agekid_attacks.set(title = "Attacks by age category of children throughout time")
    agekid_attacks.figure.savefig("images/agekid_attacks.jpg", dpi=1000)
    # Category of age of the deaths throughout history
    plt.figure()
    agecategkid_deaths = sns.histplot(data=mask_kidsfatal, x="Year", hue = "Age_categ", multiple="stack");
    agecategkid_deaths.figure.savefig("images/agecategkid_deaths.jpg", dpi=1000)
    # Open images:
    os.startfile("images/kid_attacks.jpg")
    os.startfile("images/sexkid_attacks.jpg")
    os.startfile("images/kid_deaths.jpg")
    os.startfile("images/sexkid_deaths.jpg")
    os.startfile("images/agekid_deaths.jpg")
    os.startfile("images/scatteredagekid_deaths.jpg")
    os.startfile("images/agekid_attacks.jpg")
    os.startfile("images/agecategkid_deaths.jpg")

# Shark's favourite food
def lunch(path):
    df = pd.read_csv(path)
    sns.set(rc={"figure.figsize": (5, 4)}, font_scale=0.75)
    sns.set_style("white")
    # Moment of day sharks attack the most
    plt.figure()
    lunch = df["Moment"].value_counts().plot.pie(autopct="%.1f%%"); # NaN: 1918; and not NaN: 2895
    lunch.set(title = "Percentage of attacks by moment of day");
    lunch.figure.savefig("images/lunch.jpg", dpi=1000)
    # Moment of day sharks attack the most according to sex
    plt.figure()
    sex_lunch = sns.countplot(x=df["Moment"], hue=df["Sex"], palette="magma");
    sex_lunch.set(title = "Moment of day sharks attack the most according to sex");
    sex_lunch.figure.savefig("images/sex_lunch.jpg", dpi=1000)
    # Open images:
    os.startfile("images/lunch.jpg")
    os.startfile("images/sex_lunch.jpg")
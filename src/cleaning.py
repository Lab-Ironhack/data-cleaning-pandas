import pandas as pd

def csvTrabajo(path):
    df = pd.read_csv(path, encoding="unicode_escape")
    return df[["Year", "Sex ", "Fatal (Y/N)", "Age", "Time"]]

df = csvTrabajo("C:/Users/gdcma/Ironhack/Projects/attacks.csv")

#DUPLICATES AND NAN
def duplicates(df):
    '''Deletes rows if they are repeated, and prints the resulted shape and NaN for each column'''
    df.drop_duplicates(inplace = True)
    print(f"There are {df.shape[0]} unique subjects")
        # There are 4783 unique subjects
    print(f"There are {df.isna().sum().iloc[0]} NaN values in {df.columns[0]}\nThere are {df.isna().sum().iloc[1]} NaN values in {df.columns[1]}\nThere are {df.isna().sum().iloc[2]} NaN values in {df.columns[2]}\nThere are {df.isna().sum().iloc[3]} NaN values in {df.columns[3]}\nThere are {df.isna().sum().iloc[4]} NaN values in {df.columns[4]}")
        # There are 3 NaN values in Year
        # There are 377 NaN values in Sex 
        # There are 460 NaN values in Fatal (Y/N)
        # There are 1397 NaN values in Age
        # There are 1885 NaN values in Time

#Variable Year
def cleanYear(df):
    '''If Year is 0 or less than 1000, reassigns to NaN'''
    df.loc[df["Year"][df["Year"] == 0].index, "Year"] = float('nan')
    df.loc[df["Year"][df["Year"] < 1000].index, "Year"] = float('nan')

#Variable Sex
def cleanSex(df):
    '''Categorises Sex to F (female) and M (male), and prints the number of NaN in Sex, in case there are few and can be imputed'''
    df.rename({"Sex ":"Sex"}, axis = 1, inplace = True)
    df.loc[df["Sex"][df["Sex"] == "M "].index, "Sex"] = "M"
    df.loc[df["Sex"][(df["Sex"] == "N") | (df["Sex"] == "lli") | (df["Sex"] == ".")].index, "Sex"] = float('nan')
    print(f"There are {df['Sex'].isna().sum()} NaN values in Sex.")
    
#Variable Fatal (Y/N)
def cleanFatal(df):
    '''Categorises Fatal to Y (yes) and N (no), and prints the number of NaN in Fatal, in case there are few and can be imputed'''
    df.rename({"Fatal (Y/N)":"Fatal"}, axis = 1, inplace = True)
    df.loc[df["Fatal"][(df["Fatal"] == " N") | (df["Fatal"] == "N ") | (df["Fatal"] == "M")].index, "Fatal"] = "N"
    df.loc[df["Fatal"][df["Fatal"] == "y"].index, "Fatal"] = "Y"
    df.loc[df["Fatal"][(df["Fatal"] == "2017") | (df["Fatal"] == "UNKNOWN")].index, "Fatal"] = float('nan')
    print(f"{df['Fatal'].isna().sum()} NaN values in Fatal")

#Variable Age: too many issues
def cleanAge(df):
    '''Assigns new values to Age if they are not translatable to a number'''
    # Extract numbers from strings such as 40s or 40's
    df["col1"] = df["Age"].str.extract("(\d{1,2})'?s")
    df["col1"] = pd.to_numeric(df["col1"]) + 5
    df["col1"] = df["col1"].astype("object")
    df.loc[df["col1"][df["col1"].notna()].index, "Age"] = df.loc[df["col1"][df["col1"].notna()].index, "col1"]
    df.drop(["col1"], axis = 1, inplace = True)
    # Teens are 15 years old
    df.loc[df["Age"][(df["Age"] == "Teen") | (df["Age"] == "teen") | (df["Age"] == "Teens")].index, "Age"] = "15"
    # Wrong observations are NaN
    df.loc[df["Age"][(df["Age"] == "N") | (df["Age"] == " ") | (df["Age"] == "\xa0 ") | (df["Age"] == "X") | 
                     (df["Age"] == "MAKE LINE GREEN") | (df["Age"] == "F") | (df["Age"] == "  ") | (df["Age"] == "A.M.") |
                     (df["Age"] == "Y")].index, "Age"] = float('nan')
    # 18 moths is 1 year:
    df.loc[df["Age"][df["Age"] == "18 months"].index, "Age"] = "1"
    # 6½ is 6
    df.loc[df["Age"][df["Age"] == "6½"].index, "Age"] = "6"
    # 20? is 20
    df.loc[df["Age"][(df["Age"] == "20?") | (df["Age"] == "18 to 22")].index, "Age"] = "20"
    # 16 to 18 is 17
    df.loc[df["Age"][df["Age"] == "16 to 18"].index, "Age"] = "17"
    # Elderly is 70
    df.loc[df["Age"][df["Age"] == "Elderly"].index, "Age"] = "70"
    # Ca. 33 is 33
    df.loc[df["Age"][df["Age"] == "Ca. 33"].index, "Age"] = "33"
    # >50 is 55
    df.loc[df["Age"][df["Age"] == ">50"].index, "Age"] = "55"
    # adult is 35
    df.loc[df["Age"][(df["Age"] == "adult") | (df["Age"] == "(adult)")].index, "Age"] = "35"
    # 9 months and 2 to 3 months is 0:
    df.loc[df["Age"][(df["Age"] == "9 months") | (df["Age"] == "2 to 3 months")].index, "Age"] = "0"
    # 25 to 35 is 30
    df.loc[df["Age"][df["Age"] == "25 to 35"].index, "Age"] = "30"
    # middle-age is 50
    df.loc[df["Age"][df["Age"] == '"middle-age"'].index, "Age"] = "50"
    # young is 25
    df.loc[df["Age"][(df["Age"] == '"young"') | (df["Age"] == "young")].index, "Age"] = "25"
    # 2½ is 2
    df.loc[df["Age"][df["Age"] == "2½"].index, "Age"] = "2"
    # One age or the other, is the upper mean
    df.loc[df["Age"][df["Age"] == "18 or 20"].index, "Age"] = "19"
    df.loc[df["Age"][df["Age"] == "12 or 13"].index, "Age"] = "13"
    df.loc[df["Age"][df["Age"] == "8 or 10"].index, "Age"] = "9"
    df.loc[df["Age"][df["Age"] == "30 or 36"].index, "Age"] = "33"
    df.loc[df["Age"][df["Age"] == "33 or 37"].index, "Age"] = "35"
    df.loc[df["Age"][df["Age"] == "21 or 26"].index, "Age"] = "24"
    df.loc[df["Age"][df["Age"] == "25 or 28"].index, "Age"] = "27"
    df.loc[df["Age"][df["Age"] == "13 or 18"].index, "Age"] = "26"
    df.loc[df["Age"][df["Age"] == "7 or 8"].index, "Age"] = "8"
    df.loc[df["Age"][df["Age"] == "9 or 10"].index, "Age"] = "10"
    df.loc[df["Age"][df["Age"] == "10 or 12"].index, "Age"] = "11"
    df.loc[df["Age"][df["Age"] == "31 or 33"].index, "Age"] = "32"
    df.loc[df["Age"][df["Age"] == "13 or 14"].index, "Age"] = "14"
    # One age and the other, is both. Duplicate rows and assign one value of age to each
    df.loc[10000] = df.loc[698].copy() # "28 & 26"
    df.loc[698, "Age"] = "28"
    df.loc[10000, "Age"] = "26"
    df.loc[10001] = df.loc[1506].copy() # "46 & 34"
    df.loc[1506, "Age"] = "46"
    df.loc[10001, "Age"] = "34"
    df.loc[10002] = df.loc[1508].copy() # "28, 23 & 30"
    df.loc[10003] = df.loc[1508].copy() # "28, 23 & 30"
    df.loc[1508, "Age"] = "28"
    df.loc[10002, "Age"] = "23"
    df.loc[10003, "Age"] = "30"
    df.loc[10004] = df.loc[1743].copy() # "36 & 26"
    df.loc[1743, "Age"] = "36"
    df.loc[10004, "Age"] = "26"
    df.loc[10005] = df.loc[1925].copy() # "21 & ?"
    df.loc[1925, "Age"] = "21"
    df.loc[10005, "Age"] = float('nan')
    df.loc[10006] = df.loc[2026].copy() # "23 & 20"
    df.loc[2026, "Age"] = "23"
    df.loc[10006, "Age"] = "20"
    df.loc[10007] = df.loc[2422].copy() #"7      &    31"
    df.loc[2422, "Age"] = "7"
    df.loc[10007, "Age"] = "31"
    df.loc[10008] = df.loc[2511].copy() # "32 & 30"
    df.loc[2511, "Age"] = "32"
    df.loc[10008, "Age"] = "30"
    df.loc[10009] = df.loc[3459].copy() # "9 & 12"
    df.loc[3459, "Age"] = "9"
    df.loc[10009, "Age"] = "12"
    df.loc[10010] = df.loc[3517].copy() # "? & 19"
    df.loc[3517, "Age"] = float('nan')
    df.loc[10010, "Age"] = "19"
    df.loc[10011] = df.loc[3742].copy() # "23 & 26"
    df.loc[3742, "Age"] = "23"
    df.loc[10011, "Age"] = "26"
    df.loc[10012] = df.loc[3880].copy() # "33 & 37"
    df.loc[3880, "Age"] = "33"
    df.loc[10012, "Age"] = "37"
    df.loc[10013] = df.loc[3986].copy() # "37, 67, 35, 27,  ? & 27"
    df.loc[10014] = df.loc[3986].copy() # "37, 67, 35, 27,  ? & 27"
    df.loc[10015] = df.loc[3986].copy() # "37, 67, 35, 27,  ? & 27"
    df.loc[10016] = df.loc[3986].copy() # "37, 67, 35, 27,  ? & 27"
    df.loc[10017] = df.loc[3986].copy() # "37, 67, 35, 27,  ? & 27"
    df.loc[3986, "Age"] = "37"
    df.loc[10013, "Age"] = "67"
    df.loc[10014, "Age"] = "35"
    df.loc[10015, "Age"] = "27"
    df.loc[10016, "Age"] = float('nan')
    df.loc[10017, "Age"] = "27"
    df.loc[10018] = df.loc[3998].copy() # "21, 34,24 & 35"
    df.loc[10019] = df.loc[3998].copy() # "21, 34,24 & 35"
    df.loc[10020] = df.loc[3998].copy() # "21, 34,24 & 35"
    df.loc[3998, "Age"] = "21"
    df.loc[10018, "Age"] = "34"
    df.loc[10019, "Age"] = "24"
    df.loc[10020, "Age"] = "35"
    df.loc[10021] = df.loc[4009].copy() # "30 & 32"
    df.loc[4009, "Age"] = "30"
    df.loc[10021, "Age"] = "32"
    df.loc[10022] = df.loc[4035].copy() # "50 & 30"
    df.loc[4035, "Age"] = "50"
    df.loc[10022, "Age"] = "30"
    df.loc[10023] = df.loc[4039].copy() # "17 & 35"
    df.loc[4039, "Age"] = "17"
    df.loc[10023, "Age"] = "35"
    df.loc[10024] = df.loc[4078].copy() # "34 & 19"
    df.loc[4078, "Age"] = "34"
    df.loc[10024, "Age"] = "19"
    df.loc[10025] = df.loc[4118].copy() # "33 & 26"
    df.loc[4118, "Age"] = "33"
    df.loc[10025, "Age"] = "26"
    df.loc[10026] = df.loc[4587].copy() # "17 & 16"
    df.loc[4587, "Age"] = "17"
    df.loc[10026, "Age"] = "16"
    df.loc[10027] = df.loc[4801].copy() # "Both 11"
    df.loc[4801, "Age"] = "11"
    df.loc[10027, "Age"] = "11"
    df.loc[10028] = df.loc[4999].copy() # "36 & 23"
    df.loc[4999, "Age"] = "36"
    df.loc[10028, "Age"] = "23"
    df.loc[10029] = df.loc[5181].copy() # "?    &   14"
    df.loc[5181, "Age"] = float('nan')
    df.loc[10029, "Age"] = "14"
    # Convert to number:
    df["Age"] = pd.to_numeric(df["Age"])
    print(f"{df['Age'].isna().sum()} NaN values in Fatal")

#Variable Time:
def cleanTime(df):
    '''Substitutes the Time variable with a new one called Moment, with the categories Morning, Afternoon, Evening and Night'''
    df["col1"] = df["Time"].str.extract("(\d{1,2})")
    df["col1"] = pd.to_numeric(df["col1"])
    
    # Morning
    mask = (df["col1"] >= 6) & (df["col1"] < 12)
    df.loc[mask, "col2"] = "Morning"
    mask = (df["Time"].str.contains("orning", na=False, regex=False)) | (df["Time"].str.contains("A.?M", na = False)) | (df["Time"].str.contains("b?efore noon", na = False)) | (df["Time"] == "Dawn") | (df["Time"] == "Daybreak") | (df["Time"] == "Daytime")
    df.loc[mask, "col2"] = "Morning"
    #Afternoon
    mask = (df["col1"] >= 12) & (df["col1"] < 18)
    df.loc[mask, "col2"] = "Afternoon"
    mask = (df["Time"].str.contains("fternoon", na=False, regex=False)) | (df["Time"].str.contains("fter\s?[nl]", na = False)) | (df["Time"].str.contains("Noon", na = False, regex = False)) | (df["Time"].str.contains("P.?M", na=False)) | (df["Time"].str.contains("Midday", na = False, regex = False)) | (df["Time"].str.contains("luncht?", na=False)) | (df["Time"].str.contains("Luncht?", na=False))
    df.loc[mask, "col2"] = "Afternoon"
    # Evening
    mask = (df["col1"] >= 18)
    df.loc[mask, "col2"] = "Evening"
    mask = (df["Time"].str.contains("vening", na=False, regex=False)) | (df["Time"].str.contains("sundown")) | (df["Time"].str.contains("before dusk", na=False, regex=False))
    df.loc[mask, "col2"] = "Evening"
    # Night
    mask = (df["col1"] < 6)
    df.loc[mask, "col2"] = "Night"
    mask = (df["Time"].str.contains("ight", na=False, regex=False)) | (df["Time"].str.contains("dark", na=False, regex=False)) | (df["Time"] == "Dark") | (df["Time"].str.contains("before dawn", na=False, regex=False)) | (df["Time"] == "sunset") | (df["Time"] == "Sunset") | (df["Time"].str.contains("dusk", na=False, regex=False)) | (df["Time"].str.contains("Dusk", na = False, regex=False)) | (df["Time"] == "Before daybreak")
    df.loc[mask, "col2"] = "Night"
    # NaN
    mask = (df["Time"] == "--") | (df["Time"] == "X")
    df.loc[mask, "col2"] = float('nan')
     
    df.rename({"col2":"Moment"}, axis=1, inplace=True)
    df.drop(["col1"], axis = 1, inplace = True)
    df.drop(["Time"], axis = 1 , inplace = True)
    
    print(f"{df['Moment'].isna().sum()} NaN values in Moment of the day")


def cleaningTotal(path):
    '''Deletes duplicates and cleans the variables of interest. Returns a new dataframe ready to analyse'''
    df = csvTrabajo(path)
    duplicates(df)
    cleanYear(df)
    cleanSex(df)
    cleanFatal(df)
    cleanAge(df)
    cleanTime(df)
    df.to_csv("C:/Users/gdcma/Ironhack/Projects/Project-I/data/df_projectI.csv", index=False)


cleaningTotal("C:/Users/gdcma/Ironhack/Projects/attacks.csv")
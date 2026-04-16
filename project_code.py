import pandas as pd

heart_data = pd.read_csv('heart.csv')

# This data is separated into some categories
# Age 
# Sex M/F
# Chest Pain type:
    # TA: Typical Angina
    # ATA: Atypical Angina
    # NAP: Non-Anginal Pain
    # ASY: Asymptomatic
# Resting BP
# Cholestrol as mm/dl
# Fasting Blood Sugar
# Resting ECG
    # Normal
    # ST: These are ST-T wave abnormalities
    # LVH: Left Ventricular Hypertrophy
# Max HR
# Exercise Induced Angina (Y, N)
# Oldpeak: Oldpeak is ST as a Numeric Value but depression
# ST_slope: This is the slope of the ST segment
    #Upsloping, Flag, Downsloping
# Heart Disease [1-Has, 0-Doesn't have]

# This is just how we load the data, and view the dimensions.
# 
print(heart_data.head())
print(heart_data.info())
print(heart_data.describe())



# Handle Data. We need to get it to proper 0/1 values, and then normalize
# Stuff like bp are probably going to have a pretty significant weight



# Heart Map
# This will give us a good idea as to which categories are going to have
# the most influence. 


# Lin Reg


# Neural Network


# Graphs/Etc


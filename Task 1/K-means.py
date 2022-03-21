
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('minute_weather.csv')
data.head()

data = data.loc[:, ['air_temp', 'relative_humidity']]
data.head(2)



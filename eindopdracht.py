import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import preprocessing,ensemble
from sklearn import metrics
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

st.title("PROJECT SMART AQUAPONICS")

st.write(
  pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })
)

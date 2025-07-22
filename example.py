import warnings
import numpy as ny
import pandas as pd
import streamlit as st 

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning)

file = pd.read_csv("C:/Users/Admin/Desktop/AI/My_Projects/Dataset/college_student_placement_dataset.csv")


print(file.head())
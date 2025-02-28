import pandas as pd
import matplotlib.pyplot as plt 

def OutlierDetection(df):
  clean_df=df.copy()
#   outliers=pd.DataFrame()
  for col in clean_df.columns:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR=Q3-Q1
    lower=Q1-1.5*IQR
    upper=Q3+1.5*IQR
    mask=(df[col] >= lower) & (df[col]<=upper)
    outliers=(df[col]<= lower) & (df[col] >= upper)
    clean_df=clean_df[mask]
    return clean_df
    # return outliers
    
    
def boxplotter (df):
    fig, ax=plt.subplots(nrows=len(df), ncols=1, figsize=(8, len(df)))
    for ax, col in zip(df, ax):
        ax.boxplot(df[col])
        ax.set_title(f'Boxplot for {col}')
        ax.set_xlabel('Data')
        ax.set_ylabel('Values')
    plt.tight_layout()
    plt.show()
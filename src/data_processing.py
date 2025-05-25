import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
def load_data(file_path):
    """
    Load dataset from a CSV file.
    """
    return pd.read_csv(file_path)


def process_strain_field(file_path, rolling_window, endpoint,max_centre_strain):
    df = pd.read_excel(file_path, index_col=0)
    
    # Replace placeholder with NaNs (GOM uses ??? instead of nan)
    df = df.replace('???', np.nan)

    # Initial interpolation and fill missing values
    df = df.interpolate(method='linear', limit_direction='forward', axis=0)
    df = df.fillna(method='ffill')

    # Expand columns to flexible endpoints range at intervals of 0.5
    desired_cols = np.arange(-endpoint, endpoint + 0.5, 0.5)
    for col in desired_cols:
        if col not in df.columns:
            df[col] = np.nan

    df = df[desired_cols]  # Reorder columns

    # Remove negatives and set boundary conditions
    df[df < 0] = 0
    df.iloc[0] = 0


    # Polynomial interpolation horizontally (across columns) optional
    #df = df.interpolate(method='polynomial', order=2, axis=1, limit_direction='forward')

    # Rolling mean smoothing vertically (across rows)
    df = df.rolling(rolling_window, min_periods=2).mean()

    # Post-processing cleanup
    df.iloc[0] = 0
    df[df < 0] = 0
    #uncomment if you want zero endpoints
    #df[endpoint] = 0
    #df[-endpoint] = 0
    
    if max_centre_strain is not None:
        crossing_idx = df.index[df[0] >= max_centre_strain]
        if len(crossing_idx) > 0:
            df = df.loc[:crossing_idx[0]]    # Identify the row closest to the specified center strain change from 1 if you like


    # Plot strain values at the specified column and entire strain field at center strain ~ 1
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    axs[0].plot(df[0])
    axs[0].set_xlabel('Row Index')
    axs[0].set_ylabel('Strain')
    axs[0].set_title(f'Strain values at column x=0')
    axs[0].grid(True)

    axs[1].plot(df.columns, df.iloc[-1])
    axs[1].set_xlabel('Column Index')
    axs[1].set_ylabel('Strain')
    axs[1].set_title(f'Strain field at center strain ≈ {max_centre_strain}')
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()

    return df

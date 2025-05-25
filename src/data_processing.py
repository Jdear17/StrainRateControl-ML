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

def sym_dis(df):

    df_ = df.copy()
    df_.columns = np.arange(25, -25.5, -0.5)
    df_ = df_[np.arange(-25, 25.5, 0.5)]
    DS = np.log((np.exp(df) + np.exp(df_)) * 0.5)
    return DS

def df_to_X_y(df, temp,rol, window_size):
    T_low=300
    T_high=530
    df = df.copy()  # make a copy so the original is unchanged
    # Normalize the temperature
    df_as_np = df.to_numpy()
    df['temp'] = (temp - T_low) / (T_high - T_low)
    dt=df.index[1]-df.index[0]
    # Compute strain rate using a Savitzky-Golay filter on a smoothed rolling mean
    rolling_window_size = int(len(df) / 20)
    savgol_window_size = int(len(df) / 15)
    smoothed_strain = df[0].rolling(window=rolling_window_size, min_periods=0).mean()
    dydx = scipy.signal.savgol_filter(smoothed_strain.values / dt,
                                      window_length=savgol_window_size, polyorder=1, deriv=1)
    df['SR'] = np.minimum(dydx,rol*2) / 20

    # Prepare input features

    df_as_np_X = df[[0, 'temp', 'SR']].to_numpy()
    df = df.drop('temp', axis=1)
    df = df.drop('SR', axis=1)
    # Prepare sequences and labels
    X, y = [], []
    for i in range(len(df_as_np_X) - window_size+1):
        row = df_as_np_X[i:i + window_size]
        # If window size is 1, remove the unnecessary time dimension
        X.append(row)
        label = df_as_np[i + window_size-1]  # Assuming the label is the strain at the next time step
        y.append(label)

    return np.array(X), np.array(y)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, LSTM, Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

def build_lstm_model(input_shape=(1, 3), output_dim=101, lstm_units=16, dense_units=32, lr=0.001):
    model = Sequential()
    model.add(InputLayer(input_shape))
    model.add(LSTM(lstm_units))
    model.add(Dense(dense_units, activation='linear'))
    model.add(Dense(output_dim, activation='linear'))

    model.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=lr))
    return model

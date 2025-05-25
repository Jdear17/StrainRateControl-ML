import sys
import os
from src import process_strain_field, sym_dis, df_to_X_y, build_lstm_model,prepare_dataset

files = [
    '450-01.xlsx',
    '500-01.xlsx',
    '400-05.xlsx',
    '450-05.xlsx',
    '500-05.xlsx',
    '400-25.xlsx',
    '450-25.xlsx',
    '500-25.xlsx'
]
# train_val_split  is the number of files used for training, and the rest will be used for validation
train_indices = [0, 2, 3, 4, 6]
X_train, y_train, X_val, y_val = prepare_dataset(files, 3, 1, train_indices)

# Build the LSTM model
model = build_lstm_model()

history=model.fit(X_train, y_train, epochs=200, verbose=2, validation_data=(X_val, y_val))
# Save the model
#model.save('lstm_model.h5')
# Evaluate the model
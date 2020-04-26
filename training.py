from pyedflib import highlevel
import os
import numpy as np
import keras
from keras.datasets import mnist
from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, BatchNormalization, MaxPooling1D, Conv2D, MaxPool2D
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
import itertools
from tensorflow.python.client import device_lib
from IPython.display import SVG
from keras.utils import model_to_dot, plot_model
import pydot as pyd
# import seaborn as sns
from keras.regularizers import l2

keras.utils.vis_utils.pydot = pyd

print(device_lib.list_local_devices())

data = np.load('./data/anntd_data.npy')
# set aside last 7, samples might use them for testing
data = data[0:1300, :, :]
X = data[:, :, 1:15000]
y = data[:, :, 0]
print(X.shape)
# print(y.shape)
y = y[:, 0]
print(y.shape)

inputs = X
targets = to_categorical(y)
batch_size = 32
no_epochs = 10
no_classes = 7
# validation_split = 0.2
num_folds = 10
verbosity = 1

acc_per_fold = []
loss_per_fold = []


kfold = KFold(n_splits=num_folds, shuffle=True)
fold_no = 1
for train, test in kfold.split(inputs, targets):

    # Define the model architecture
    model = Sequential()
    model.add(Conv1D(filters=16, kernel_size=2, activation='relu',
                     kernel_regularizer=l2(0.2), input_shape=(64, 14999)))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(600, activation='relu'))
    model.add(Dense(no_classes, activation='softmax'))
    # model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy',
                  metrics=['accuracy'])

   # Generate a print
    print('------------------------------------------------------------------------')
    print(f'Training for fold {fold_no}/{num_folds} ...')

    # Fit data to model
    history = model.fit(inputs[train], targets[train],
                        epochs=no_epochs, batch_size=batch_size, shuffle=True)

    # Generate generalization metrics
    scores = model.evaluate(inputs[test], targets[test], verbose=0)
    print(
        f'Score for fold {fold_no}/{num_folds}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]*100}%')
    acc_per_fold.append(scores[1] * 100)
    loss_per_fold.append(scores[0])

    # Plot training & validation accuracy values
    plt.plot(history.history['accuracy'])
    # plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig(f'./results/acc_fold_{fold_no}.png')
    plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    # plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.savefig(f'./results/loss_fold_{fold_no}')
    plt.show()

    # Increment fold number
    fold_no = fold_no + 1
# == Provide average scores ==
print('------------------------------------------------------------------------')
print('Score per fold')
for i in range(0, len(acc_per_fold)):
    print('------------------------------------------------------------------------')
    print(
        f'> Fold {i+1} - Loss: {loss_per_fold[i]} - Accuracy: {acc_per_fold[i]}%')
print('------------------------------------------------------------------------')
print('Average scores for all folds:')
print(f'> Accuracy: {np.mean(acc_per_fold)} (+- {np.std(acc_per_fold)})')
print(f'> Loss: {np.mean(loss_per_fold)}')
print('------------------------------------------------------------------------')

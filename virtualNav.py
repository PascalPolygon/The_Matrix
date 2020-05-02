import numpy as np
from vpython import *
import keras.models

scene = canvas()

print('Loading data...')
X_train = np.load('./data/X_train.npy')
y_train = np.load('./data/y_train.npy')
model = keras.models.load_model('./models/16filt_conv1_batchnorm.h5')
print('Done!')


def predict(c):
    for i in range(len(y_train)):
        if y_train[i] == c:
            signals = X_train[i].reshape(
                (1, X_train[0].shape[0], X_train[0].shape[1]))
            yhat = model.predict(signals)
            pred = np.argmax(yhat)  # find index of max value
    return pred


def main():
    platform = box(pos=vector(0, 0, 0), size=vector(
        100, 3, 100), color=color.orange)
    ball = sphere(pos=vector(0, 5, 0), radius=4, color=color.red)

    print("Awaiting command")

    while True:
        cmmd = input("Class of signals to load:")
        cmmd = int(cmmd)

        if cmmd < 2 or cmmd > 7:
            print("Signal classes are between 3 and 6 (inclusive)")
            continue  # go back to beginning of while loop

        pred = predict(cmmd)
        print(pred)
        # move up
        if pred == 3:
            init_pos = ball.pos.y
            while ball.pos.y < init_pos+5:
                rate(100)
                ball.pos.y += 0.1
        # move right
        elif pred == 4:
            init_pos = ball.pos.x
            while ball.pos.x < init_pos+5:
                rate(100)
                ball.pos.x += 0.1
        # move down
        elif pred == 5:
            init_pos = ball.pos.y
            while ball.pos.y > init_pos-5:
                rate(100)
                ball.pos.y -= 0.1
        # move left
        elif pred == 6:
            init_pos = ball.pos.x
            while ball.pos.x > init_pos-5:
                rate(100)
                ball.pos.x -= 0.1
        else:
            print("Signal classes are between 3 and 6 (inclusive)")


if __name__ == "__main__":
    main()

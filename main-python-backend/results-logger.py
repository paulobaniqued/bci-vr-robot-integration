"""Test prediction stream output from NeuroPype."""

from pylsl import StreamInlet, resolve_stream


def main():
    # first resolve a prediction stream on the lab network
    print("looking for a Prediction stream...")
    streams = resolve_stream('type', 'Prediction')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        sample, timestamp = inlet.pull_sample()
        left_prediction = sample[0]
        right_prediction = sample[1]

        if left_prediction > right_prediction:
            prediction = "LEFT"
            print("Prediction is ", prediction, " with value ", left_prediction)
        elif left_prediction < right_prediction:
            prediction = "RIGHT"
            print("Prediction is ", prediction, " with value ", right_prediction)
        else:
            print("Prediction is equal for both class")


if __name__ == '__main__':
    main()
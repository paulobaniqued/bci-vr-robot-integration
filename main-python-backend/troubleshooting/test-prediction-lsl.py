"""Test prediction stream output from NeuroPype."""

from pylsl import StreamInlet, resolve_stream


def main():
    # first resolve a prediction stream on the lab network
    print("looking for a Prediction stream...")
    streams = resolve_stream('type', 'Prediction')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()

        print("timestamp: ", timestamp)

        left_prediction = sample[0]
        right_prediction = sample[1]
        print("left prediction: ", left_prediction)
        print("right prediction: ", right_prediction)


if __name__ == '__main__':
    main()
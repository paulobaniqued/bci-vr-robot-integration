"""Example program to demonstrate how to read string-valued markers from LSL."""

from pylsl import StreamInlet, resolve_stream


def main():
    # first resolve a marker stream on the lab network
    print("looking for a marker stream...")
    streams = resolve_stream('type', 'Markers')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    trial_counter = 0
    left_counter = 0
    right_counter = 0
    trial = 'none'

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()

        if (sample[0] == '3') | (sample[0] == '4'):

            trial_counter += 1

            if sample[0] == '3':
                left_counter += 1
                trial = 'left'
            elif sample[0] == '4':
                right_counter += 1
                trial = 'right'

            print("Trial: ", trial_counter, " ", trial)
            print("Left count: ", left_counter, " / ", "Right count: ", right_counter)


    

if __name__ == '__main__':
    main()
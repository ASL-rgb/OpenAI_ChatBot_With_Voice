import pyaudio
import wave
import keyboard

def record():
    chunk_size = 1024  # Record in chunks of 8096 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    sample_rate = 44100  # Record at 44100 samples per second
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    def callback(in_data, frame_count, time_info, status):
        frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    print('Press space to start recording...')
    while True:
        if keyboard.is_pressed("space"):
            break

    print('Recording...')
    print('\nPress Enter to finish recording')
    frames = []  # Initialize array to store frames
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size,
                    stream_callback=callback)

    while not keyboard.is_pressed("enter"):
        pass

    # Stop the stream and add frames to recording
    stream.stop_stream()
    stream.close()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Terminate PyAudio
    p.terminate()
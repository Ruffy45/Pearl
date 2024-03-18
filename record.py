import pyaudio
from faster_whisper import WhisperModel
import wave




def save_audio_chunk(data, filename):
  # Assuming 16-bit signed integer PCM data with specific channels and rate
  # Adjust these parameters based on your actual audio format
  wf = wave.open(filename, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))  # Use get_sample_size method
  wf.setframerate(RATE)
  wf.writeframes(data)
  wf.close()


# Model and audio processing parameters
model_size = "large-v3"
device = "cuda"  # Assuming GPU acceleration
compute_type = "float16"
CHUNK = 1024  # Audio chunk size
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono
RATE = 44100  # Sampling rate (Hz)

# Initialize model
model = WhisperModel(model_size, device=device, compute_type=compute_type)

# Initialize PyAudio object
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Start speaking...")
x=0
while True:
    x+=1
    data = stream.read(CHUNK)  # Read audio data

    # Convert data to a format your model accepts (likely NumPy array)
    # Your model documentation might specify the expected format
    chunk_file = "temp_chunk.wav"
    save_audio_chunk(data , "temp_chunk.wav")  # Replace with your conversion function 
        
    # Check for termination (optional)
    if x == 10:
        break

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

print("Finished recording.")

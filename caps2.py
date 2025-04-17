import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq, irfft
def collect_green_channel(video_path):
    cap = cv2.VideoCapture(video_path)
    green_channels = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Extract the green channel
        green_channel = frame_rgb[:, :, 1]
        # Calculate the mean of the green channel and append to the list
        green_channels.append(np.mean(green_channel))

    cap.release()
    return np.array(green_channels)

# Provide the path to your video file
video_path = 'Desktop/build/WIN_20240727_15_39_19_Pro.mp4'
green_channel_data = collect_green_channel(video_path)

# Step 3: Mean normalize the pixel values
mean_value = np.mean(green_channel_data)
normalized_signal = green_channel_data - mean_value

# Plot the normalized signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(normalized_signal)
plt.title('Normalized Green Channel Signal')
plt.xlabel('Frame Number')
plt.ylabel('Amplitude')

sampling_rate = 30  # Assuming video is recorded at 30 frames per second
num_frames = len(normalized_signal)
frequencies = rfftfreq(num_frames, d=1/sampling_rate)
fft_values = rfft(normalized_signal)

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_values))
plt.title('FFT of Normalized Green Channel Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
min_freq = 0.45
max_freq = 8.0

mask = (frequencies >= min_freq) & (frequencies <= max_freq)
filtered_frequencies = frequencies[mask]
filtered_fft_values = np.abs(fft_values[mask])

plt.figure(figsize=(12, 6))
plt.plot(filtered_frequencies, filtered_fft_values)
plt.title('Filtered FFT of Normalized Green Channel Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.show()

peak_frequency = filtered_frequencies[np.argmax(filtered_fft_values)]
video_duration = num_frames / sampling_rate
bpm = peak_frequency * 60

print(f'Peak Frequency: {peak_frequency:.2f} Hz')
print(f'Heart Rate: {bpm:.2f} BPM')


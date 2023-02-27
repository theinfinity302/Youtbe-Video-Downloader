from pytube import YouTube

# Enter the YouTube link
link = input("Enter the YouTube link: ")

# Create a YouTube object
yt = YouTube(link)

# Get all available streams
streams = yt.streams.all()

# Display the available resolutions
print("Available resolutions:")
for i, stream in enumerate(streams):
    print(f"{i+1}. {stream.resolution}")

# Prompt the user to select a resolution
selection = int(input("Enter the number for the desired resolution: "))

# Download the video at the selected resolution
print("Downloading...")
streams[selection-1].download()
print("Download complete!")

import os
import yt_dlp

def download_video(url, output_path="downloads/"):
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Save with video title
        'format': 'bestvideo+bestaudio/best',  # Download best quality video + audio
        'noplaylist': True,  # Disable downloading playlists
        'quiet': False,  # Set to True to suppress detailed output
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Optional: convert to another format
            'preferedformat': 'mp4',  # Convert to mp4 format
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading from URL: {url}")
        try:
            ydl.download([url])
            print("Download complete!")
        except Exception as e:
            print(f"Error downloading video: {e}")

if __name__ == "__main__":
    while True:
        video_url = input("Enter the video URL (or 'exit' to quit): ")

        if video_url.lower() == 'exit':
            break

        download_video(video_url)

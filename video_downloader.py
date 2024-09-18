import yt_dlp

def download_video(url, output_path="downloads/"):
    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Save with title as filename
        'format': 'bestvideo+bestaudio/best',  # Download the best available video + audio
        'noplaylist': True,  # Disable downloading playlists
        'quiet': False,  # Set to True to suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading from URL: {url}")
        ydl.download([url])
        print("Download complete!")


if __name__ == "__main__":
    # Example URL (You can add multiple URLs to the list)
    video_url = input("Enter the video URL: ")
    
    download_video(video_url)

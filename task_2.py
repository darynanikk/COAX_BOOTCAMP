import httpx
import os
from moviepy.editor import VideoFileClip


def convert_video_to_gif(link):
    """Convert video downloaded from TikTok to gif"""

    file = "video.mp4"
    processed_file = file.replace('mp4', 'gif')

    if os.path.exists(processed_file):
        return os.path.abspath(processed_file)
    with httpx.Client() as client:
        r = client.get(link)
        print(f'Status code: {r.status_code}')

        if r.status_code == 403:
            return f'Unauthorized request.'

        with open(file, 'wb') as o:
            o.write(r.content)

    # check if file exist
    if os.path.exists(file):
        clip = VideoFileClip(file)
        clip.write_gif(processed_file)
        return os.path.abspath(file)
    else:
        return "File does not exist."

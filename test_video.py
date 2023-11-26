from moviepy.editor import VideoFileClip


def get_video_duration(file_path):
    try:
        video_clip = VideoFileClip(file_path)
        duration = video_clip.duration
        video_clip.close()
        return duration
    except Exception as e:
        print(f"Xatolik: {e}")
        return None


# Funksiyani ishlatish
video_path = "media/videos/video_2023-09-28_22-16-46.mp4" # video path
duration = get_video_duration(video_path)

if duration is not None:
    print(f"Video uzunligi: {int(duration)} sekund")
else:
    print("Video uzunligini aniqlashda xatolik yuz berdi.")

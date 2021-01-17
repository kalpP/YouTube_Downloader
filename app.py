video_url = input("Please enter the YouTube video URL: ")
video_id = video_url[(video_url.index('=') + 1): ]
thumbnail_url = f'https://img.youtube.com/vi/{video_id}/sddefault.jpg'

#
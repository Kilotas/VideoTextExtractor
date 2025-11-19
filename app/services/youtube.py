import re
from typing import List, Dict

from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
)

# поддержка /watch?v=, youtu.be/, /shorts/
YOUTUBE_URL_REGEX = re.compile(
    r"""(?x)
    (?:https?://)?       # optional http/s
    (?:www\.)?           # optional www
    (?:youtube\.com/    # youtube.com/
        (?:watch\?v=|   #   watch?v=ID
         embed/|        #   embed/ID
         v/|            #   v/ID
         shorts/)       #   shorts/ID
     |youtu\.be/)       # youtu.be/ID
    ([A-Za-z0-9_-]{11}) # capture ID (group 1)
    """
)



def extract_video_id(url: str) -> str:
    """Извлекаем ID из ссылки YouTube."""
    match = YOUTUBE_URL_REGEX.search(url)
    print(match)
    if not match:
        raise ValueError("Не удалось извлечь ID видео из ссылки.")
    return match.group(1)


def get_video_transcript(video_url: str, language_priority=None) -> List[Dict]:
    """
    Возвращает транскрипт видео как список элементов:
    [
        {"text": "...", "start": 0.33, "duration": 2.1},
        ...
    ]
    """
    if language_priority is None:
        language_priority = ["ru", "ru-RU", "en", "en-US"]

    video_id = extract_video_id(video_url)

    # Пробуем получить транскрипт по каждому языку
    for lang in language_priority:
        try:
            return YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        except (TranscriptsDisabled, NoTranscriptFound):
            continue  # пробуем следующий язык
        except Exception:
            continue

    raise RuntimeError("Нет доступного транскрипта ни на одном из указанных языков.")

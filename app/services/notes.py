from typing import List, Dict
import re


def transcript_to_text(transcript: List[Dict]) -> str:
    """Склеивает весь транскрипт в один текст."""
    parts = [chunk["text"].replace("\n", " ") for chunk in transcript]
    text = " ".join(parts)
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> List[str]:
    """Режет текст на предложения по ., ! или ?"""
    raw = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in raw if s.strip()]


def build_notes_from_transcript(transcript: List[Dict], max_points: int = 10) -> List[str]:
    """Строит конспект (список ключевых предложений)."""
    full_text = transcript_to_text(transcript)
    sentences = split_sentences(full_text)

    if not sentences:
        return ["Не удалось построить конспект"]

    sorted_sentences = sorted(sentences, key=len, reverse=True)

    return sorted_sentences[:max_points]



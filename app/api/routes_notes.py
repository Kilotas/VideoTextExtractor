from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

from ..services.youtube import get_video_transcript
from ..services.notes import build_notes_from_transcript
from ..core.errors import BadRequest, NotFound, InternalError


router = APIRouter(prefix="/notes", tags=["notes"])


class NotesRequest(BaseModel):
    url: HttpUrl
    max_points: int = 10


class NotesResponse(BaseModel):
    url: HttpUrl
    points: list[str]


@router.post("", response_model=NotesResponse)
def generate_notes(payload: NotesRequest):
    try:
        transcript = get_video_transcript(str(payload.url))

    except ValueError as e:
        raise BadRequest(detail=str(e))

    except RuntimeError as e:
        raise NotFound(detail=str(e))

    except Exception as e:
        raise InternalError(detail=f"Ошибка получения транскрипта: {e}")

    points = build_notes_from_transcript(
        transcript,
        max_points=payload.max_points
    )

    return NotesResponse(url=payload.url, points=points)

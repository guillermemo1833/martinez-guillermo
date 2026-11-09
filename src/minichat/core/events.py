from __future__ import annotations

from enum import Enum


class Event(str, Enum):
    """Enumeration of the observable event names used across the app.

    Centralizes the Observer-pattern event identifiers so that a typo
    becomes an AttributeError at import time instead of a silent bug.
    Inherits from ``str`` so members compare equal to their raw string
    value and remain usable as dict keys.

    Values:
        MESSAGES_UPDATED: Fired after any session mutation.
        CONFIG_CHANGED: Fired after updating GenerationConfig.
        GENERATING_START: Fired before calling the backend.
        GENERATING_DONE: Fired after a successful reply.
        GENERATING_ERROR: Fired on backend exception.
        EXPORT_DONE: Fired after exporting the transcript as JSON.

    Example:
        self._notify(Event.MESSAGES_UPDATED, {})
    """

    MESSAGES_UPDATED = "messages_updated"
    CONFIG_CHANGED = "config_changed"
    GENERATING_START = "generating_start"
    GENERATING_DONE = "generating_done"
    GENERATING_ERROR = "generating_error"
    EXPORT_DONE = "export_done"

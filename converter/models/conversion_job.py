from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
from uuid import uuid4


@dataclass
class ConversionJob:
    """
    Represents a complete conversion request.

    This object flows through the entire conversion pipeline:

    Input
        ↓
    Inspector
        ↓
    Planner
        ↓
    Dispatcher
        ↓
    Converter
        ↓
    Validator
        ↓
    Exporter
    """

    # ------------------------------------------------------------------
    # Job Information
    # ------------------------------------------------------------------

    job_id: str = field(default_factory=lambda: str(uuid4()))

    status: str = "created"

    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    error: Optional[str] = None

    # ------------------------------------------------------------------
    # User Input
    # ------------------------------------------------------------------

    source: str = ""
    output_path: Optional[Path] = None

    # After download / resolution
    model_path: Optional[Path] = None

    # ------------------------------------------------------------------
    # Inspector Results
    # ------------------------------------------------------------------

    framework: Optional[str] = None
    architecture: Optional[str] = None
    task: Optional[str] = None

    # ------------------------------------------------------------------
    # Loaded Objects
    # ------------------------------------------------------------------

    model: Optional[Any] = None
    tokenizer: Optional[Any] = None

    # ------------------------------------------------------------------
    # Planner / Dispatcher
    # ------------------------------------------------------------------

    backend: Optional[str] = None

    # ------------------------------------------------------------------
    # Converter Output
    # ------------------------------------------------------------------

    converted_model: Optional[Any] = None

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    options: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    validation_results: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    metadata: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Device information
    # ------------------------------------------------------------------

    device_info: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------------------

    def mark_started(self) -> None:
        self.status = "running"
        self.started_at = datetime.utcnow()

    def mark_completed(self) -> None:
        self.status = "completed"
        self.completed_at = datetime.utcnow()

    def mark_failed(self, error: Exception | str) -> None:
        self.status = "failed"
        self.completed_at = datetime.utcnow()
        self.error = str(error)

    @property
    def duration(self) -> Optional[float]:
        """
        Returns the conversion time in seconds.
        """
        if self.started_at is None or self.completed_at is None:
            return None

        return (self.completed_at - self.started_at).total_seconds()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "job_id": self.job_id,
            "status": self.status,
            "source": self.source,
            "model_path": str(self.model_path) if self.model_path else None,
            "framework": self.framework,
            "architecture": self.architecture,
            "task": self.task,
            "backend": self.backend,
            "output_path": str(self.output_path) if self.output_path else None,
            "duration": self.duration,
            "error": self.error,
            "metadata": self.metadata,
            "validation_results": self.validation_results,
            "options": self.options,
            "device_info": self.device_info,
        }
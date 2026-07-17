from __future__ import annotations

from converter.models.conversion_job import ConversionJob
from converter.inspector.inspector import Inspector
from converter.planner.planner import Planner
from converter.dispatcher.dispatcher import Dispatcher


def convert(source: str):

    job = ConversionJob(source=source)

    print("\nInspecting model...")
    Inspector().inspect(job)

    print(f"Framework    : {job.framework}")
    print(f"Architecture : {job.architecture}")

    planner = Planner()

    job.backend = planner.select_backend(job)

    print(f"Backend      : {job.backend}")

    dispatcher = Dispatcher()

    output = dispatcher.dispatch(job)

    print("\nConversion Complete!")
    print(f"Output : {output}")

    return output
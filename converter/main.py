from __future__ import annotations

from converter import device
from converter.report.json_report import JSONReport
from converter.validator.validator import Validator
from converter.models.conversion_job import ConversionJob
from converter.inspector.inspector import Inspector
from converter.planner.planner import Planner
from converter.dispatcher.dispatcher import Dispatcher
from converter.exporter.exporter import Exporter
from converter.report.json_report import JSONReport
from converter.device.detector import DeviceDetector



def convert(source: str):

    job = ConversionJob(source=source)
    device = DeviceDetector().detect()
    job.device_info = device.to_dict()

    try:
        job.mark_started()

        print("\nInspecting model...")
        Inspector().inspect(job)

        print(f"Framework    : {job.framework}")
        print(f"Architecture : {job.architecture}")

        planner = Planner()

        job.backend = planner.select_backend(job)

        print(f"Backend      : {job.backend}")

        dispatcher = Dispatcher()

        output = dispatcher.dispatch(job)

        job.output_path = output

        Validator().validate(job)

        final_output = Exporter().export(
            job,
            output
        )
        
        JSONReport().generate(job)

        job.mark_completed()

        print("\nConversion Complete!")
        print(f"Output : {output}")

        return job

    except Exception as e:
        job.mark_failed(e)
        raise
FROM python:3.10-slim

COPY src /llmperf/src/

COPY pyproject.toml *.py /llmperf/

WORKDIR /llmperf

RUN pip install .

COPY src/llmperf/sonnet.txt /usr/local/lib/python3.10/site-packages/llmperf/

ENTRYPOINT ["python", "token_benchmark_ray.py"]

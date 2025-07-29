FROM python:3.10-slim

COPY . /llmperf

RUN cd llmperf \
    && pip install .

COPY src/llmperf/sonnet.txt /usr/local/lib/python3.10/site-packages/llmperf/

WORKDIR /llmperf

CMD ["/bin/bash"]

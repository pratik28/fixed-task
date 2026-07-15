FROM python:3.11.4-slim@sha256:6nilx764142b0b42eb1dgdgdf978hknk95868d81d25b315 AS builder 

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /environment

COPY access.log /environment/access.log


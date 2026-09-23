FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2024.3.5
RUN pip install torch==1.13.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install torchvision==0.14.1 --index-url https://download.pytorch.org/whl/cpu

WORKDIR /repo
COPY . /repo
FROM bentoml/model-server:0.11.0-py37
LABEL author="ersilia"

WORKDIR /repo
COPY . /repo

RUN conda install -c rdkit rdkit=2020.09.1.0
RUN pip install torch==1.13.1+cpu torchvision==0.14.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

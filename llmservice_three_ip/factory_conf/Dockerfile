FROM nvcr.io/nvidia/pytorch:24.04-py3

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
RUN pip install -e .[deepspeed,metrics,bitsandbytes]

EXPOSE 7860

CMD [ "llamafactory-cli", "webui" ]

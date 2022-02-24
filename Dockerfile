FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONUTF8=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

RUN apt-get -q update && \
  apt-get -y clean

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]

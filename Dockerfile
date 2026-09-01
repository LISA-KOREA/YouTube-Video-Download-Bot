FROM python:3.14-rc-alpine3.20

WORKDIR /app

RUN apk add --no-cache \
    ffmpeg \
    jq \
    python3-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    curl \
    unzip

RUN curl -fsSL https://deno.land/install.sh | sh

ENV DENO_INSTALL=/root/.deno
ENV PATH=$DENO_INSTALL/bin:$PATH

RUN deno --version

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN yt-dlp --version && \
    ffmpeg -version && \
    python3 -m pip check

CMD ["python3", "bot.py"]

FROM python:3.11-alpine

# Set build directory
WORKDIR /tmp

# Copy files necessary for build
COPY requirements.txt requirements.txt

# COPY setup.py setup.py

# Perform build and cleanup artifacts
RUN apk add --no-cache \
    git curl \
    && apk add --no-cache --virtual .build gcc musl-dev make\
    && pip install --user -r requirements.txt \
    && apk del .build gcc musl-dev \
    && rm -rf /tmp/*

ENV PATH=$PATH:/root/.local/bin
# Set working directory

RUN mkdir /app
WORKDIR /app
COPY ./ ./

# Expose FastAPI development server port
EXPOSE 5000

# Start development server by default
ENTRYPOINT ["python", "run.py"]
CMD ["python", "run.py"]
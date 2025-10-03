from python:3.10
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /NEW FOLDER

COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
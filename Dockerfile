FROM python:3.11-slim@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf

RUN useradd -m -u 1000 -s /bin/bash appuser

WORKDIR /app

# Copy requirements file and install dependencies (currently not needed) - but we discussed it in the interview ;)
# COPY requirements.txt .
# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser server.py .

RUN mkdir -p /app/logs && chown -R appuser:appuser /app/logs

USER appuser

EXPOSE 5050

CMD ["python", "-u", "server.py"]


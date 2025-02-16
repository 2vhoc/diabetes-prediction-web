FROM python:3.12.3
RUN apt-get update && apt-get install -y \
    python3-pip \
    vim \
    && rm -rf /var/lib/apt/lists/*
RUN pip install fastapi pydantic numpy pandas joblib scikit-learn seaborn matplotlib uvicorn
WORKDIR /app/back_end
COPY . /app/back_end
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

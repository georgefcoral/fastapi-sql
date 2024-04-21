## Intelimetrica Project

## Instruccions for run locally

### Install dependencies

> - **`python -m venv myenv`**
> - **`source myenv/Scripts/activate`**

- **`pip install fastapi`**
- **`pip install uvicorn`**
- **`pip install sqlalchemy`**
- **`pip install geopy`**

### Migration of data

- **`cd ./scripts`**
- **`python migrate_csv_to_sqlite.py`**

## Run server

- **`uvicorn main:app --reload --port 5000`**

## Project Structure

The project structure separates each of the application layers into different directories. In this case,
we will have the following directories:

```
project/
├── config/
├── models/
├── routers/
├── schemas/
├── services/
├── scripts/
├── utils/
└── main.py
```
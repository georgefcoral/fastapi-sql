python -m venv myenv

source myenv/Scripts/activate

pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install geopy

cd ./scripts

python migrate_csv_to_sqlite.py

cd ..
uvicorn main:app --reload --port 5000

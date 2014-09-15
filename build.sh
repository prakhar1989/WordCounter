echo "Installing requirements"
pip install -r requirements.txt
mkdir data
python app/db.py setup
python server.py

install:
	echo "Installing requirements"
	pip install -r requirements.txt
	mkdir data
	python app/db.py setup
	echo "App ready to rock and roll.. Run ./run to start app"

test:
	echo "Running tests ..."

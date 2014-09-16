install:
	echo "Installing requirements"
	pip install -r requirements.txt
	mkdir data
	chmod +x run
	./run -setup
	echo "App ready to rock and roll.. Run ./run to start app"

test:
	./run -test

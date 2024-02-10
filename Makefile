start: setup
	uvicorn --app-dir ./src main:app --reload
setup: requirements.txt
	pip install -r requirements.txt

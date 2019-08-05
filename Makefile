VENV ?= venv
PIP ?= $(VENV)/bin/pip

help:
	@echo "  help         this list"
	@echo "  clean        delete virtualenv directory $(VENV)"
	@echo "  prepare-venv install virtualenv and requiements into directory $(VENV)"

clean:
	rm -rf venv

prepare-venv:
	virtualenv --python python3.6 $(VENV) --no-pip
	$(VENV)/bin/easy_install pip==18.0
	$(PIP) install -r requirements.txt

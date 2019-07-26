VENV ?= env
PIP ?= $(VENV)/bin/pip

help:
	@echo "  help         this list"
	@echo "  clean        delete virtualenv directory $(VENV)"
	@echo "  prepare-venv install virtualenv and requiements into directory $(VENV)"

clean:
	rm -rf env

prepare-venv:
	virtualenv -p /usr/bin/python3.6 $(VENV) --no-pip
	$(VENV)/bin/easy_install pip==19.1
	$(PIP) install -r requirements.txt

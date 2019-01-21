.PHONY: clean train-nlu train-core cmdline server

TEST_PATH=./

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config"
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data"
	@echo "    action-server"
	@echo "        Starts the server for custom action."
	@echo "    cmdline"
	@echo "       This will load the assistant in your terminal for you to chat."


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md --path models --project livio --fixed_model_name nlu --verbose

run-nlu-server:
	python -m rasa_nlu.server --path models/nlu

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/livio/dialouge -c policies.yml

action-server:
	python -m rasa_core_sdk.endpoint --actions actions

run-core-server:
	python -m rasa_core.run -d models/livio/dialouge -u models/livio/nlu --endpoints endpoints.yml

retrain-reload-app:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md --path models --project livio --fixed_model_name nlu --verbose
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/livio/dialouge -c policies.yml
	python app.py

retrain-reload-core-server:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md --path models --project livio --fixed_model_name nlu --verbose
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/livio/dialouge -c policies.yml
	python -m rasa_core.run -d models/livio/dialouge -u models/livio/nlu --endpoints endpoints.yml

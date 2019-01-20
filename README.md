# livio-bot
A chatbot to answer questions on non-alcoholic fatty liver disease (NAFLD)

## Installation:
- `requirements.txt`
- `pip install rasa_nlu`
- `pip install rasa_core`
- `conda install -c conda-forge spacy`
- `python -m spacy download en`
- make
- `python -m pip install msgpack<0.6.0`
- `pip install msgpack==0.5.6`

## Use:
1. Train the Rasa NLU model by running:
`make train-nlu`: train NLU model from contents in nlu_data
This will train the Rasa NLU model and store it inside the /models/current/nlu folder of your project directory.
`make nlu-server`: run NLU server

2. Train the Rasa Core model by running:
`make train-core`
This will train the Rasa Core model and store it inside the /models/current/dialogue folder of your project directory.

3. In a new terminal start the server for the custom action by running:
`make action-server`
This will start the server for emulating the custom action.

4. Test the assistant by running:
`make cmdline`
This will load the assistant in your terminal for you to chat.

## UI to train data:
https://rasahq.github.io/rasa-nlu-trainer/

https://www.analyticsvidhya.com/blog/2018/01/faq-chatbots-the-future-of-information-searching/#comment-151142

## Scripts:
* app.py: Chatbot UI built using Flask, using templates/*.html
* engine.py: Chatbot core logic as well as knowledgebase.
* run_training: Windows batch file to build trained modeling
* run_server: Windows batch file to execute Rasa-NLU server.

## Other Data
* nlu_config.yml: Rasa NLU settings for training as well as executing intent extraction
* nlu_data: Directory containing training files
* static and templates: Flask UI related files

## Dependencies:
* Needs Python 3.5, numpy, scipy, spacy, sklearn crf suite

## ToDos
* Add more training data
* Entity extraction not working as desired, find out more.
* Etc.

## References
* Rasa-NLU [installation](https://github.com/RasaHQ/rasa_nlu)
* Bhavani Ravi’s event-bot [code](https://github.com/bhavaniravi/rasa-site-bot), Youtube [Video](https://www.youtube.com/watch?v=ojuq0vBIA-g)

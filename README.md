# Steve-Jobs-Chatbot-NLP
This is a Steve Jobs chatbot. It extracts topic, subject, and root from the user's input and uses that to find the most pertinent information from the database.

If it cannot find a suitable reply it asks you for the most suitable reply and stores it in learnedData.txt and after that, it can answer the same question.

It also stores the user's name and any new information that the user provides.

The chatbot may take up to 3 minutes to start depending on your system, so be patient!

Have chatbot.py, database.txt, and learnedData.txt in the same folder.
You need to run StanfordCoreNLP Server locally for this chatbot to function.

My chatbot is implemented in python and uses spacy, stanford core nlp and nltk.

It extracts 3 parameters from a user's input:
1. Subject
2. Root
3. Object
It then uses these parameters to query the database for the most appropriate response.

It also stores the user's name and any new information that the user provides.

### Instructions to execute program:

1. Download required packages and libraries
	Enter the following commands in cmd to download the following libraries:
	
	pip install spacy
	
	pip install nltk
	
	pip install stanfordcorenlp
	
	python -m spacy download en
	
	pip install en_core_web_sm

2. Download Stanford CoreNlP(not the same as running the pip command) from: https://stanfordnlp.github.io/CoreNLP/download.html

3. Extract Stanford CoreNlp from zip file.

4. Enter the following command in cmd (path should be the downloaded Stanford CoreNLP folder)
	java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators

5. In cmd (path should be where you downloaded chatbot.py and database.txt) enter the following command:
	python chatbot.py

6. Chat Away!	

Please note that you need to have the Stanford CoreNLP server running locally for the chatbot to work.
If you have any trouble ruuning Stanford CoreNLP see https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/


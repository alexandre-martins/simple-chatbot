from utils import get_random_response
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'JoeBot',
    read_only=False,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    response_selection_method=get_random_response,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I dont understand. Iam still learning!',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'maximum_similarity_threshold': 0.70
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training with general and custom data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
trainer.train("src/training_data/personal_questions.yml")


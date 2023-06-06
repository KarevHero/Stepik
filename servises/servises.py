import random
from lexicon.lexicon_ru import LEXICON_RU

def bot_choice():
    return random.choice(['rock', 'scissors', 'paper'])

def _norm_messege(user_unswer: str):
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_unswer:
            return key
    raise Exception

def get_winner(user_unsver: str, choice_bot: str):
    user_unsver = _norm_messege(user_unsver)
    rules: dict[str, str] = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if user_unsver == choice_bot:
        return 'nobody_won'
    elif rules[user_unsver] == choice_bot:
        return 'user_won'
    else:
        return 'bot_won'
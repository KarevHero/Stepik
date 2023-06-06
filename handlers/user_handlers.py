from aiogram import Router
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, game_kb
from lexicon.lexicon_ru import LEXICON_RU
from aiogram.filters import Command, CommandStart, Text
from servises.servises import bot_choice, get_winner

router: Router = Router()

@router.message(CommandStart())
async def m_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

@router.message(Command(commands=['help']))
async def m_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

@router.message(Text(text=LEXICON_RU['yes_button']))
async def m_yes(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(Text(text=LEXICON_RU['no_button']))
async def m_no(message: Message):
    await message.answer(text=LEXICON_RU['no'])

@router.message(Text(text=[LEXICON_RU['rock'], LEXICON_RU['scissors'], LEXICON_RU['paper']]))
async def m_process(message: Message):
    choice_bot = bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[choice_bot]}')
    winner = get_winner(message.text, choice_bot)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

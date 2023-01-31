import logging
from typing import Any, Dict

from aiogram import F, Router, html, types
from aiogram.filters import Command
import openai
form_router = Router()
openai.api_key = "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"




@form_router.message(Command("start"))
async def start_cmd(message: types.Message):
  await message.answer("<b>Hi, Welcome to my bot! Send your promt and GPT-3 AI will answer you in few seconds. This bot was created by @workani</b>", parse_mode="HTML")
  
 
@form_router.message
async def promt_handler(message: types.Message):
  user_promt = message.text
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=user_promt,
  temperature=0.6,
  max_tokens=500,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)
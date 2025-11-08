from aiogram import types  
from aiogram import F, Router
import logging  
from aiogram import Bot, Dispatcher  
from teext import *


router = Router()

logging.basicConfig(level=logging.INFO)  
bot = Bot(token="7942694780:AAEDRJqWBnKbiAx1p99Kt7sW_YGtczeQGuM")  
dp = Dispatcher()  












@router.callback_query(F.data == "A1") 
async def bruises(callback_query: types.CallbackQuery): 
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
    text = answers['A1'])
    
    

@router.callback_query(F.data == "A2") 
async def cut_wound(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['A2'])

@router.callback_query(F.data == "B1") 
async def abrasions(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['B1'])

@router.callback_query(F.data == "B2") 
async def splinter(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['B2'])

@router.callback_query(F.data == "C1") 
async def bruise(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['C1'])

@router.callback_query(F.data == "C2") 
async def laceration(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['C2'])

# @router.callback_query(F.data == "D1")
# async def send_random_value(callback_query: types.CallbackQuery):
#     await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
#     await bot.answer_callback_query(callback_query.id) 
#     await callback_query.message.answer(
#         text = answers['D1'])

@router.callback_query(F.data == "D2") 
async def acne(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['D2'])


@router.callback_query(F.data == "A3") 
async def bee_bumblebee_or_wasp_sting(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['A3'])
    
@router.callback_query(F.data == "A4") 
async def ant_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['A4'])
    
@router.callback_query(F.data == "B3") 
async def tick_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['B3'])
    
@router.callback_query(F.data == "B4") 
async def hedgehog_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['B4'])
    
@router.callback_query(F.data == "C3") 
async def flea_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['C3'])
    

@router.callback_query(F.data == "C4") 
async def snake_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['C4'])
    
@router.callback_query(F.data == "D3") 
async def spider_bite(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['D3'])
    

@router.callback_query(F.data == "D4") 
async def animal_bites(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id) 
    await callback_query.message.answer(
        text = answers['D4'])
    


@router.message(F.text.lower() == "помощь при инсульте") 
async def stroke_assistance(message: types.Message): 
    new_msg = await bot.copy_message(
        chat_id=message.from_user.id,
        from_chat_id=message.from_user.id, 
        message_id=message.message_id
    )
    await message.delete()
    await bot.edit_message_text(
        text = answers['D5'],
        chat_id=message.from_user.id,
        message_id=new_msg.message_id
    )

    


@router.message(F.text.lower() == "помощь при потере сознания") 
async def assistance_in_case_of_loss_of_consciousness(message: types.Message): 
    
    new_msg = await bot.copy_message(
        chat_id=message.from_user.id,
        from_chat_id=message.from_user.id, 
        message_id=message.message_id
    )
    await message.delete()
    await bot.edit_message_text(
        text = answers['D6'],
        chat_id=message.from_user.id,
        message_id=new_msg.message_id
    
    )


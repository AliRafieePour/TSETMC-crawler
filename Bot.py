from Dependecies import *



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, UNKNOWN= range(2)

def start(update, context):
    reply_keyboard = [['S11'], ['S12'], ['S13'], ['S14'], ['S15'], ['S16'], ['S17'], ['S18'], ['S19'], ['S20']]

    update.message.reply_text( 'Filter khod ra entekhab konid!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER

def gender(update, context):
    
    user = update.message.from_user
    if (update.effective_chat.username == "Tishk_1981" or update.effective_chat.username == "crawl3r"):
        init(update.message.text)
    
        logger.info('I got the message')
        logger.info("Filter of %s", user.first_name)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_document(chat_id=update.effective_chat.id, document=open('C:/Users/Administrator/Desktop/Output_{}.xlsx'.format(update.message.text), 'rb'))
        
        context.bot.send_message(chat_id="@Filter_12345", text="{}".format(update.message.text))
        context.bot.send_document(chat_id="@Filter_12345", document=open('C:/Users/Administrator/Desktop/Output_{}.xlsx'.format(update.message.text), 'rb'))
        
        
        reply_keyboard = [['S11'], ['S12'], ['S13'], ['S14'], ['S15'], ['S16'], ['S17'], ['S18'], ['S19'], ['S20']]
    
        update.message.reply_text( 'Filter khod ra entekhab konid!',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
        return GENDER

def unknown(update, context):
    logger.info("Known command")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
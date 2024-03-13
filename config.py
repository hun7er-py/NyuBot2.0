import nextcord

"""
this is the global variable set/get cog. All cross - cog vars will be declared and stored here;

Should work on declaring all vars with their expected type

"""
TOKEN = None
CREATE_CHANNEL = None
TEST = "TESTING UPPER"
CREATION_CHANNEL = None
TEMP_CAT = None
CREATION_CHANNEL_NAME = ""
MODERATION_CHANNEL = None
WELCOME_MESSAGE = "Welcome to the server! We hope you enjoy your stay"
WELCOME_TITLE = "Welcome!"
DJ_CHANNEL = None
DJ_ROLE = None
CTX_MUSIC = None
SETUP_NYU_DONE = False
TICKETING_CAT = None
TICKETING_CHANNEL = None
TICKET_COUNTER = 0
SUPPORT_ROLE = None

def set_SETUP_NYU_DONE(done):
  global SETUP_NYU_DONE
  SETUP_NYU_DONE = done
  
def get_SETUP_NYU_DONE():
  global SETUP_NYU_DONE
  return SETUP_NYU_DONE
  
def set_TEST(text):
    global TEST
    TEST = text

def get_TEST():
    global TEST
    return TEST

def set_CTX_MUSIC(ctx):
    global CTX_MUSIC
    CTX_MUSIC = ctx

def get_CTX_MUSIC():
    global CTX_MUSIC
    return CTX_MUSIC

def set_DJ_ROLE(role):
    global DJ_ROLE
    DJ_ROLE = role

def get_DJ_ROLE():
    global DJ_ROLE
    return DJ_ROLE
    
def set_DJ_CHANNEL(channel):
    global DJ_CHANNEL
    DJ_CHANNEL = channel

def get_DJ_CHANNEL():
    global DJ_CHANNEL
    return DJ_CHANNEL

def set_WELCOME_MESSAGE(text):
    global WELCOME_MESSAGE
    WELCOME_MESSAGE = text

def get_WELCOME_MESSAGE():
    global WELCOME_MESSAGE
    return WELCOME_MESSAGE

def set_WELCOME_TITLE(text):
    global WELCOME_TITLE
    WELCOME_TITLE = text

def get_WELCOME_TITLE():
    global WELCOME_TITLE
    return WELCOME_TITLE

def set_TEMP_CAT(category):
    global TEMP_CAT
    TEMP_CAT=category

def get_TEMP_CAT():
    global TEMP_CAT
    return TEMP_CAT

def set_CREATION_CHANNEL(channel):
    global CREATION_CHANNEL
    CREATION_CHANNEL = channel

def get_CREATION_CHANNEL():
    global CREATION_CHANNEL
    return CREATION_CHANNEL

def set_CREATION_CHANNEL_NAME(channel):
    global CREATION_CHANNEL_NAME
    CREATION_CHANNEL_NAME = channel

def get_CREATION_CHANNEL_NAME():
    global CREATION_CHANNEL_NAME
    return CREATION_CHANNEL_NAME

def set_MODERATION_CHANNEL(channel):
    global MODERATION_CHANNEL
    MODERATION_CHANNEL = channel

def get_MODERATION_CHANNEL():
    global MODERATION_CHANNEL
    return MODERATION_CHANNEL

def get_TOKEN():
    return str(TOKEN)



def set_TICKETING_CAT(cat):
  global TICKETING_CAT
  TICKETING_CAT = cat
def get_TICKETING_CAT():
  global TICKETING_CAT
  return TICKETING_CAT
def set_TICKETING_CHANNEL(channel):
  global TICKETING_CHANNEL
  TICKETING_CHANNEL=channel
def get_TICKETING_CHANNEL():
  global TICKETING_CHANNEL
  return TICKETING_CHANNEL
def add_TICKET_COUNTER():
  global TICKET_COUNTER
  TICKET_COUNTER = TICKET_COUNTER+1

def set_SUPPORT_ROLE(role):
  global SUPPORT_ROLE
  SUPPORT_ROLE = role

def get_SUPPORT_ROLE():
  global SUPPORT_ROLE
  return SUPPORT_ROLE


def get_TICKET_COUNTER():
  global TICKET_COUNTER
  return TICKET_COUNTER
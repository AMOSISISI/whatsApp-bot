from twilio.rest import Client

# Twilio configuration
account_sid = 'your_account_sid'
token = 'your_auth_token'
client = Client(account_sid, token)

# WhatsApp number
whatsapp_number = 'whatsapp:+14155238886'  # Twilio Sandbox WhatsApp number

# Auto-reply function

def auto_reply(message):
    response = "Hello! This is an auto-reply from the bot."
    return response

# Function to delete a message (placeholder)
def delete_message(message_sid):
    try:
        client.messages(message_sid).delete()
        print('Message deleted successfully.')
    except Exception as e:
        print(f'Error deleting message: {e}')  

# Main function to handle incoming messages
if __name__ == '__main__':
    # Here we would normally fetch the messages from Twilio and invoke the auto_reply
    # This is a mockup of how it might work in an actual implementation
    incoming_messages = [{'sid': 'msg_sid_123', 'body': 'Test message'}]  # Placeholder for incoming messages
    for msg in incoming_messages:
        reply = auto_reply(msg['body'])
        print(f'Replying to {msg['sid']} with: {reply}')  
        # In actual usage, you would send the reply here.
        # e.g. client.messages.create(from_=whatsapp_number, body=reply, to=msg['from'])
        delete_message(msg['sid'])  # Call to delete the message after replying

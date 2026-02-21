import schedule
import time
from datetime import datetime

class MessageScheduler:
    """Class to handle scheduled messaging for WhatsApp bot"""
    
    def __init__(self):
        self.scheduled_messages = {}
        self.message_id_counter = 1
    
    def schedule_message(self, phone_number, message_body, scheduled_time, recurrence=None):
        """
        Schedule a message to be sent at a specified time.
        
        Args:
            phone_number: Recipient's phone number
            message_body: Message content
            scheduled_time: Time to send (format: "HH:MM")
            recurrence: Optional recurrence pattern ("daily", "weekly", etc.)
        
        Returns:
            Message ID of the scheduled message
        """
        message_id = self.message_id_counter
        self.message_id_counter += 1
        
        self.scheduled_messages[message_id] = {
            'phone_number': phone_number,
            'message_body': message_body,
            'scheduled_time': scheduled_time,
            'recurrence': recurrence,
            'status': 'scheduled',
            'created_at': datetime.now()
        }
        
        # Schedule the job
        if recurrence == 'daily':
            schedule.every().day.at(scheduled_time).do(self.send_scheduled_message, message_id)
        elif recurrence == 'weekly':
            schedule.every().week.at(scheduled_time).do(self.send_scheduled_message, message_id)
        else:
            schedule.at(scheduled_time).do(self.send_scheduled_message, message_id)
        
        return message_id
    
    def send_scheduled_message(self, message_id):
        """Send the scheduled message"""
        if message_id in self.scheduled_messages:
            msg_info = self.scheduled_messages[message_id]
            print(f"Sending message to {msg_info['phone_number']}:{msg_info['message_body']}")
            msg_info['status'] = 'sent'
            msg_info['sent_at'] = datetime.now()
    
    def cancel_schedule(self, message_id):
        """Cancel a scheduled message"""
        if message_id in self.scheduled_messages:
            self.scheduled_messages[message_id]['status'] = 'cancelled'
            return True
        return False
    
    def modify_schedule(self, message_id, new_time=None, new_message=None):
        """Modify a scheduled message"""
        if message_id not in self.scheduled_messages:
            return False
        
        if new_time:
            self.scheduled_messages[message_id]['scheduled_time'] = new_time
        if new_message:
            self.scheduled_messages[message_id]['message_body'] = new_message
        
        return True
    
    def get_scheduled_messages(self):
        """Get all scheduled messages"""
        return self.scheduled_messages
    
    def run_scheduler(self):
        """Run the scheduler continuously"""
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == '__main__':
    scheduler = MessageScheduler()
    print("Message Scheduler initialized successfully!")
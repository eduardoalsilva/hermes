class Scheduler:
    def __init__(self):
        self.scheduled_events = []

    def schedule_event(self, title, date, time):
        if not title or not date or not time:
            raise ValueError("Title, date, and time are required for scheduling an event")

        event = {
            'title': title,
            'date': date,
            'time': time
        }

        self.scheduled_events.append(event)

    def get_scheduled_events(self):
        return self.scheduled_events.copy()

    def edit_event(self, old_title, new_title, new_date, new_time):
        for event in self.scheduled_events:
            if event['title'] == old_title:
                event['title'] = new_title
                event['date'] = new_date
                event['time'] = new_time

    def delete_event(self, title):
        self.scheduled_events = [event for event in self.scheduled_events if event['title'] != title]

    def set_reminder(self, title, minutes_before):
        if event['title'] == title:
            reminder_time = event['time'] - timedelta(minutes=minutes_before)

            print(f'Reminder: The event "{event['title']}" will occur in {minutes_before} minutes, at {reminder_time}.')
            

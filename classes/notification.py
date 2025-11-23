class Notification:
    def __init__(self, title, description, duration, urgency, icon_path):
        self.title = title
        self.description = description
        self.duration = duration
        self.urgency = urgency
        self.icon_path = icon_path
    
    def send(self):
        

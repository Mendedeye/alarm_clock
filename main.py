class AlarmClock:

    def __init__(self):
        self.current_time = "12:00 a.m."
        self.alarm_on = False
        self.alarm_time = "6:30 a.m."
    
    def set_time(self):
        print(f"\n\nThe current time is: {self.current_time}")
    
    def is_alarm_on(self, turn_on, user_alarm):
        if turn_on == "y":
            self.alarm_on = True
            print(f"The alarm is on for {user_alarm}")
        else: 
            self.alarm_on = False
            print(f"The alarm is off for {user_alarm}")
        

    def set_alarm_time(self, new_alarm):
        self.alarm_time = new_alarm
        print(f"The new alarm time is : {self.alarm_time}")



# Optional: file logging or timestamping


# 🛠 Bonus Engineering Constraints:
# Raise appropriate errors if required data is missing.

# Use a clean format to print or save data.

# Make it easy to add new roles in future without rewriting everything.
# 🧠 Real-Life Python Code Challenge: Event Registration System
# 💼 Scenario:
# You’ve been hired by an event planning company to build 
# a registration system for a large conference.
#  The company expects different kinds of participants
#  (speakers, guests, staff), and each has different required 
# information when registering. You must design a flexible system using your knowledge of:

# *args and **kwargs

# Classes and __init__

# Decorators
# Speakers must include topic, duration.



# Use a decorator to:

# Log the registration details (name, role, time registered) to a file called registrations.txt.

# 🎯 Requirements:
# Create a base class Participant with initializer logic that accepts name, role (speaker, guest, etc), and additional optional attributes (handled via **kwargs).

# Allow different types of participants to be registered with varying information:


# Support a function to display all current registrations clearly.

# Use *args if needed, e.g., if registering multiple people at once.

           # Guests must include ticket_type.
           # Staff must include department, shift.
from datetime import datetime   
class Register_sysyem():
    def __init__(self,name, role, time_registered,**kwargs):
        self.name=name
        self.role=role
        self.time_registered=time_registered
        self.kwargs=kwargs
        if self.role=="speaker":
            self.topic=kwargs.get("topic")
            self.duration=kwargs.get("duration")
            if not self.topic or not self.duration:
                raise ValueError("Speaker must include topic and duration")
        elif self.role=="staff":
            self.department=kwargs.get("department")
            self.shift=kwargs.get("shift")
            if not self.department or not self.shift:
                raise ValueError("Staff must include department and shift")
        elif self.role=="guest":
            self.ticket_type=kwargs.get("ticket_type")
            if not self.ticket_type:
                raise ValueError("Guest must include ticket")
         
    @property    
    def get_name(self):
        now=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        print ("somebody tried to acess data",now)
        return self.name
    @get_name.setter
    def get_name(self,new_name):
        if not isinstance(new_name,str):
            now=datetime.now()
            print(now,"datetime")


    def print_register(self):
        print(f"role: {self.role}")
        print(f"name: {self.name}")
        print(f"time_registered: {self.time_registered}")

        if self.role == "speaker":
          print(f"topic: {self.topic}")
          print(f"duration: {self.duration}")
        elif self.role == "staff":
          print(f"department: {self.department}")
          print(f"shift: {self.shift}")
        elif self.role == "guest":
          print(f"ticket type: {self.ticket_type}")
    





from datetime import datetime
now = datetime.now().strftime("%A-%B-%d %H:%M:%S")

speaker = Register_sysyem(
    name="Alice",
    role="speaker",
    time_registered=now,
    topic="AI Ethics",
    duration="45 minutes"
)

guest = Register_sysyem(
    name="Bob",
    role="guest",
    time_registered=now,
    ticket_type="VIP"
)

staff = Register_sysyem(
    name="Jane",
    role="staff",
    time_registered=now,
    department="Security",
    shift="Night"
)

speaker.print_register()
guest.print_register()
staff.print_register()       


    






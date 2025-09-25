 ## LightSwitch — Toggle On/Off

class LightSwitch:
    def __init__(self):
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

    def show_status(self):
        status = "ON" if self.is_on else "OFF"
        print("Light is", status)

switch = LightSwitch()
switch.toggle()
switch.show_status()



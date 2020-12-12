from machine import Pin

class Controller:
    
    def __init__(self):
        self.automation = True
        self.trigger_value = 15000
        self.residents_present = True
        self.sun = Pin(2,Pin.OUT)
        
    def enable_automation(self):
        self.automation = True
        
    def toggle_light(self):
        self.automation = False
        self.sun.value(not self.sun.value())
        
    def set_trigger_level(self, level):
        self.trigger_value = level
        
    def set_residents_present(self, present):
        self.residents_present = present
        
    def notify_light_level(self, level):
        if self.automation:
            if level <= self.trigger_value:
                self.sun.value(True)
            else:
                self.sun.value(False)
                
            
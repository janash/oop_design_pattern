"""
    Observer design pattern
"""

import abc

class Subject:

    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self):
        for observer in self._observers:
            observer.update(self)

#-----------------------------------------------

class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, subject):
        pass

#------------------------------------------------

class Facebook(Subject):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def new_msg(self, message):
        print('A new msg is being processed, DB, ..')
        self.notify_observer()

class Device(Observer):

    def __init__(self, name):
        self.name = name

    # lots of other methods
    def update(self, subject):
        print('Showing the msg in {}'.format(self.name))

class LoggingServer(Observer):

    # lots of other methods
    def update(self, subject):
        print('Message is saved on the server.')
#---------------------------------------------------


sarah_fb = Facebook('Sarah')

logging_server = LoggingServer()

iphone = Device('iPhone')
sarah_fb.register_observer(iphone)

desktop = Device('Desktop')
sarah_fb.register_observer(desktop)

laptop = Device('Thinkpad')
sarah_fb.register_observer(laptop)

sarah_fb.new_msg('Hello Sarah')




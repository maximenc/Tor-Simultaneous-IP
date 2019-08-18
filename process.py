# -*- coding: utf-8 -*-
from stem.control import Controller
from stem import Signal
from threading import Thread
import requests
import time
from datetime import datetime

password = None # Replace with Tor Password

class TorThread(Thread):

    def __init__(self, _id):
 
        Thread.__init__(self)
        self._id = _id
        self.port = (9050 + 10 * _id)
        self.proxy ={"http" : "socks5://localhost:" + str(self.port), "https":"socks5://localhost:"+ str(self.port)}

    def ipchange(self):
        """ Open Tor controller to change IP """
        
        with Controller.from_port(port = self.port + 1) as controller:
            controller.authenticate(password = password)
            controller.signal(Signal.NEWNYM)

    def run(self):
        """
        Replace here the execution needed
        """

        while True:
            resp = requests.get('https://api.ipify.org', proxies=self.proxy)
            myip = str(resp.content)
            print('%s - THREAD: %s - PORT: %s - IP: %s' % (datetime.now().strftime("%H:%M:%S"), self._id, self.port, myip))
            
            time.sleep(10)

            self.ipchange() # IP rotation

if __name__ == "__main__":

    nb_threads = 8  # One thread corresponds to a Tor port

    list_threards = []

    for i in range(nb_threads):
        thread = TorThread(i)
        thread.setDaemon(True)  # set Daemon to kill threads when __main__ is finished 
        list_threards.append(thread)
        thread.start()
        
    print("Press \"CTRL + C\" to exit")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
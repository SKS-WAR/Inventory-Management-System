# -*- coding: utf-8 -*-
from win10toast import ToastNotifier

def notify(msg):
    toaster = ToastNotifier()
    
    toaster.show_toast("Notification!",msg, threaded=True,
                       icon_path=None,duration=3)
    
    import time
    while toaster.notification_active():
        time.sleep(0.1)
        
#filesystem_monitoring.py
####################################################################
#monitors changes to filesystem, e.g. added/deleted files
#
#uses watchdog library (see https://pythonhosted.org/watchdog/)
####################################################################

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileWatcher:
    def __init__(self,src_path):
        self.__src_path = src_path
        self.__event_handler = NasFileEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

class NasFileEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_any_event(self,event):
        if event.event_type!="modified":
            self.notify_user(event)

    def notify_user(self,event):
        print(event.src_path + " " + event.event_type)

def start_monitoring(src_path):
    FileWatcher(src_path).run()

if __name__ == "__main__":
    FileWatcher("/home/alex/test").run()

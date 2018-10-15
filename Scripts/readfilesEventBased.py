# import os
# import timeit

# folderPath = "./test/"
# old_files = []
# while True:
# 	new_files = os.listdir(folderPath)
# 	if new_files != old_files:
# 		for filename in new_files:
# 			print(filename)
# 		print("-------------------------------------------------------------------")	
# 		old_files = new_files


import time
import cv2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
IMAGE_DIRECTORY = "./test/"


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take actions when a image file has been created
            print("Received created event - %s." % event.src_path)
            cv2.imread(event.src_path)


class ImageFileWatcher:

    def __init__(self, IMAGE_DIRECTORY):
    	self.IMAGE_DIRECTORY = IMAGE_DIRECTORY
    	self.observer = Observer()

    def run(self):
        event_handler = EventHandler()
        self.observer.schedule(event_handler, self.IMAGE_DIRECTORY, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Error")
        self.observer.join()





if __name__ == '__main__':
    w = ImageFileWatcher(IMAGE_DIRECTORY)
    w.run()
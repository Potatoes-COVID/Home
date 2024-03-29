import time
import recommender as rc
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Watches for changes in the map_data directory
# Calls recommender if a file has been modified

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        rc.recommender()


if __name__ == "__main__":
    path = "/Users/sabra/Documents/GitHub/Home/recommender/map_data"
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

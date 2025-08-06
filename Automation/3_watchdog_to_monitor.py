import os
import shutil
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/testing")

FILE_DEST = {
  '.pdf': 'PDFs',
  '.jpg': 'Images',
  '.jpeg': 'Images',
  '.png': 'Images',
}

class FileMoverHandler(FileSystemEventHandler):
  def on_created(self, event) -> None:
    if  event.is_directory:
      return
    filepath = event.src_path 
    ext = os.path.splitext(filepath)[1].lower()

    dest_folder = FILE_DEST.get(ext, "Others") # type: ignore
    full_dest = os.path.join(WATCH_FOLDER, dest_folder)
    os.makedirs(full_dest, exist_ok=True)
    move_to = os.path.join(full_dest, os.path.basename(filepath)) # type: ignore

    try: 
      shutil.move(filepath, move_to)  # type: ignore
    except: 
      print("Failed to move")

if __name__ == "__main__":
  print(f"Watching folder: {WATCH_FOLDER}")
  event_handler = FileMoverHandler()
  observer = Observer()
  observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
  observer.start()

  try: 
    while True:
      pass
  except KeyboardInterrupt:
    observer.stop()
  observer.join()


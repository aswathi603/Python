import threading 
import time
import os

File_Path = r"D:\Krish NAik\Krish Naik Ultimate Data Science RoadMAp Python\Python\May\17-05-2025\file_change.txt"

def show_changes(old,new):
    old_lines = old.splitlines()
    new_lines = new.splitlines()

    for i, line in enumerate(new_lines):
        if i >= len(old_lines) or  line != old_lines[i] :
            print(f"Line {i+1} changed or added : {line}")
    if len(old_lines) > len(new_lines):
        print("Lines were removed.")
        for j in range(len(new_lines), len(old_lines)):
            print(f"Line {j+1} removed : {old_lines[j]}")

        
def watch_file(file_path):
    print(f"Watching {file_path} for changes..... ")
    last_modified = os.path.getmtime(file_path)

    with open(file_path, 'r') as file:
        old_content = file.read()


    while True:
        time.sleep(5) # Check every 5 seconds
        try:
            current_modified = os.path.getmtime(file_path)

            if current_modified != last_modified :
                last_modified =current_modified

                with open(file_path, 'r') as file:
                    new_content = file.read()

                print(f"File {file_path} has been modified.")

                show_changes(old_content, new_content)
                old_content = new_content

        except Exception as e:
            print(f"Issue : {e}")

## deamon is to carefully exit or close the thread when the main program exits       
watcher_thread = threading.Thread(target=watch_file, args=(File_Path,), daemon=True)
watcher_thread.start()


try:
    while True:
        print("Main thread is running ...")
        time.sleep(5)
except Exception as e:
    print(f"Exception in main thread: {e}")
    print("Existing main thread gracefully...")

# when deamon is there we don't need the thread.join() as it will automatically close when the main thread exits


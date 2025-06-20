import threading
import requests
import time
url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
file_path = "downloaded_dummy.pdf"
def download_url(process_name, url, file_path):
    try:
        print(F"Download Process name started: {process_name}")
        response = requests.get(url)
        print(response)
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size =  8192):
                if chunk:
                    file.write(chunk)
        print("File downloaded Successfully")
    except Exception as e:
        print("Error Downloading File : {e}")
    print(f"Process name completed : {process_name}")

t1 =threading.Thread(target = download_url, args = ("Download without thread 1", url, "a1.png"))
t2 =threading.Thread(target = download_url, args = ("Download without thread 2", url, "a2.png"))
t3 =threading.Thread(target = download_url, args = ("Download without thread 3", url, "a3.png"))

#Thread.start()
T1 = time.time()
t1.start()
t2.start()
t3.start()

# Thread.join()
t1.join() # wait for thread 1 to complete
t2.join()
t3.join()

print("Main Program Done!!")
T2 = time.time()
print(f"Time Taken To Download : {T2 - T1} seconds")

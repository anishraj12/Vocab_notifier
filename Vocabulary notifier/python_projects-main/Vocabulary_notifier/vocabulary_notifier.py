# Import library
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        # specify parameters
        title = "Learn this Vocab"
        # use file functions to read the file
        with open("Vocabulary.txt") as vc:
            lines = vc.readlines()
            # Iterate over these lines to get one line at a time
            for vocab in lines:
                # Now create notifier
                notification.notify(title= title, message= vocab.strip(), timeout= 10)
                time.sleep(5)
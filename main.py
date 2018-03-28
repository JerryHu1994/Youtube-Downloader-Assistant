#!/usr/bin/env python3
##################################
# University of Wisconsin-Madison
# Author: Jieru Hu
##################################
# This the main file for youtube downloading.

import pafy
import time
from threading import Thread
import logging
from queue import Queue
from downloader import Download_Worker

logger = logging.getLogger(__name__)

# pass the user argument
def user_input():
    if len(sys.argv) != 3:
        print ("Usage: >> python youtube_url multi_thread")
        sys.exit(1)
    url = sys.argv[1]
    mt_flag = True if sys.argv[2] == "multi_thread" else False
    return (url)



# main method
def main():
    #url, multi_thread = user_input()

#    start_ts = time()
    num_of_worker = 3
    url1 = "https://www.youtube.com/watch?v=JujrK0xApqw"
    url2 = "https://www.youtube.com/watch?v=4SK9c5i7NGg"
    url3 = "https://www.youtube.com/watch?v=NK5DTb2YrHg"
    url4 = "https://www.youtube.com/watch?v=b9lwsIhQ7h0"
    url5 = "https://www.youtube.com/watch?v=c4deK9apylY"
    direct = "./data/"
    url_list = [url1, url2, url3, url4, url5]
    task_queue = Queue()


    #crawl the page

    logger.info("Creating a pool of {} youtube downloaders".format(num_of_worker))
    # create workers
    for i in range(num_of_worker):
        worker = Download_Worker(task_queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    for url in url_list:
        task_queue.put((direct, url))

    task_queue.join()
  #  logger.info("The downloading task took {}".format(time()-start_ts))

if __name__ == "__main__":
  main()


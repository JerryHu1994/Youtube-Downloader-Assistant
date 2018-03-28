#!/usr/bin/env python3
##################################
# University of Wisconsin-Madison
# Author: Jieru Hu
##################################
# This file defines a downloader thread for a youtube download task.

from queue import Queue
from threading import Thread
import pafy

class Download_Worker(Thread):
    def __init__(self, url_queue):
        Thread.__init__(self)
        self.queue = url_queue
    # start the thread
    def run(self):
        while True:
            # get download information from queue
            directory, link = self.queue.get()
            print("Downloading {} into {}".format(link, directory))
            self.download_video(directory, link)
            self.queue.task_done()

    # action for downloading a video given an url
    def download_video(self, directory, url):
        video = pafy.new(url)
        print ("Downloading {} from Youtube".format(video.title))
        best = video.getbest()
        print ("The video resolution: {}\nThe download format: {}\n".format(best.resolution, best.extension))
        best.download(filepath=directory, quiet=True)




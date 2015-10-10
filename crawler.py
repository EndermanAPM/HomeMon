
import http.cookiejar, urllib, getpass
from bs4 import BeautifulSoup
import urllib.request as urllib2
from login import *

#Moodle urls: toDo, create a config file for storing them.
moodleUrlRoot = ("http://moodle.monlau.es:91/")
moodleUrlLogin = (moodleUrlRoot+"login/index.php")
moodleUrlCalendar = (moodleUrlRoot+"calendar/view.php")

def crawler():
    cookieJar = http.cookiejar.CookieJar()
    opener = urllib2.build_opener(

        urllib2.HTTPCookieProcessor(cookieJar),
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=1))

    opener.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36")]

    data = urllib.parse.urlencode(forms)
    binary_data = data.encode("utf-8")
    req = urllib2.Request(moodleUrlLogin, binary_data,)
    res = opener.open(req)
    #print(res.geturl())
    #login_html = res.read()

    res = opener.open(moodleUrlCalendar)
    if res.geturl() == moodleUrlCalendar:
        print("Succesfully loged in.")
    else:
        print("I broke")

    calendar = res.read()
    calendar = calendar.decode()

    #print(calendar) //Used for debugging purposes.

    return BeautifulSoup(calendar, 'html.parser')
    #print(soup.prettify().encode("utf8")) #Used for debugging purposes.

soup = crawler()

def plain(soup):
    mydivs = soup.findAll("div", { "class" : "event" })
    print(mydivs)

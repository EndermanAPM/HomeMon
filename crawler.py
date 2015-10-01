
import http.cookiejar, urllib, getpass
from bs4 import BeautifulSoup
import urllib.request as urllib2
from login import *


moodleUrlLogin = ("http://moodle.monlau.es:91/login/index.php")
moodleUrlCalendar = ("http://moodle.monlau.es:91/calendar/view.php")

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
print(res.geturl())
#login_html = res.read()

res = opener.open("http://moodle.monlau.es:91/calendar/view.php")
print(res.geturl())
calendar = res.read()
calendar = calendar.decode()

#print(calendar) //Used for debugging purposes.

soup = BeautifulSoup(calendar, 'html.parser')
#print(soup.prettify().encode("utf8"))
mydivs = soup.findAll("div", { "class" : "event" })
print(mydivs)

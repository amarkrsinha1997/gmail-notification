__author__='''
Email : surajsinghbisht054@gmail.com
Blog  : hackworldwithssb.blogspot.in

'''

import urllib, urllib2, cookielib, sys
from getpass import getpass

def cook(cj):
        j=str(cj)
        t2=j.find(' for ')
        t1=int(j.find('~'))+1
        tokken=str(j[t1:t2])
        return tokken


def way2sms(mobile, number, password,message_raw):
        #================   Checking Mechanizam =====================================
        if len(str(number))==10:
                pass
        else:
                print " [*] Invalid Username"
                sys.exit(0)
        if len(str(password))==10:
                pass
        else:
                print " [*] Invalid Password  "
                sys.exit(0)
        #============================================================================
        # ***************** Login *******************************
        # ***************** Configuration  **********************
        url='http://site24.way2sms.com/Login1.action'
        data={'username':str(number),'password':str(password)}
        data=urllib.urlencode(data)
        # ********************************************************
        cj=cookielib.CookieJar()
        header={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0'}
        req=urllib2.Request(url, data, headers=header)
        opennr=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPRedirectHandler())
        print ' [+] Please Wait. Trying To Login In '
        req=opennr.open(req)
        sucess=str(req.info())
        sucess=sucess.find('Set-Cookie')
        if (sucess==-1):
                print '\n',' [+] Login Successful [+]'
                pass
        else:
                print '\n',' [+] Login Failed [+]'
                raw_input('')
                sys.exit(0)
        # ****** Tokken Receiving Mechanizem ******************
        tokken=cook(cj)
        print '\n [+] Tokken Received : ', tokken
        # *******************************************************************
        # ********* Sms Sending System Configuration ************************
        url='http://site24.way2sms.com/smstoss.action'
        head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Chrome/62.0.3202.94 Firefox/31.0 Iceweasel/31.8.0','Refere':str('http://site24.way2sms.com/sendSMS?Token='+tokken)}
       # mobile=int(raw_input(' [*] Please Enter Mobile Number For Sending SMS : '))
        #================   Checking Mechanizam =====================================
        if len(str(mobile))==10:
                pass
        else:
                print " [*] Invalid Username"
                sys.exit(0)


        while True:
                message_raw=str(message_raw)
                message=message_raw.replace(' ', '+')
                msglen=140-len(message)
                if len(message)<140:
                        break
                else:
                        pass
        data='ssaction=ss&Token='+tokken+'&mobile='+str(mobile)+'&message='+str(message)+'&msgLen='+str(msglen)
        req=urllib2.Request(url, data=data, headers=head)
        print ' [+] Sending SMS . Please Wait [+]'
        req=opennr.open(req)
        print '\n',' [+] Task Complete Thanks For Using [+]'
        print '\n\n\n'
        return

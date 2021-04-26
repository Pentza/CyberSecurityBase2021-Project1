# **Cyber Security Base 2021**
University of Helsinki - Cyber Security Base 2021

[Course page](https://cybersecuritybase.mooc.fi/)

## **Project I**

The task is to create a web application that has at least five different flaws from the OWASP [top ten list](https://owasp.org/www-project-top-ten/).

This project is simple web application where you can send messages to other users. You have a main page where you see your received messages and a form to send message to another user. It's implemented using Python & Django. 

## Installation
You need to have python 3.x.y and Django to run application. Runserver runs default on port 8000

```
$ git clone https://github.com/Pentza/CyberSecurityBase2021-Project1.git

$ python manage.py runserver
```

Default users:  
`admin` : `admin`  
`test` : `strongpassword`


## **Flaws**

---

### [A7:2017](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)) - Cross-Site Scripting (XSS)

The application includes unvalidated and unescaped user input as part of HTML output. Attacker can send javascript code as a message to other users and execute it in the victim's browser.

```
1. Log in as admin:admin or other user. 
2. Type '<script>alert("xss")</script>' as message content
3. Send it to other user or yourself. 
```
Using Django templates protects you against the majority of XSS attacks. Django templates escape specific characters, however in this application we disable auto-escape by using **safe** filter. 

```Django
This will be escaped: {{ data }}
This will not be escaped: {{ data|safe }}
```
Fix: Sanitize data before including it in a page. 

Read more about [Security in Django](https://docs.djangoproject.com/en/3.2/topics/security/)

---




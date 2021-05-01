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

### [A1:2017](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection) - Injection

User-supplied data in the search input is not validated by the application, thus making the SQL-injection possible. This is done in the application by using raw queries instead of Django's querysets.

To get all of the messages in the database:
```
1. Log in as admin:admin or other user.
2. Type "DOESNOTEXIST') UNION SELECT * FROM pages_message --"  in the seach bar
3. Press search
```
Server crashes if you alter the injection in certain way, for example selecting table that does not exist. 

**Fix:** Using Django's querysets as they're protected from SQL injection.

---

### [A2:2017](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication) - Broken Authentication

The application permits automated attack, such as credential stuffing. Also application has default, well known `admin:admin` credentials. 

I have included [hackpassword](https://github.com/Pentza/CyberSecurityBase2021-Project1/blob/main/hackpassword.py) tool above. It's a simple modified tool from course material that takes list of passwords and tries to log in with them. I have also provided example [password file](https://github.com/Pentza/CyberSecurityBase2021-Project1/blob/main/passwords.txt) with correct password in it. 

To use this tool:
```
1. Make sure server is running on port 8000 (it's hard coded port for example reasons).
2. Run 'python3 hackpassword.py'.
3. If match we should get our password for 'admin' printed in the console.
```
**Fix:** When and when possible, implement multi-factor authentication. Don't use default credentials and implement weak-password checks (Django actually does this if using it's templates). 

---

### [A3:2017](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure) - Sensitive Data Exposure

As this application has users and messages, the most sensitive data is user password. Using protocols like HTTP, data is trasmitted in plain text, thus making man-in-the-middle attacks possible. 

**Fix:** Use HTTPS -protocol

---

### [A6:2017](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration) - Security Misconfiguration

Attackers will often attempt to exploit unpatched flaws or access default accounts, unused pages, unprotected files and directories, etc to gain unauthorized access or knowledge of the system.

In the application config.settings SECRET_KEY is visible and DEBUG is on. This could lead to privilege escalation and remote code execution vulnerabilities.
There is also error handling that reveals stack traces that reveal informative messages to users. 

**Fix:** Use latest patches, review and update security configurations and hanle errors correctly. Remember to hide your secret key and switch DEBUG off when pushing to production.  

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
**Fix:** Sanitize data before including it in a page. 

---

### [A9:2017](https://owasp.org/www-project-top-ten/2017/A9_2017-Using_Components_with_Known_Vulnerabilities) - Using Components with Known Vulnerabilities

Outdated components might have known security issues or they're unsupported. This application uses Djanjo 3.1.7 while latest is 3.2 (atm). This is't major security issue but it's worth mention. 

**Fix:** Make sure to use supported and latest components and remove all unused stuff, for example  dependencies. 

---

### [CSRF](https://owasp.org/www-community/attacks/csrf) - Cross Site Request Forgery

Csrf is not in the top-ten anymore but I thought it would be good to showcase as it was part of the course. 

It's an attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated. 

Somehow I couldn't bypass Djangos string escapes but by using @csrf_exempt decorators you could have CSRF vulnerabilities, for example:
```html
<img src="http://127.0.0.1:8000/delete_message/?id=78"  alt="" style="width:1;height:1;">
```
Example [csrf.html](https://github.com/Pentza/CyberSecurityBase2021-Project1/blob/main/csrf.html).

**Fix:** Add @csrf_protect decorators to views and don't use @csrf_exempt decorator if not needed. 

---






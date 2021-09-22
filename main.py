import ssl
import socket
import datetime
import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

print("Insert your link below, use only bare links without any slashes like www.google.com or https://www.google.com.")
given_link = input("Insert your link: ")

if "https://" not in given_link:
    given_link = given_link[:0] + "https://" + given_link[0:]
else:
    pass
regex = re.compile(
    r'^(?:http|ftp)s?://'  
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?.)+(?:[A-Z]{2,6}.?|[A-Z0-9-]{2,}.?)|'  
    r'localhost|'  
    r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})' 
    r'(?::\d+)?'  
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

x = (re.match(regex, given_link) is not None)

if x:
    req = Request(given_link)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print("The server couldn't fulfill the request.")
        exit(0)
    except URLError as e:
        print("We couldn't reach the website server.")
        exit(0)
    else:
        pass
else:
    print("Not a valid site")
    exit(0)

if "https://" in given_link:
    given_link = given_link.replace("https://", "")
    given_link = given_link.replace("/", "")
else:
    pass


def check_expired_ssl(host, port=443):
    ssl_format = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=host, )

    conn.settimeout(3.0)
    conn.connect((host, port))
    ssl_raw = conn.getpeercert()

    date0 = datetime.datetime.strptime(ssl_raw['notAfter'], ssl_format)
    return date0


date1 = check_expired_ssl(given_link)

current_date = datetime.datetime.today()

print("Proof of certificate validity: ")
print("Current time: ", current_date.day, ".", current_date.month, ".", current_date.year, sep='')
print("Valid until: ", date1.day, ".", date1.month, ".", date1.year, sep='')

if check_expired_ssl(given_link) > current_date:
    print("THE CERTIFICATE IS VALID !")
else:
    print("THE CERTIFICATE HAS EXPIRED !")

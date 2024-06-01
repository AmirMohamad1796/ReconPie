import requests
from bs4 import BeautifulSoup
import dns.resolver
import socket
from urllib.parse import urlparse
import whois
import re
import os
import argparse
import datetime
import atexit
from Wappalyzer import WebPage , Wappalyzer
import shutil
import time
import subprocess
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', help='Enter a URL')
args = parser.parse_args()
real_url=args.url

# for remove the text of txt
def remove():

    try:
        text_file = open("main_links.txt", "r")
        text_file2 = open("subdomains.txt", "r")
        text_file3 = open("new_ip.txt", "r")
        text_file4 = open("get_links.txt", "r")
        text_file5 = open("project_times.txt", "r")

    finally:
        text_file.close()
        text_file2.close()
        text_file3.close()
        text_file4.close()
        text_file5.close()

        with open("main_links.txt", "w") as file:
            file.truncate(0)
        with open("subdomains.txt", "w") as file:
            file.truncate(0)
        with open("new_ip.txt", "w") as file:
            file.truncate(0)
        with open("get_links.txt", "w") as file:
            file.truncate(0)        
        with open("project_times.txt", "w") as file:
            file.truncate(0)            


remove()


# write to html
#add BeautifulSoup for html
soup = BeautifulSoup("<html></html>", "html.parser")

#  add head
head = soup.new_tag("head")
title = soup.new_tag("title")
title.string = "RECONPIE Hosein and Amir"
head.append(title)
soup.html.append(head)
icon=soup.new_tag("link" , rel="icon",href="./Python.svg.png")
head.append(icon)
css=soup.new_tag("link",rel="stylesheet",href="./style.css")
head.append(css)



# add body
body = soup.new_tag("body")

ul=soup.new_tag("ul",id="menu")
body.append(ul)
li1=soup.new_tag("li",id="menu__links")
li1.string="AllLinks"
ul.append(li1)
li2=soup.new_tag("li",id="menu__subs")
li2.string="AllSubdomains"
ul.append(li2)
li3=soup.new_tag("li",id="menu__step3")
li3.string="AllStatus&Titles"
ul.append(li3)
li4=soup.new_tag("li",id="menu__ip")
li4.string="AllIp"
ul.append(li4)
li5=soup.new_tag("li",id="menu__ports")
li5.string="AllOpenPort"
ul.append(li5)
li6=soup.new_tag("li",id="menu__regex")
li6.string="AllEmail&Phone"
ul.append(li6)
li7=soup.new_tag("li",id="menu__whois")
li7.string="AllInformations"
ul.append(li7)
li8=soup.new_tag("li",id="menu__wapp")
li8.string="AllTechnoligies"
ul.append(li8)
h1 = soup.new_tag("h1")
h1.string = "Reconpie project-created by hosein naderi and amir mohammad"
body.append(h1)


soup.html.append(body)
a22=soup.new_tag("a",href=real_url,target="blank")
a22.string="Main URL"
body.append(a22)


# for saving date
def save_project_time(project_name, start_time, end_time):
    start_time_formatted = start_time.strftime("%Y-%m-%d %H:%M:%S")  
    end_time_formatted = end_time.strftime("%Y-%m-%d %H:%M:%S")  
    with open("project_times.txt", "a", encoding="utf-8") as file:
        file.write(f"Project: {project_name}, Start Time: {start_time_formatted}, End Time: {end_time_formatted}\n")

project_name = "RECONPIE"
start_time = datetime.datetime.now()

# URL
all_links1 = []

# getting main links
def extract_links(url):
    """Extract links from HTML content"""
    title_mainl=soup.new_tag("h2")

    title_mainl.string="MAIN LINKS"
    body.append(title_mainl)
    div1=soup.new_tag("div",id="link-wrraper")
    body.append(div1)
    for i in url.find_all('a'):
        href = i.get('href')
        if href is not None and href.startswith('http'):
            all_links1.append(href)
            pforlinks=soup.new_tag("p",id="links")

            pforlinks.string=href
            div1.append(pforlinks)        

    return all_links1

# getting second links
def for_getting_alllinks(ls):
    unique_links = set()  
    title_links=soup.new_tag("h2")
    title_links.string="ALL LINKS"
    body.append(title_links)
    div1=soup.new_tag("div",id="links-wrraper")
    body.append(div1)
    for i in ls:
        with open("get_links.txt","a") as o:
            o.write(i + "\n")
        try:    
            r=requests.get(i)
            c=r.content
            b=BeautifulSoup(c, "html.parser")
            for link in b.find_all('a'):
                href = link.get('href')
                if href is not None and href.startswith('http'):
                    if href not in unique_links: 
                        unique_links.add(href)
                        pforlink=soup.new_tag("p",id="alllinks")

                        pforlink.string=href
                        div1.append(pforlink)    
                        with open("get_links.txt","a") as o:
                            o.write(href + "\n")
        except:
            pass      


# write our links to a txt file
def write_links_to_file(links, file_name):
    """Write links to a file"""
    with open(file_name, "a") as f:
        for link in links:
            f.write(link + "\n")


div2=soup.new_tag("div",id="subs-wrraper")

# getting sobdomains
def get_subdomains(links, api_file):
    """Get subdomains from links and API file"""
    subdomains = set()
    resolver = dns.resolver.Resolver()

    with open(api_file, "r") as f:
        for line in f.readlines():
            line = line.strip()
            for link in links:
                subdomain = link.replace("https://", line)
                try:
                    answers = resolver.resolve(subdomain, "A")
                    if answers:
                        subdomains.add(subdomain)
                        p_sub=soup.new_tag("p",id="subs")
                        p_sub.string=subdomain
                        div2.append(p_sub)
                except dns.resolver.NoAnswer:
                    print("No answer found for:", subdomain)
                except dns.resolver.NXDOMAIN:
                    print("No such domain:", subdomain)
                except dns.resolver.Timeout:
                    print("Timeout occurred for:", subdomain)
                except dns.exception.DNSException as e:
                    print("An error occurred:", e)
                except Exception as e:
                    print("An error occurred:", e)
    return subdomains

def main():
    response = requests.get(real_url)
    html = BeautifulSoup(response.content, "html.parser")
    links = extract_links(html)
    write_links_to_file(links, "main_links.txt")
    title_sb=soup.new_tag("h2")
    title_sb.string="All SUBDOMAINS"
    body.append(title_sb)
    with open("allapi.txt", "r") as f:
        api_content = f.readlines()
    subdomains = get_subdomains(links, "allapi.txt")
    with open("subdomains.txt", "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")


if __name__ == "__main__":
    main()
body.append(div2)
for_getting_alllinks(all_links1)


div3=soup.new_tag("div",id="step3-wrraper")

# all status codes 
def step3():
    title_status=soup.new_tag("h2")
    title_status.string="ALL STATUSCODES AND TITLES"
    body.append(title_status)
    with open("main_links.txt", "r",encoding="utf-8") as o:
        for line in o.readlines():
            try:
                url = line.strip()
                response = requests.get(url)
                status = response.status_code
                # print(status)
                str_status=str(status)
                total=str(url+"  -  statuscode : "+str_status)
                p_status=soup.new_tag("p",id="stuts")
                p_status.string=total
                div3.append(p_status)
            except Exception as e:
                print("An error occurred:", e)

step3()

#get the title of website
def title():
    o=open("main_links.txt",'r',encoding="utf-8")
    for i in o.readlines():
        s=i.strip()
        try:

            respons=requests.get(s)
            soup=BeautifulSoup(respons.content,"html.parser")
            title=soup.title.string
            # print(reverse_farsi_word(title))
            p_title=soup.new_tag("p",id="titles")
            p_title.string=title
            div3.append(p_title)
        except:
            print("there is no title!!!")
            pass
            
title()    
body.append(div3)

# getting all ip
def step4(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[-1]
        return (url, ip_addresses)
    except Exception as e:
        print("Error:", e)
        return (url, [])

with open("main_links.txt", "r") as f:
    unique_ip_urls = set()
    unique_ips = set()

    p_ipt = soup.new_tag("h2")
    p_ipt.string = "ALL IP"
    body.append(p_ipt)
    div1=soup.new_tag("div",id="ips-wrraper")
    body.append(div1)

    for line in f:
        line = line.strip()
        url, ips = step4(line)
        if ips:
            for ip in ips:
                if ip not in unique_ips:
                    unique_ips.add(ip)
                    unique_ip_urls.add((url, ip))
                    p_ip = soup.new_tag("p",id="ip")
                    p_ip.string = f"{url} - ip: {ip}"
                    div1.append(p_ip)
        else:
            print("No IP found for:", line)

    with open("new_ip.txt", "w") as o:
        for unique_ip in unique_ips:
            o.write(unique_ip + "\n")

    with open("new_ip_with_urls.txt", "w") as o:
        for url, ip in unique_ip_urls:
            o.write(f"{url} - ip: {ip}\n")

step4(real_url)


#checking all ports IP
def step5():
    p_portD = soup.new_tag("h2")
    p_portD.string = "ALL PORT"
    body.append(p_portD)
    div1=soup.new_tag("div",id="ports-wrraper")
    body.append(div1)
    try:
        with open("new_ip.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue  
                print("Scanning IP:", line)   
                
                ip = line
                
                common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]
                
                for port in common_ports:  
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)  
                    try:
                        result = sock.connect_ex((ip, port))
                        if result == 0:
                            # print("Port {} is open".format(port))
                            p_port = soup.new_tag("p",id="ports")
                            reversP = str(ip + " - : Port {} is open".format(port))
                            p_port.string = reversP
                            div1.append(p_port)
                        else:
                            # print("Port {} is closed".format(port))
                            p_portc = soup.new_tag("p")
                            reversPc = str(ip + " - : Port {} is closed".format(port))
                            p_portc.string = reversPc
                            div1.append(p_portc)
                    except Exception as e:
                        print("Error scanning port {}: {}".format(port, e))  
                    finally:
                        sock.close()
    except Exception as e:
        print("Error:", e)  

step5()

# getting all phonenumbers and emails
def step6():
    p_re = soup.new_tag("h2")
    p_re.string = "ALL EMAILs AND PHONE NUMBERs"
    body.append(p_re)
    div1=soup.new_tag("div",id="regex-wrraper")
    body.append(div1)

    with open("main_links.txt", "r") as f:
        for line in f:
            line = line.strip()
            try:
                response = requests.get(line)
                response.raise_for_status() 
                html_text = response.text
                
                pattern_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
                pattern_phone_English = r"09\d{9}"    
                pattern_phone_Persian = r"۰۹\d{9}"    
                pattern_tel_English = r"025\d{6,8}|021\d{6,8}"    
                pattern_tel_combined = r"۰۲۵\d{6,8}|۰۲۱\d{6,8}"

                emails = re.findall(pattern_email, html_text)
                phones = re.findall(pattern_phone_English, html_text) + \
                         re.findall(pattern_phone_Persian, html_text) + \
                         re.findall(pattern_tel_English, html_text) + \
                         re.findall(pattern_tel_combined, html_text)

                if emails:
                    print("Email(s) found:", emails)
                    p_reEma = soup.new_tag("p",id="emails")
                    revers_reEMA = str(emails)
                    p_reEma.string = revers_reEMA
                    div1.append(p_reEma)
                else:
                    print("No email found")

                if phones:
                    print("Phone number(s) found:", phones)
                    p_rePH = soup.new_tag("p",id="phons")
                    revers_rePH = str(phones)
                    p_rePH.string = revers_rePH
                    div1.append(p_rePH)
                else:
                    print("No phone number found")

            except requests.RequestException as e:
                print(f"Error accessing {line}: {e}")

step6()


def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def step7():
    p_Who = soup.new_tag("h2")
    p_Who.string = "ALL Details"
    body.append(p_Who)
    div1=soup.new_tag("div",id="whois-wrraper")
    body.append(div1)

    
    with open("main_links.txt", "r") as f:
        for line in f:
            line = line.strip()
            domain = get_domain(line)
            try:
                all_information = whois.whois(domain)
                print(all_information)
                
                p_WhoE = soup.new_tag("p",id="infor")
                revers_Who = str(all_information)
                p_WhoE.string = revers_Who
                div1.append(p_WhoE)
            except Exception as e:
                print(f"Error processing {line}: {e}")

step7()

def img():
    with open("main_links.txt", "r") as s:
            for lines in s:
                link = lines.strip()
                try:
                    response = requests.get(link)
                    response.raise_for_status() 

                    soup = BeautifulSoup(response.text, 'html.parser')
                    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
                    image_folder = os.path.join(desktop_path, 'downloaded_images')

                    for img_tag in soup.find_all('img'):
                        img_url = img_tag.get('src')
                        if img_url and img_url.startswith('http'):
                            img_name = os.path.basename(urlparse(img_url).path)
                            img_content = requests.get(img_url).content
                            img_path = os.path.join(image_folder, img_name)
                            with open(img_path, 'wb') as img_file:
                                img_file.write(img_content)
                            print(f"Image '{img_name}' downloaded successfully from: {link}")

                except requests.exceptions.RequestException as e:

                    print(f"Error occurred for link {link}: {e}")
                    continue 

img()

def capture_screenshots(links):
    desktop_path = Path.home() / 'Desktop'
    output_directory = desktop_path / 'gowitness_screenshots'

    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)

    os.makedirs(output_directory, exist_ok=True)

    gowitness_path = r'C:\\SCR_GG\\gowitness-2.5.1-windows-amd64.exe'

    for link in links:
        subprocess.run([gowitness_path, 'single', link, '-P', str(output_directory)])

    print(f"Screenshots saved in {output_directory}")

def read_links_from_file(file_path):
    links = []
    with open(file_path, 'r') as file:
        for line in file:
            links.append(line.strip())
    return links

links_file_path = 'main_links.txt'

links = read_links_from_file(links_file_path)

capture_screenshots(links)


divwapp=soup.new_tag("div",id="wapp_wrraper")
body.append(divwapp)

def step12():
    p_wapp = soup.new_tag("h2")
    p_wapp.string = "ALL TECHNOLIGIEs"
    body.append(p_wapp)
    wap = Wappalyzer.latest()
    try : 
        web = WebPage.new_from_url(real_url)
        technoligies = wap.analyze(web)
        for t in technoligies:
            # print("technoligies detected : {}".format(t))
            p_wapa = soup.new_tag("p")
            revers_wapp = str(real_url + " - : technoligies detected : {}".format(t))
            p_wapa.string = revers_wapp
            divwapp.append(p_wapa)
    except Exception as e:
        print("ERROR!!!" , e)

if __name__ == '__main__':
        try:
            step12()
        except KeyboardInterrupt:
            print("bye")
            exit()


step12()
        

def on_exit():
    print("Mission Accomplished")
atexit.register(on_exit)

end_time = datetime.datetime.now()
save_project_time(project_name, start_time, end_time)

a=soup.new_tag("a",href="#",id="go_up")
a.string="UP"
body.append(a)

time_html=soup.new_tag("div",id="time_wrraper") 
f = open("project_times.txt", "r") 
pp=f.read() 
time_html.append(pp) 
body.append(time_html)

script=soup.new_tag("script",src="./js.js")
body.append(script)

file_name = "index.html"
with open(file_name, "w",encoding="utf-8") as file:
    file.write(str(soup.prettify()))
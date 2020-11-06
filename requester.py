import requests
import sys

def requester():
    print("-\t-\t-\nWelcome to this unnamed tool!\nFor help use the -h option.\nUsage: <script> <tested URL without the protocol prefix>\n-\t-\t-")
    if len(sys.argv) != 2:
        print(">> Error: Argument error! For help input: \'<script> -h\'")
        exit()
    if sys.argv[1] == "-h":
        print("This software has been developed with the support of the Government of Smexopolis!\n")
        exit()
    host_url = sys.argv[1]
    headers = {"user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    if "http://" in host_url or "https://" in host_url:
        print(">> Error: Provide the URL without the protocol specified!")
        exit()
    try:
        print(f">> Testing: http://{host_url}/")
        r = requests.get(f"http://{host_url}/", allow_redirects=False, timeout=2, headers=headers)
        response_handler(r)
    except requests.exceptions.Timeout:
        print(">> Error: http request timed out!")
    except:
        print(f">> Error: an error has occurred. Sorry.")
    print("-\t-\t-")
    try:
        print(f">> Testing: https://{host_url}/")
        r = requests.get(f"https://{host_url}/", allow_redirects=False, timeout=2, headers=headers)
        response_handler(r)
    except requests.exceptions.Timeout:
        print(">> Error: https request timed out!")
    except requests.exceptions.SSLError as e:
        print(f">> Error: secure connection failed due to an error:\n{e}")
    except:
        print(">> Error: an error has occurred. Sorry.")

def response_handler(request):
    print(f"Response status is: {request.status_code}")
    if str(request.status_code)[0] == "2":
        print("Server header: {0}".format(request.headers.get("server", "Not found")))
        print("Content length is: {0}".format(len(request.content)))
    if str(request.status_code)[0] == "3":
        print("Server header: {0}".format(request.headers.get("server", "Not found")))
        print("Location header: {0}".format(request.headers.get("location", "Not found")))
    if str(request.status_code)[0] == "4":
        print("Server header: {0}".format(request.headers.get("server", "Not found")))
    if str(request.status_code)[0] == "5":
        print("Server header: {0}".format(request.headers.get("server", "Not found")))

if __name__ == "__main__":
    requester()
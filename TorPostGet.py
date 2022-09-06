# Developed by Lateraluz++
# 11-12-2021

# In order to use connection and either send or post data follow:
# 1- Close Tor Browser    
# 2- Search and open file in tor torrc. Edit file with notepad/notepadd++
# 3- Add at the end of file 
#    a- SocksPort 9050
#    b- HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
#    c- SocksPort 9050
# 4- Open Tor Browser and connecto to network 
# 5- Test port 9050 using curl
#    a- curl -v --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/

# 06-09-2022
# There was a error : "Missing dependencies for SOCKS support" that is fixed installing: 
# c:\pip install PySocks
#
# CURL Testing
# POST: 
# curl -v --socks5 localhost:9050 --socks5-hostname localhost:9050  -X POST https://httpbin.org/post
# GET:
# curl -v --socks5 localhost:9050 --socks5-hostname localhost:9050  https://www.wikipedia.org


import requests
import random


_HEADER_USER_AGENT= [
     'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/ '   ]


def Tor():
     
    myHeaders = {"Accept": "application/json",
                 "User-Agent": _HEADER_USER_AGENT[0]} 
    url1 ="https://www.wikipedia.com"
    url2="https://httpbin.org/post"
    
    # Post Parameters 
    data = {"q":"gfsdgsdfgsdfgsdfgsdfgsdf" }    
            
    
    # Configure session
    s = requests.session()    
    s.proxies['http']  = 'socks5h://127.0.0.1:9050'
    s.proxies['https'] = 'socks5h://127.0.0.1:9050'    

    try:
        # Get data    
        get_response = requests.get(url1, headers = myHeaders)   
         
        print(f"GET Response code : {get_response.status_code}. 200 means OK")    
        #print("Data :"+ response.text)  

        # Post data
        post_response= s.post(url2,  data, headers = myHeaders)                    
        print(f"POST Response code : {post_response.status_code}. 200 means OK")
        print("Data :"+ post_response.text)   
    except RuntimeError as err:
        print("Error")        
        print(f"Catched Unexpected error {err=}, {type(err)=}")    
    

def main():    
    Tor()
    
if __name__ == "__main__":
    main()

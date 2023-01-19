# Tor-Post-Get
Send data thru Tor network


In order to use connection and either send or post data follow:
1. Close Tor Browser    
2. Search and open file in tor torrc. Edit file with notepad/notepadd++
3. Add at the end of file 
   - SocksPort 9050
   - HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C
   - SocksPort 9050
4. Open Tor Browser and connecto to network 
5. Test port 9050 using curl
   - curl -v --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/
6. In order to execute this Python program, MUST install ---> pip install PySocks  to avoid error "Missing dependencies for SOCKS support"


## License
Feel free to improve it!

<BR>
  <BR>
**knowledge belongs to humanity**, *Pascal*

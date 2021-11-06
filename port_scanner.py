#-*-coding:utf8;-*-
#qpy:3
#qpy:console
print(
	"   $ Port Scanner By Mo $")

	    
import socket
def scan_ip(ip,ports):
    host=socket.gethostbyname(ip)
    print("$"*40)
    print(["Scanning " + host + " ....."])
    print("$"*40)
    for port in ports:
        port=int(port)
        
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect_ex((ip,port))
            print("[+] Port "+str(port)," ----> "+"is open ")
        except:
             print("[+] Port "+str(port)," ----> "+"is close ")
        finally:
            s.close()
    print("\n[X] Scan finished!!------> (:")
    print("-"*40)
ip=input("\nenter the ip you want to scan :")
ports=input("\nenter the port you want to scan : ")
if ports=="":
    ports=range(1,25)
ports=ports.split(",")
scan_ip(ip,ports

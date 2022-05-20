#UMC by Hope Destruction

import platform
import time
import os
import sys

def clearterminal():
    if platform.system() == 'Windows':
    #Clear CMD for Windows
        import os
        clear = lambda: os.system('cls')
        clear()
    else:
        #Clear Terminal for Linux
        import os
        clear = lambda: os.system('clear')
        clear()

clearterminal()

version = str("0.13 Open Beta")
miners = ["nanominer"]
coins = ["ERG | ERGO"]
pools = ["Flypool"]

print(" ")
print("Welcome to UMC (Universal Miner Configurator) version " + version)
print("by Hope Destruction")
time.sleep(1)
print(" ")
print("WARNING. UMC is currently in Beta; you can find a really limited experience compared to what it will be in the future, keep it in mind.")
time.sleep(3)
print(" ")
print("Available miner configurations:")
for miner in miners:
    print(" - " + miner)
print(" ")
time.sleep(1)
print(" ")
print("[X] " + miners[0] + " selected")
print(" ")

os.system("pause")
clearterminal()


print("Select the coin to mine")
for coin in coins:
    print(" - " + coin)
print(" ")
time.sleep(1)
print("[X] " + coins[0] + " selected")
print(" ")

os.system("pause")
clearterminal()

#Pool
print("Available mining pools:")
for pool in pools:
    print(" - " + pool)
print(" ")
time.sleep(1)
print(" ")
print("[X] " + pools[0] + " selected")
print(" ")


os.system("pause")
clearterminal()


address = input("Enter your address (You can paste it with the right click mouse button): ")
clearterminal()

workername = input("Enter the name for your worker (GPU): ")
clearterminal()

f = open("config.ini", "w+")
f.write("[autolykos]\n")
f.write("wallet = " + address + "\n")
f.write("rigName = " + workername + "\n")
f.write("pool1 = stratum-ergo.flypool.org:3333\n")
f.close()


print("That's it!")
print(" ")
time.sleep(1)
print("The config.ini file has been successfully created in the same place where you ran this program, all you have to do is move it to the directory where you have your miner and execute nanominer.exe")
time.sleep(2)
print(" ")
print("You can check your mining stats here :) https://ergo.flypool.org/miners/" + address + "/dashboard")
print(" ")
print("Happy mining!")
print(" ")
os.system("pause")

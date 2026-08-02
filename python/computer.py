import serial
import time
import serial.tools.list_ports
import pyfiglet
import os 
from colorama import Fore, Back, Style, init


init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.GREEN + Style.DIM + ("подключаемся к нужному порту: com"))

def find_wemos():

    ports = serial.tools.list_ports.comports()

    for port in ports:

        description = port.description.lower()

        # Wemos D1 mini обычно CH340 или CP210x
        if (
            "ch340" in description or
            "cp210" in description or
            "usb serial" in description
        ):
            return port.device

    return None



port = find_wemos()


if port is None:
    print(Fore.GREEN + Style.DIM + ("Wemos не найден!"))
    exit()

print(Fore.GREEN + Style.DIM + f"Найден Wemos: {port}")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
arduino = serial.Serial(
    port=port,  
    baudrate=115200,
    timeout=1
)

def send(command):
    arduino.write((command + "\n").encode())

    answer = arduino.readline().decode().strip()

    print(Fore.GREEN + Style.BRIGHT + ( answer))

def send_multi(command):
    arduino.write((command + "\n").encode())

    while True:
        line = arduino.readline().decode(errors="ignore").strip()

        if not line:
            continue

        if line == "END":
            break

        print(line)

while True:
    print(Fore.GREEN + Style.BRIGHT + r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣾⣶⣹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡿⠿⢋⠁⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠶⡒⠊⠁⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠟⡇⠀⠀⠀⠈⣿⣿⡟⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠒⢤⣰⡇⠀⠀⠀⠀⠻⠿⢀⡼⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣖⠁⠀⠀⠹⣇⠀⠀⠀⠀⠀⢠⠋⠀⠈⠛⠛⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢹⣆⠀⠀⠀⢀⠇⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⣄⣀⣸⠛⢓⣦⣤⣼⠀⠀⠀⠀⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⡧⠤⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠿⠿⠿⠛⢿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print(Fore.GREEN + Style.BRIGHT + ("by president"))
    print(Fore.GREEN + Style.BRIGHT + ("1. NRF24          2. SUB-GHZ           3. IR"))
    print(Fore.GREEN + Style.BRIGHT + ("       4. WI-FI           5. SETTINGS"))
    cmd = input("> ")

    if cmd == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⣦⠀⠀⠀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣗⣴⣦⣤⡙⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⣿⣿⣾⣿⣷⣦⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⣿⣿⣿⣿⣿⡿⠙⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠋⠀⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⣿⠈⠏⢻⣿⡿⠟⠋⠉⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⣟⠀⠀⠈⢿⣇⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡇⠀⠀⠀⢻⡇⠀⠀⠈⣿⣶⣄⠀⢸⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⡏⠀⠀⠀⠉⠉⠉⠀⠈⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """)
        print(Fore.GREEN + Style.BRIGHT + ("1.scanapp               2.scansta             3.deauth attack"))
        print(Fore.GREEN + Style.BRIGHT + ("          4.spectrum          5.evil portal                B. Back"))
        wifi = input("> ")
        if wifi == "1":
            send_multi("scanapp")
            input("\nНажмите Enter чтобы вернуться...")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        if wifi == "2":
            pass
            input("\nНажмите Enter чтобы вернуться...")
            os.system('cls' if os.name == 'nt' else 'clear')
        if wifi == "4":
            send_multi("wifianalyzer")
            input("\nНажмите Enter чтобы вернуться...")
            os.system('cls' if os.name == 'nt' else 'clear')
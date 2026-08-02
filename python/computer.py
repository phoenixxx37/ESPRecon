import serial
import time
import serial.tools.list_ports
import pyfiglet
import os 
import cfg
from colorama import Fore, Back, Style, init

init(autoreset=True)
cfg.clear()

print(cfg.color1 + cfg.style + ("подключаемся к нужному порту: com"))
cfg.port = cfg.find_wemos()


if cfg.port is None:
    print(cfg.color1 + cfg.style + ("Wemos не найден!"))
    exit()

print(cfg.color1 + cfg.style + f"Найден Wemos: {cfg.port}")
time.sleep(3)
cfg.clear()





while True:
    cfg.draw_pingvy()
    print(cfg.color1 + cfg.style + ("by president"))
    print(cfg.color1 + cfg.style + ("1. NRF24          2. SUB-GHZ           3. IR"))
    print(cfg.color1 + cfg.style + ("       4. WI-FI           5. SETTINGS           6.OTHER"))
    cmd = input("> ")
    if cmd == 1:
        cfg.clear()
        cfg.draw_dog()
        print(cfg.color1 + cfg.style + ("1.JAMMING         2.SPECTRUM"))
        nrf = input("> ")
        if nrf == 1:
            print("not worked...")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
        elif nrf == 2:
            print("not worked...")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
    if cmd == 2:
        cfg.clear()
        cfg.draw_dog()
        print(cfg.color1 + cfg.style + ("1.READ   2.SEND    3.JAMMING     4.SPECTRUM"))
        subghz = input("> ")
        if subghz == 1:
            print("not worked...")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
        elif subghz == 2:
            print("not worked...")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
    if cmd == "4":
        cfg.clear()
        cfg.draw_dog()
        print(cfg.color1 + cfg.style + ("1.scanapp               2.scansta             3.deauth attack"))
        print(cfg.color1 + cfg.style + ("          4.spectrum          5.evil portal                B. Back"))
        wifi = input("> ")
        if wifi == "1":
            cfg.send_multi("scanapp")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
            
        if wifi == "2":
            
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
        if wifi == "4":
            cfg.send_multi("wifianalyzer")
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
    elif cmd == "5":
        cfg.clear()
        print(cfg.color1 + cfg.style + "1. COLOR   2. STYLE")
        settings = input("> ").strip()
        
        if settings == "1":
            colors = {
                "red": Fore.RED,
                "green": Fore.GREEN,
                "yellow": Fore.YELLOW,
                "blue": Fore.BLUE,
                "magenta": Fore.MAGENTA,
                "cyan": Fore.CYAN,
                "white": Fore.WHITE,
                "black": Fore.BLACK
            }
            print(cfg.color1 + "Доступные цвета:")
            for name in colors:
                print(cfg.color1 + f"- {name}")
            
            choice = input("Цвет: ").strip().lower()
            if choice in colors:
                cfg.color1 = colors[choice]
                print(cfg.color1 + "✅ Цвет изменён!")
            else:
                print(cfg.color1 + "❌ Неверный цвет")
            
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
        
        elif settings == "2":
            styles = {
                "dim": Style.DIM,
                "bright": Style.BRIGHT,
                "normal": Style.NORMAL
            }
            print(cfg.color1 + "Доступные стили:")
            for name in styles:
                print(cfg.color1 + f"- {name}")
            
            choice = input("Стиль: ").strip().lower()
            if choice in styles:
                cfg.style = styles[choice]
                print(cfg.color1 + "✅ Стиль изменён!")
            else:
                print(cfg.color1 + "❌ Неверный стиль")
            
            input("\nНажмите Enter чтобы вернуться...")
            cfg.clear()
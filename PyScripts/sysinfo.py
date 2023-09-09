#!/usr/bin/env python
import os
import time
import platform
import psutil


def main():
    os.system("clear")
    print("\t" + "#" * 80 + "#")
    print("\t" + "#\033[91m\t[*]System Information[*]\033[0m\t\t" + "#")
    print("\t" + "#" * 80 + "#")
    print("")

    freq = psutil.cpu_freq()
    print("\033[91m\tTime: \033[0m" + time.ctime())
    print("\033[91m\tCurrent directory: \033[0m" + os.getcwd())
    print("\033[91m\tOperation System: \033[0m" + platform.system())
    print("\033[91m\tNode: \033[0m" + platform.node())
    print("\033[91m\tOS Version: \033[0m" + platform.uname()[3])
    print("\033[91m\tSystem Type: \033[0m" + platform.architecture()[0])
    print("\033")
    print("\033[91m\tCPU Cores: \033[0m" + str(psutil.cpu_count(logical=False)))
    print("\033[91m\tCPU Cores: \033[0m" + str(psutil.cpu_freq(percpu=True)))
    print("\033[91m\tCPU %: \033[0m" + str(psutil.cpu_percent()))

if __name__ == "__main__":
    main()
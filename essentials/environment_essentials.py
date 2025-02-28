#!/user/env/python3

#external libraries
import os
import shutil
import subprocess
import sys
import time

#colors
green = "\033[38;2;60;236;133m"
red = "\033[31m"
blue = "\033[34m"
yellow = "\033[33m"
pink = "\033[38;5;213m"
turquoise = "\033[36m"
gray = "\033[37m"
end = "\033[0m"

def start_scan_animation():
    time_sleeping = .1
    phrase = f'starting scan...'

    print('[', end = '\r')
    time.sleep(time_sleeping)
    print(f'[{green}+{end} ', end = '\r')
    time.sleep(time_sleeping)
    print(f'[{green}+{end}]', end = '\r')

    for character in range(len(phrase) + 1):
        print(f'[{green}+{end}]', phrase[:character], end = '\r')
        time.sleep(time_sleeping)
    time.sleep(.5)

class required_environment_checker:
    def __init__(self, main_self):
        self = main_self
    
        required_environment_checker.operative_system_clasificator(self)
        subprocess.run(["clear"])

        if not self.verbose:
            sys.stdout = sys.__stdout__

        start_scan_animation()

        time_sleeping_logo = .05
        print(self.green)  
        time.sleep(time_sleeping_logo)
        print('\n\n\a ▄▄▄▄ ▓██   ██▓')
        time.sleep(time_sleeping_logo)
        print('▓█████▄▒██  ██▒')
        time.sleep(time_sleeping_logo)
        print('▒██▒ ▄██▒██ ██░')
        time.sleep(time_sleeping_logo)
        print('▒██░█▀  ░ ▐██▓░')
        time.sleep(time_sleeping_logo)
        print('░▓█  ▀█▓░ ██▒▓░')
        time.sleep(time_sleeping_logo)
        print('░▒▓███▀▒ ██▒▒▒██▓ ▄▄▄       ██▀███   █     █░ ██▓ ███▄    █  ')
        time.sleep(time_sleeping_logo)
        print('▒░▒   ░▓██ ░▒░██▒▒████▄    ▓██ ▒ ██▒▓█░ █ ░█░▓██▒ ██ ▀█   █  ')
        time.sleep(time_sleeping_logo)
        print(' ░    ░▒ ▒ ░░▒██▒▒██  ▀█▄  ▓██ ░▄█ ▒▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒  ')
        time.sleep(time_sleeping_logo)
        print(' ░     ░ ░   ░██░░██▄▄▄▄██ ▒██▀▀█▄  ░█░ █ ░█ ░██░▓██▒  ▐▌██▒   ')
        time.sleep(time_sleeping_logo)
        print('      ░░ ░   ░██░ ▓█   ▓██▒░██▓ ▒██▒░░██▒██▓ ░██░▒██░   ▓██░   ')
        time.sleep(time_sleeping_logo)
        print('             ░▓   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ')
        time.sleep(time_sleeping_logo)
        print('             ▒ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ▒ ░ ░   ▒ ░░ ░░   ░ ▒░')
        time.sleep(time_sleeping_logo)
        print('             ▒ ░  ░   ▒     ░░   ░   ░   ░   ▒ ░   ░   ░ ░ ')
        time.sleep(time_sleeping_logo)
        print('             ░        ░  ░   ░         ░     ░           ░\n\n')
        time.sleep(2)
        print(self.end)

        if not self.verbose:
            sys.stdout = open(os.devnull, 'w')

        required_environment_checker.utilities_tester(self)

    class operative_system_clasificator:
        def __init__(self, main_self):
            self = main_self

            if self.operative_system != "Linux":
                sys.stdout = sys.__stdout__

                print(f'\n{self.red}[!]{self.end} os not supported... ({self.green}good luck{self.end})\n')
                print('\033[?25h', end='\r')
                sys.exit(1)

    class utilities_tester:
        def __init__(self, main_self):
            self = main_self

            self.utilities_to_test = ['clear', 'groups', 'whoami']
            self.utilities_not_found_list = []

            for utility in self.utilities_to_test:
                utility_tested = shutil.which(utility)

                if utility_tested:
                    pass
                else:
                    self.utilities_not_found_list.append(utility)

            if self.utilities_not_found_list:
                sys.stdout = sys.__stdout__

                self.utilities_not_found_text = f"{self.end},{self.yellow} ".join(self.utilities_not_found_list)
                print(f'\n{self.red}[!]{self.end} utilities not found (please {self.blue}install{self.end}) --> {self.yellow}{self.utilities_not_found_text}{self.end}\n')
                
                print('\033[?25h', end='\r')
                sys.exit(1)

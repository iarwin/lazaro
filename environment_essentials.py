#!/user/env/python3

#external libraries
import os
import shutil
import subprocess
import sys
import time

class required_environment_checker:
    def __init__(self, main_self):
        self = main_self
    
        required_environment_checker.operative_system_clasificator(self)
        subprocess.run(["clear"])

        if not self.verbose:
            sys.stdout = sys.__stdout__

        print(f'{self.green}[+]{self.end} starting scan...')

        if not self.verbose:
            sys.stdout = open(os.devnull, 'w')

        time.sleep(self.time_sleeping)

        required_environment_checker.utilities_tester(self)

    class operative_system_clasificator:
        def __init__(self, main_self):
            self = main_self

            if self.operative_system != "Linux":
                sys.stdout = sys.__stdout__

                print(f'\n{self.red}[!]{self.end} os not supported... ({self.green}good luck{self.end})\n')
                os.system("tput cnorm")
                sys.exit(1)

    class utilities_tester:
        def __init__(self, main_self):
            self = main_self

            self.utilities_to_test = ['clear', 'groups', 'tput']
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
                
                os.system("tput cnorm")
                sys.exit(1)

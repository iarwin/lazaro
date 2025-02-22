#!/usr/env/python3

#external libraries
import subprocess

class essential_bases_checker:
    def __init__(self, main_self):
        self = main_self
        self.something_changed = False

        print(f'\n{self.blue}╔═════════════════╣  {self.green}BASICS{self.blue}  ╠═════════════════╗')
        print(f'{self.blue}║\t\t\t\t\t       ║{self.end}')

        essential_bases_checker.root_checker(self)
        essential_bases_checker.groups_checker(self)
        
        if not self.something_changed:
            print(f'{self.blue}║{self.end}  [{self.green}+{self.end}] nothing was found')
        
        print(f'{self.blue}║{self.end}')
        print(f'{self.blue}╚═══════╝{self.end}')

    class root_checker:
        def __init__(self, main_self):
            self = main_self

            if self.user == "root":
                summary_line = f'{self.blue}║{self.end}  [{self.red}!{self.end}] you idiot, ya already as {self.red}root{self.end} ({self.blue}user{self.end})'
                self.summary.append(summary_line)

                print(summary_line)
                print(f'{self.blue}║{self.end}')
                self.something_changed = True

    class groups_checker:
        def __init__(self, main_self):
            self = main_self
            active_exploitable_groups = []

            self.exploitable_groups = ['docker', 'root', 'staff', 'sudo', 'sys', 'users', 'wheel']

            for group in self.groups:

                if group in self.exploitable_groups:
                    active_exploitable_groups.append(group)
                   
            if active_exploitable_groups:        
                for group in active_exploitable_groups:
                    helper = ''

                    if group == 'docker':
                        try:
                            command = 'docker run -d --rm --privileged -v /:/host -v /etc:/etc -v /proc:/proc -it ubuntu'
                            output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT).decode('utf-8')

                            color = f'{self.red}'; symbol = '!'
                            helper = f' ({self.green}run{self.end} "{self.red}{" ".join(command.split()[:2] + command.split()[3:])}{self.end}")'

                        except subprocess.CalledProcessError:
                            try:
                                command = 'docker run -d -it -v /:/mnt alpine chroot /mnt'
                                output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT).decode('utf-8')

                                color = f'{self.red}'; symbol = '!'
                                helper = f' ({self.green}run{self.end} "{self.red}{" ".join(command.split()[:2] + command.split()[3:])}{self.end}")'

                            except subprocess.CalledProcessError:
                                active_exploitable_groups.remove(group)
                                print("\033[2A")
                                continue

                    elif group == 'sudo' or group == 'wheel':
                        try:
                            sudo_list_result = subprocess.check_output(['sudo', '-n', '-l'], stderr=subprocess.STDOUT).decode('utf-8')

                            if "no matches" in sudo_list_result or "not allowed" in sudo_list_result or "may not run" in sudo_list_result:
                                continue
                            elif not sudo_list_result.strip():
                                continue
                            else:
                                color = f'{self.red}'; symbol = '!'
                                helper = ''

                        except subprocess.CalledProcessError as error:
                            if 'password' in error.output.decode('utf-8').lower():
                                color = f'{self.pink}'; symbol = '*'
                                helper = ''

                    elif group == 'root':
                        color = f'{self.red}'; symbol = '!'
                        helper_root = ''

                    else:
                        color = 'fix this'
                        symbol = '/this too'

                    summary_line = f'{self.blue}║{self.end}  [{color}{symbol}{self.end}] {color}{group}{self.end} ({self.blue}group{self.end}){helper}'
                    self.summary.append(summary_line)

                    print(summary_line)
                    self.something_changed = True

                    if group != active_exploitable_groups[-1]:
                        print(f'{self.blue}║{self.end}')

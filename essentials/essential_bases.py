#!/usr/env/python3

#external libraries


class essential_bases_checker:
    def __init__(self, main_self):
        self = main_self

        print(f'\n{self.blue}╔═══════════════╣  {self.green}BASICS{self.blue}  ╠═══════════════╗')
        print(f'{self.blue}║                                          ║{self.end}')
        essential_bases_checker.root_checker(self)
        print(f'{self.blue}║                               {self.end}')
        print(f'{self.blue}╚═══════╝{self.end}')

        print("\n=====GROUPS======")
        essential_bases_checker.groups_checker(self)

    class root_checker:
        def __init__(self, main_self):
            self = main_self

            if self.user == "root":
                summary_line = f'{self.blue}║{self.end}  [{self.purple}*{self.end}] you idiot, ya already {self.purple}root{self.end}'
                print(summary_line)
                self.summary.append(summary_line)

    class groups_checker:
        def __init__(self, main_self):
            self = main_self

            self.exploitable_groups = ['sudo', 'wheel', 'root', 'adm', 'staff', 'docker', 'sys', 'users']

            for group in self.groups:
                if group in self.exploitable_groups:
                    print(group)

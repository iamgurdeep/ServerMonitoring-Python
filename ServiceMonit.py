import yaml
import platform
import subprocess


class Monitor:
    def __init__(self, f):
        self.f = f
        with open(self.f) as f:
            self.data = yaml.load(f)
        for self.os, self.configs in self.data['OS'].items():
            if platform.system() is 'Windows':
                if self.os == 'Windows':
                    self.services = self.configs['Services']
                    win_monitor(self.services)
            elif platform.os is 'Unix':
                if self.os == 'Unix':
                    self.services = self.configs['Services']
                    unix_monitor(self.services)
            else:
                print('Platform is not supported as of now ')


def unix_monitor(services):
    print(platform.system())


def win_monitor(services):
    for service in services:
        call = 'TASKLIST', '/FI', 'imagename eq %s' % service
        # use buildin check_output right away
        output = subprocess.check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split('\r\n')[-1]
        # because Fail message could be translated
        # print(service + '  returns ', last_line.lower().startswith(service.lower()))
        if last_line.lower().startswith(service.lower()):
            print(service + ' Service is running ')
        else:
            print(service + ' service is not running')
        # yield last_line.lower().startswith(service.lower())


config_data = Monitor('config.yaml')

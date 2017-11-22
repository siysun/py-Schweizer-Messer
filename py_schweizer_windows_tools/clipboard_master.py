import os
import sys


class WindowsClipBoardMaster:
    def __init__(self, ip_initial):
        self.clipboard_content = ""
        self.ip_initial = ip_initial

    def __copy_to_clipboard(self):
        command = 'echo ' + self.clipboard_content + '| clip'
        os.system(command)

    def __clear_clipboard(self):
        command = '@echo off| clip'
        os.system(command)

    def put_ip_to_clipboard(self):
        list_hits = []
        command = 'ipconfig |findstr /c:": %s"' % self.ip_initial
        list_output = os.popen(command).readlines()
        if len(list_output) == 0:
            sys.stdout.write("No ip initial matched")
            self.clipboard_content = "No ip initial matched"
        else:
            for ip_info in list_output:
                if "IPv4" in ip_info:
                    list_hits.append(ip_info.split(":")[1].strip())
                else:
                    pass
            self.clipboard_content = ",".join(list_hits)
            sys.stdout.write("ip initial '%s' matches:\n%s" % (ip_initial, clip.clipboard_content))
        self.__copy_to_clipboard()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ip_initial = sys.argv[1]
        try:
            clip = WindowsClipBoardMaster(ip_initial)
            clip.put_ip_to_clipboard()
        except IndexError as e:
            sys.stdout.write("No ip initial matched")
    else:
        sys.stdout.write("Input ip initial as the param\ne.g:python ip_to_clipboard.py 172")

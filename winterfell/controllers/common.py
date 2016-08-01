import re
import subprocess


def check_call(command):
    print command
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    p.wait()
    if p.returncode != 0:
        raise Exception
    return True


def check_output(command):
    result = []
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        result.append(line)
    return result


def is_cidr(cidr):
    cidr_re = r'^([0-9]{1,3}\.){3}[0-9]{1,3}(/(8|16|24))'
    if re.match(cidr_re, cidr):
        return True
    else:
        return False

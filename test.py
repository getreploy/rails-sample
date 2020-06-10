import subprocess
import os

is_dir = False
if os.path.isdir("270921786"):
    is_dir = True

print(is_dir)

if not is_dir:
    cmd = ['git', 'clone', 'https://fc723a84133d367841bec6eef2b74df3c7b2843b@github.com/getreploy/rails-sample.git', '270921786']
    try:
        out = subprocess.check_output(cmd)
    except Exception as e:
        print("error cloning directory")
        print(e.output.decode())
        exit(0)


output = subprocess.check_output('ls -a && pwd && cd 270921786 && git checkout 4238067', shell=True)
print(output)

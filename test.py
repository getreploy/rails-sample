import subprocess

cmd = ['git', 'clone', 'https://fc723a84133d367841bec6eef2b74df3c7b2843b@github.com/getreploy/rails-sample.git', '270921786']
try:
    out = subprocess.check_output(cmd)
except Exception as e:
    print("error cloning directory")
    print(e.output.decode())
    exit(0)



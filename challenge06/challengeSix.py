import subprocess

who = subprocess.run("whoami", capture_output=True).stdout
ip = subprocess.run(["ip", "a"], capture_output=True).stdout
lshw = subprocess.run(["lshw", "-short"], capture_output=True).stdout

# How to remove b' \n?
print(who)
print(ip)
print(lshw)
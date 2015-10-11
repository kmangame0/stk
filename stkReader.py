import subprocess

process = subprocess.Popen(['supertuxkart.app'], shell=False,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
#process.stdin.write("Some String")
process.stdin.close()  # <-- Makes sure the external app gets an EOF while
                       #     reading its input stream.
for line in process.stdout.readlines():
    print line
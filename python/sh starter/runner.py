import subprocess, os, signal
import readline

processes = {}

def run_sh_file(file_path):
    process = subprocess.Popen(f"sudo sh /path/to/file/{file_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes[file_path] = process 

def stop_process(file_path):
    if file_path in processes:
        process = processes[file_path]
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            print(f"Process {file_path} stopped.\n")
        except OSError:
            print(f"Process {file_path} already stopped.\n")
    else:
        print(f"No process running for {file_path}.\n")

for i in range(99):
    user = input("gm:sgm xm:sxm - mnrs : ")
    if user == "gm":
        run_sh_file("gminer.sh")
        print("gminer is running")
    elif user == "sgm":
        stop_process("gminer.sh")
        print("gminer is stopped")
    elif user == "xm":
        run_sh_file("xmrig.sh")
        print("xmrig is running")
    elif user == "sxm":
        stop_process("xmrig.sh")
        print("xmrig is stopped")
    elif user == "mnrs":
        run_sh_file("gminer.sh")
        run_sh_file("xmrig.sh")
        print("miners are now running")
    
    # Clear the input buffer
    readline.clear_history()

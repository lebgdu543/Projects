import tkinter as tk
import subprocess, os, signal

processes = {}

def run_sh_file(file_path):
    print(f"Running {file_path}...\n")
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

# Create the main window
root = tk.Tk()
root.title("Runner")

# Button to run gminer.sh
button1 = tk.Button(root, text="  Run gminer  ", command=lambda: run_sh_file("gminer.sh"))
button1.pack()

# Button to stop gminer.sh process
stop_button1 = tk.Button(root, text="  Stop gminer  ", command=lambda: stop_process("gminer.sh"))
stop_button1.pack()

# Button to run xmrig.sh
button2 = tk.Button(root, text="  Run xmrig  ", command=lambda: run_sh_file("xmrig.sh"))
button2.pack()

# Button to stop xmrig.sh process
stop_button2 = tk.Button(root, text="  Stop xmrig  ", command=lambda: stop_process("xmrig.sh"))
stop_button2.pack()

root.mainloop()

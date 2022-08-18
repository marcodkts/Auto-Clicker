import os, psutil


def alreadyRunning():
    PROCNAME = (
        os.path.basename(__file__)
        if ".py" not in os.path.basename(__file__)
        else "python.exe"
    )
    process_list = [proc.name() for proc in psutil.process_iter()]
    if process_list.count(PROCNAME) > 1:
        input("Already running, press enter to exit.")
        exit()

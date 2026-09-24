import psutil
import os
import datetime


def get_system_resources():
    






                                                                                          
    print("██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗")
    print("██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝")
    print("███████║█████╗  ███████║██║     ██║   ███████║    ██║     ███████║█████╗  ██║     █████╔╝ ")
    print("██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ")
    print("██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗")
    print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝")
    cpu_usage = psutil.cpu_percent(interval=2)

    memory = psutil.virtual_memory()
    memory_used = memory.used / (1024**3)
    memory_total = memory.total / (1024**3)

    disk = psutil.disk_usage("/")
    disk_used = disk.used / (1024**3)
    disk_total = disk.total / (1024**3)

    

    return {
        "CPU": f"{cpu_usage:.1f}%",
        "Memory": f"{memory_used:.2f}/{memory_total:.2f} GB",
        "Disk": f"{disk_used:.2f}/{disk_total:.2f} GB"
    }

resource = get_system_resources()
with open("ServerStatusLogs.txt", "a") as f:
    print("\nHere is your report:\n", file=f)


    print("+---------------------------------------+", file=f)

    for name, usage in resource.items():
        label = f"{name} usage:"
        print(f"| {label:<13} {usage:>22} |", file=f)


    print("+---------------------------------------+", file=f)

    print("+---------------------------------------+")
    
    for name, usage in resource.items():
            label = f"{name} usage:"
            print(f"| {label:<13} {usage:>22} |")
    
    
    print("+---------------------------------------+")
    
    print("", file=f)
    ct = datetime.datetime.now()
    print("current time:", ct, file=f)

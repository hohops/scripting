import psutil

def get_system_resources():
    while True:
        try:
            nInterval = float(input("Select a time period to run the check(In seconds): "))
            if 0 < nInterval < 1000000:
                break
            print("Please enter a positive number less than 1,000,000.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    cpu_usage = psutil.cpu_percent(interval=nInterval)

    memory = psutil.virtual_memory()
    memory_used = memory.used / (1024**3)
    memory_total = memory.total / (1024**3)

    disk = psutil.disk_usage("/")
    disk_used = disk.used / (1024**3)
    disk_total = disk.total / (1024**3)


    return {
        "CPU": f"{cpu_usage:.1f}%",
        "Memory": f"{memory_used:.2f}/{memory_total:.2f}" ,
        "Disk": f"{disk_used:.2f}/{disk_total:.2f}"
    }

resource = get_system_resources()
for name, usage in resource.items():

    print("---------------------------")
    print("| "f"{name} usage: {usage}")
print("")

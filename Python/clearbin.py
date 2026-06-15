import winshell


try:   
    winshell.recycle_bin().empty(confirm=False,
          show_progress=False, sound=True)

    print("Recycle Bin is emptied now!")
except:
    print("Recycle Bin is already empty!")
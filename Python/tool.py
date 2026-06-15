import os
import winshell
from datetime import datetime

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

recycleBin_items = list(winshell.recycle_bin())
winshell.recycle_bin().empty(confirm=False,
          show_progress=False, sound=True)
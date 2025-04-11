import math
from pyrogram.types import InlineKeyboardButton

def human_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def get_progress_bar(percentage):
    filled = "●" * int(percentage / 5)
    empty = "○" * (20 - len(filled))
    return f"{filled}{empty} {percentage}%"

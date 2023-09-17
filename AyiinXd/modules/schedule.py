# Credit to Ultroid Teams. 
# this code from Ultroid.


import asyncio
import time
import uuid
from datetime import timedelta

from telethon.tl import functions, types

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string

def ban_time(time_str):
    """Simplify ban time from text"""
    if not any(time_str.endswith(unit) for unit in ("s", "m", "h", "d")):
        time_str += "s"
    unit = time_str[-1]
    time_int = time_str[:-1]
    if not time_int.isdigit():
        raise Exception("Invalid time amount specified.")
    to_return = ""
    if unit == "s":
        to_return = int(time.time() + int(time_int))
    elif unit == "m":
        to_return = int(time.time() + int(time_int) * 60)
    elif unit == "h":
        to_return = int(time.time() + int(time_int) * 60 * 60)
    elif unit == "d":
        to_return = int(time.time() + int(time_int) * 24 * 60 * 60)
    return to_return
  
@ayiin_cmd(pattern="schedule( (.*)|$)", fullsudo=True)
async def schedule(event):
    x = event.pattern_match.group(1).strip()
    xx = await event.get_reply_message()
    if x and not xx:
        y = x.split(" ")[-1]
        k = x.replace(y, "")
        if y.isdigit():
            await event.client.send_message(
                event.chat_id, k, schedule=timedelta(seconds=int(y))
            )
            await event.eor(get_string("schdl_1"), time=5)
        else:
            try:
                z = ban_time(y)
                await event.respond(k, schedule=z)
                await event.eor(get_string("schdl_1"), time=5)
            except BaseException:
                await event.eor(get_string("schdl_2"), time=5)
    elif xx and x:
        if x.isdigit():
            await event.respond(xx, schedule=timedelta(seconds=int(x)))
            await event.eor(get_string("schdl_1"), time=5)
        else:
            try:
                z = ban_time(x)
                await event.respond(xx, schedule=z)
                await event.eor(get_string("schdl_1"), time=5)
            except BaseException:
                await event.eor(get_string("schdl_2"), time=5)
    else:
        return await event.eor(get_string("schdl_2"), time=5)

CMD_HELP.update(
    {
        "schedule": f"**Plugin : **`schedule`\
        \n\n  »  **Perintah :** `{cmd}schedule` <text/reply to msg> <time>\
        \n  »  **Kegunaan : **untuk mengirim pesan terschedule.\
        \n\n  »  **Perintah :** `{cmd}restart`\
        \n  »  **Kegunaan : **untuk menghentikan schedule. \
    "
    }
)

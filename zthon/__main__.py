import contextlib
import sys

import zthon
from zthon import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import mybot
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("SEMO8L")
cmdhr = Config.COMMAND_HAND_LER

print(zthon.__copyright__)
print(f"المرخصة بموجب شروط  {zthon.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("⌭ بـدء تنزيـل سيمو ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("⌭ بـدء تشغيـل البـوت ⌭")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


try:
    LOGS.info("⌭ جـار تفعيـل وضـع الانـلاين ⌭")
    zedub.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم تفعيـل الانـلاين .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐌𝐎 ➖➖")
    print("تـم التنصـيب .. بنجـاح ✓")
    print(
        f"⌔┊تـم تنصيـب سورس سيمو  . . بنجـاح 🧸♥️ \n\n⌔┊تحيـاتي ..  الـمـبـرمـجہ سـمـيـر\n⌔┊قنـاة السـورس ↶.\n🌐┊@SEMO8L "
    )
    print("➖➖ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐌𝐎 ➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    return


zedub.loop.run_until_complete(startup_process())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        zedub.run_until_disconnected()
else:
    zedub.disconnect()

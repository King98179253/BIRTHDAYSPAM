import asyncio
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from OfficialSameer import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, SAM11, SAM12, SAM13, SAM14, SAM15, SAM16, SAM17, SAM18, SAM19, SAM20, SAM21, SAM22, SAM23, SAM24, SAM25, SAM26, SAM27, SAM28, SAM29, SAM30, SAM31, SAM32, SAM33, SAM34, SAM35, SAM36, SAM37, SAM38, SAM39, SAM40, SUDO_USERS
from resources.data import DEADLYSPAM
from .. import CMD_HNDLR as hl
  
    
@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM21.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM22.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM23.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM24.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM25.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM26.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM27.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM28.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM29.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM30.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM31.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM32.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM33.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM34.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM35.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM36.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM37.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM38.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM39.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@SAM40.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def _(e):
    usage = "**Module Name = BIRTHDAY**\n\nCommand:\n\n ..bday <Username of User>\n\nit will continuously birthday until you restart!!."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DEADLYSPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(DEADLYSPAM) == 1:
            user = str(DEADLYSPAM[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"I can't bdy @ZINDA_H_TU_MERE_LIYE_HEART_HACK Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} HAPPY BIRTHDAY JANNI"
                caption2 =f"{name} **???????????? ???????????????????? ???????? ??????????**"
                caption3 =f" {name} ???????????? ???????? ???????????????? ???? ???????????????????? ????????????????"
                caption4 =f" {name} ???????????????????????????? ???????????????? ???????????? ???????????????????????? ????????????"
                caption5 =f"{name} **???????? ???????? ???? ???????? ???????????????????? ???? ???????????????????? ????????????????**"
                caption6 =f" {name} __???????????????? ???????????????????????????? ???????????????? ???????????? ???????????????????? ????????__ ????"
                caption7 =f"# {name} ???????????????????????????????????????????????? ???????????????????? ???????????????????????????????? ????????????????????????????????????"
                caption8 =f"{name} **???????? ???????????????? ???????????????? ???????? ???????? ???????????????????? ???????????????? ???? ???????????????????? ???? ???????????????????? ???????????? ????????????????????????????????????????????**"
                caption9 =f"{name} ???????????????????? ???????????????????????????????? ???????? ???????????????? ????1000 ???????????????? ??????????????????????"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **???????? ??????????????? ???????????????? ???????? ???????????????? ????????????????????? ?????????????**"
                caption12 =f"**???????? ???????????? ???? ???????? ???????? ???????????? ???????????????????? ???????? ???????????????? ???? ???????????????? ???????????? ????????????????????????**"
                caption13 =f"**???????????????? ???????????????? ???????????????? ???????????????????? ???????? ???????????? ???????? ???????????????? ???????????????? ????**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE B???I???R???T???H???D???A???Y??? P???R??? T???E???R???E??? G???F???/B???F??? K???I??? U???M???A???R??? T???E???K???O??? L???A???G??? J???A???Y?????????????"
                caption16 =f"????????????????"
                caption17 =f"????????????"
                caption18 =f"????????????????"
                caption18 =f"????????????"
                caption20 =f"__A??J??J??J?? P??A??R??T??Y?? H??O??G??I?? N??O??N?? S??T??O??P??????????????????????_"
                caption21 =f"{name} ???????????????? ????????A??M??I?? ????K??O?? B??O??L??U??N??G??A?? ????T??E??L??E?? P??R?? L??A??D??K??I??/L??A??D??K??A?? B??A??J??I?? K??A??R??T??A?? H??????????????????????"
                caption22 =f"????"
                caption23 =f"{name} __???????????????????????? ????????????????????? ???????????????????? ???????????????? ???? ???????????????? ???????????? ????????????????/???????????????????? ????????????__????????"
                caption24 =f"{name} __???????????????????????? ???????????? ???????? ???????????????? ???????? ????????????????????????????????????__"
                caption25 =f"{name} __???????????????? ???????????? ???????? ???????????????????? ????????????????????????????????????????????__"
                caption26 =f"{name} __#????????????????????_????????????????????????????????_????????????????_???????????????????????????????????????????????????????__ ????????"
                caption27 =f"???????????????????????????????????????????????????????????????????????????????????????????"
                caption28 =f"????"
                caption29 =f"__???????????? ???????????????????? {name} ???????? ???? ???????????????? ???????? ???????????????? ???? ????????????????????????__"
                caption30 =f"{name} **???????????? ???????????? ???????????????????????? ???????????? ????????????????/???????????????? ???????????????? ???????????????????? ???????????????? ???????????????? ????????????__ \n\n _ {name} ???????????????? ??????????????????????????????????????????????????????????????????????????__"
                fuk = e.chat_id
                async with e.client.action(bdy, "typing"):
                        await e.client.send_message(bdy, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(bdy, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(bdy, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)

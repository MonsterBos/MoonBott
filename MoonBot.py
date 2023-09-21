# t.me/EmilyOwner
# t.me/destekgroup
# t.me/PlutoKanal 
# Bunuda çalacaklar da neyse sadakamız olsun @EmilyOwner 
from config import api_id, api_hash, session, SUDO_USER
from asyncio import sleep
from pyrogram import Client, enums, idle, filters
from pyrogram.types import Message
import os
import pyrogram
 
from random import choice 


spam_chats = []



# Client 
app = Client(
	"BasicBot",
	api_id=api_id,
	api_hash=api_hash,
	session_string=session
)


# Aktif olmadığını görmek için 
@app.on_message(
    filters.command(["alive"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def yonetıcı(c: Client, message: Message):
    await message.reply_text("**Asistan Aktif!**")

# Yardım Menüsü 
@app.on_message(
    filters.command(["help"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def yonetıcı(c: Client, message: Message):
    await message.reply_text("**Yardım Menüsü!**\n\n!all - Üyeleri tek tek etiketler\n!etag - Üyeleri emoji ile etiketler\n!soru - Üyeleri random soru ile etiketler\n!iptal - Etiketleme işlemini iptal eder\n!katil @username - Asistanı gruba ekler\n!ayril @username - Asistan gruptan ayrılır\n\n**Destek için @destekgroup geliniz!**")



def get_arg(message: Message):
    msg = message.textE
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

# Normal Etiketleme 
@app.on_message(
    filters.command(["all"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.reply_text("**Mesaj mı versen canım!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 1:
            if args:
                txt = f"{usrtxt} {args}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(5)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


# Soru İle Etiketleme
listem = ["Hayatta gerçekleştirmek istediğin bir hayalin var mı?", 
"Kaç tane kız aradaşın oldu ?", 
"Nefret ettiğiniz ancak yine de kullandığın bir uygulama var mı?",
"En tuhaf korkun nedir?",
"Hangi takımı tutuyorsun ?",
"Romayı senmi yaktın?",
"Fiziksel olarak sana en acı veren deneyimin ne oldu?",
"Hangi yılda doğdun?",
"Boyun kaç ?",
"En sevdiğin hobi nedir?",
"Nasılsın ?",
"Gruptaki gizli aşık olduğun kim?",
"Nerelisin?",
"Nbr nasıl gidiyor?",
"Grupta nefret ettiğin kişi kim?",
"Kaç tane sevgilin oldu?",
"Gruptaki partnerin kim?",
"Kendini 3 kelime ile anlatırmısın",
"Selam ne yapıyorsun?",
"En son okuduğun kitabın adı neydi?"
"Grubu yakacakmışsın doğru mu? xd",
"En sevdiğin müzik nedir?",
"Google 'da en son neye baktın?",
"Aşk mı? para mı?",
"En son yaptığın en saçma olay neydi?",
"Keşke şu olsada yesek dediğin şey neydi?",
"Karşı cinste aradığın krater nedir?",
"Karşı cinsin ilk neresine bakıyorsun? xd",
"Grupta sevdiğin 3 kişiyi etiketler misin?",
"Grupta en sevmediğin 3 kişiyi etiketler misin?",
"Grupta işte aradığım eş adayı dediğin kişiyi etiketler misin?",
"Aşkın yaşı yoktur diyorlar doğru mu?",
"Bir adaya düşsen yanına alacağın üç şey ne olurdu?",
"Grupta sevgilin var mı?",
"İnstagram 'a günde kaç story atıyorsun?",
"Hangi şehirde yaşıyorsun",
"Şehrini üç kelime ile anlatır mısın?",
"Memleketini üç kelime ile anlatır mısın?",
"Geçmişe dönüp yaşadığım bir olayı silebilmem mümkün olsaydı hangi olay olurdu?"
]

@app.on_message(
    filters.command(["soru"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def soru(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.reply_text("**Kullanım: !soru .**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 1:
            if args:
                soru = choice(listem)
                txt = f"{usrtxt} __{soru}__"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(10)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

# Emoji İle Etiketleme 

emojiler = "💋 💘 💝 💖 💗 💓 💞 💕 💌 ❣️ 💔 ❤️ 🧡 💛 💚 💙 💜 🖤 💟 💍 💎 💐 💒 🌸 💮 🏵️ 🌹 🥀 🌺 🌻 🌼 🌷 🌱 🌲 🌳 🌴 🌵 🌾 🌿 ☘️ 🍀 🍁 🍂 🍃 🍄 🥭 🍇 🍈 🍉 🍊 🍋 🍌 🍍 🍎 🍏 🍐 🍑 🍒 🥬 🍓 🥝 🍅 🥥 🥑 🍆 🥔 🥕 🌽 🌶️ 🥯 🥒 🥦 🥜 🌰 🍞 🥐 🥖 🥨 🥞 🧀 🍖 🍗 🥩 🥓 🍔 🍟 🍕 🌭 🥪 🌮 🌯 🥙 🥚 🧂 🍳 🥘 🍲 🥣 🥗 🍿 🥫 🍱 🍘 🍙 🍚 🍛 🍜 🥮 🍝 🍠 🍢 🍣 🍤 🍥 🍡 🥟 🥠 🥡 🍦 🍧 🍨 🍩 🍪 🧁 🎂 🍰 🥧 🍫 🍬 🍭 🍮 🍯 🍼 🥛 ☕️ 🍵 🍶 🍾 🍷 🍸 🍹 🍺 🍻 🥂 🥃 🥤 🥢 🍽️ 🍴 🥄 🏺 🙈 🙉 🦝 🐵 🐒 🦍 🐶 🐕 🐩 🐺 🦊 🐱 🐈 🦁 🐯 🐅 🐆 🐴 🐎 🦄 🦓 🦌 🐮 🦙 🐂 🐃 🐄 🐷 🦛 🐖 🐗 🐽 🐏 🐑 🐐 🐪 🐫 🦒 🐘 🦏 🐭 🐁 🐀 🦘 🐹 🦡 🐰 🐇 🐿️ 🦔 🦇 🐻 🐨 🐼 🐾 🦃 🐔 🦢 🐓 🐣 🐤 🦚 🐥 🐦 🦜 🐧 🕊️ 🦅 🦆 🦉 🐸 🐊 🐢 🦎 🐍 🐲 🐉 🦕 🦖 🐳 🐋 🐬 🐟 🐠 🐡 🦈 🐙 🐚 🦀 🦟 🦐 🦑 🦠 🐌 🦋 🐛 🐜 🐝 🐞 🦗 🕷️ 🕸️ 🦂 🦞 👓 🕶️ 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 👙 👚 👛 👜 👝 🛍️ 🎒 👞 👟 👠 👡 👢 👑 👒 🎩 🎓 🧢 ⛑️ 📿 💄 🌂 ☂️ 🎽 🥽 🥼 🥾 🥿 🧺 🚂 🚃 🚄 🚅 🚆 🚇 🚈 🚉 🚊 🚝 🚞 🚋 🚌 🚍 🚎 🚐 🚑 🚒 🚓 🚔 🚕 🚖 🚗 🚘 🚙 🚚 🚛 🚜 🚲 🛴 🛵 🚏 🛣️ 🛤️ ⛵️ 🛶 🚤 🛳️ ⛴️ 🛥️ 🚢 ✈️ 🛩️ 🛫 🛬 🚁 🚟 🚠 🚡 🛰️ 🚀 🛸 🌍 🌎 🌏 🌐 🗺️ 🗾 🏔️ ⛰️ 🗻 🏕️ 🏖️ 🏜️ 🏝️ 🏞️ 🏟️ 🏛️ 🏗️ 🏘️ 🏚️ 🏠 🏡 🏢 🏣 🏤 🏥 🏦 🏨 🏩 🏪 🏫 🏬 🏭 🏯 🏰 🗼 🗽 ⛪️ 🕌 🕍 ⛩️ 🕋 ⛲️ ⛺️ 🏙️ 🎠 🎡 🎢 🎪 ⛳️ 🗿 💦 🌋 🌁 🌃 🌄 🌅 🌆 🌇 🌉 🌌 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌙 🌚 🌛 🌜 🌡️ ☀️ 🌝 🌞 🌟 🌠 ☁️ ⛅️ ⛈️ 🌤️ 🌥️ 🌦️ 🌧️ 🌨️ 🌩️ 🌪️ 🌫️ 🌬️ 🌀 🌈 ☔️ ❄️ ☃️ ⛄️ ☄️ 💧 🌊 🎑 👁️‍🗨️ 💤 💥 💨 💫 💬 🗨️ 🗯️ 💭 🕳️ 🚨 🛑 ⭐️ 🎃 🎄 ✨ 🎈 🎉 🎊 🎋 🎍 🎎 🎏 🎐 🎀 🎁 🃏 🀄️ 🦷 🦴 🛀 👣 💣 🔪 🧱 🛢️ ⛽️ 🛹 🚥 🚦 🚧 🛎️ 🧳 ⛱️ 🔥 🧨 🎗️ 🎟️ 🎫 🧧 🔮 🎲 🎴 🎭 🖼️ 🎨 🎤 🔍 🔎 🕯️ 💡 🔦 🏮 📜 🧮 🔑 🗝️ 🔨 ⛏️ ⚒️ 🛠️ 🗡️ ⚔️ 🔫 🏹 🛡️ 🔧 🔩 ⚙️ 🗜️ ⚖️ ⛓️ ⚗️ 🔬 🔭 📡 💉 💊 🚪 🛏️ 🛋️ 🚽 🚿 🛁 🛒 🚬 ⚰️ ⚱️ 🧰 🧲 🧪 🧴 🧷 🧹 🧻 🧼 🧽 🧯 💠 ♟️ ⌛️ ⏳ ⚡️ 🎆 🎇".split(" ")


@app.on_message(
    filters.command(["etag"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def etag(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.reply_text("**Mesaj mı versen canım!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{random.choice(emojiler)}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(5)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


# Etiketleme İşlemini İptal Eder 
@app.on_message(
    filters.command(["iptal"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def cancel_spam(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.reply_text("**Malmısın cemile etiketleme işlemi yok burda.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply_text("**Tmm durdum.**")

# Gruba Davet İçin 
@app.on_message(
    filters.command(["katil"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`İşleniyor...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**Başarıyla Katılan Sohbet Kimliği** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")

# Gruptan Ayrılması İçin 
@app.on_message(
    filters.command(["ayril"], "!") & (filters.me | filters.user(SUDO_USER))
)
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`İşleniyor...`")
    try:
        await xv.edit_text(f"{client.me.first_name} bu gruptan ayrıldım, hoşçakal!!")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")




# Botu başlatalım :) 
if app:
    app.start()
    app.join_chat("destekgroup")
    app.join_chat("PlutoKanal")
print("Bot Başlatıldı Destek Ve Sorunlar İçin @destekgroup Gelin :)")
idle()

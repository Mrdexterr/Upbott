import re
import time
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.client import Client
from pyrogram.types import InlineKeyboardButton as ikb
from pyrogram.types import InlineKeyboardMarkup as ikm

# text = input('type movie name:- ')
# url = 'https://vegamovies.baby/?s=' + text

bot = Client("66s",
             bot_token="5824866627:AAH1zmWkvNLLz09ydr1WUmMn0oUHz-8q1RM",
             api_id="1712043",
             api_hash="965c994b615e2644670ea106fd31daaf")


async def movievala(url, bot, message, mess):

  #-----------------url 1 ---------------------
  response = requests.get(url)
  html = response.content.decode()
  soup = BeautifulSoup(html, "html.parser")
  link = soup.find_all("div", attrs={"class": "thumb rsz"})
  array = []

  for i in link:
    a = i.find("a")
    array.append(a["href"])
    a1 = a["href"]
    break
  try:
    x = "".join(a1)
    x1 = "https://filmyfly.net/" + x

  except:
    await mess.edit(text='<code>..No Movie Found..</code>')

  #-----------------url 1 end ----------------------
  response1 = requests.get(x1)
  html1 = response1.content.decode()
  soup1 = BeautifulSoup(html1, "html.parser")
  mname = soup1.find("h2", attrs={"class": "header3"})
  moviename = mname.text
  await mess.edit(text='<code>Search Completed</code>')
  #  print (moviename)
  link1 = soup1.find("a",
                     attrs={"href": re.compile("https://link2me.xyz/")})
  y = link1["href"]
  y1 = "".join(y)

  print (y1)

  response3 = requests.get(y1)
  html3 = response3.content.decode()
  soup3 = BeautifulSoup(html3, "html.parser")
  getlink = soup3.find_all("div", attrs={"class": "dlink dl"})
  # h = await bot.send_message(message.chat.id, "" + moviename + "")
  if moviename == None or not moviename:
    await bot.send_message(message.chat.id, "no movie found")
  # else:
  #   print(h)
  global linklist
  linklist = []
  global qualitylist
  qualitylist = []
  global download_btn
  download_btn = []
  for i in getlink:
    a = i.find("a")
    b = i.text
    c = a["href"]
    i.append(c)
    download_btn.append([ ikb(text = b, url = c) ])
    # await bot.send_message(message.chat.id,
    #                        b,
    #                        reply_markup=ikm([[ikb(text="CLICK HERE", url=c)]]))
    qualitylist.append(b)

  await mess.delete()
  await bot.send_message(message.chat.id, '' + moviename + '', reply_markup=ikm(download_btn))
  return linklist, qualitylist


@bot.on_message(filters.command("start"))
def start(bot, message):
  bot.send_message(
    message.chat.id,
    "Welcome to MovieSearcherBot by @iRoleEx \n This bot is totally free to use \n for Query contact @iRoleEx",
  )


@bot.on_message(filters.text & filters.incoming)
async def sm(bot, message):
  mess = await message.reply(text='<code>Searching \nPlease Wait...</code>')
  movie = message.text
  url = "https://filmyfly.net/site-search.html?to-search=" + movie
  # print(url)

  resuult = await movievala(url, bot, message, mess)


bot.run()

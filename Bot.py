from bs4 import BeautifulSoup as bs
import requests
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup  as ikm 
from pyrogram.types import InlineKeyboardButton as ikb 


bot = Client(
    "b1boqt",
    bot_token="5631870454:AAHZ6U_YkOUITaxVuf73UN7COI7H11fINH4",
    api_id=  1712043,
    api_hash="965c994b615e2644670ea106fd31daaf"
)

#movie = input("Enter Movie Name: ")
#url = "https://filmyfly.site/site-search.html?to-search="+movie

async def movies(url,bot, message):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    m1 = soup.find('div', class_="thumb rsz")
    m2 = m1.find('a')['href']
    m3 = "".join(m2)
    m4 = "https://filmyfly.site"+m3
    
    r2 = requests.get(m4)
    soup2 = bs(r2.content, 'html.parser')
    mainname = soup2.find('h2', class_="header3").text
    print(mainname)
    await bot.send_message(message.chat.id, "**Movie Name :- **"+ mainname)
    try:
        m5 = soup2.find('a', attrs={'href' : re.compile("https://linkm")})
        m6 = m5['href']
        r3 = requests.get(m6)
        soup3 = bs(r3.content, 'html.parser')
        m7 = soup3.find_all('div', class_="dlink dl")
        for i in m7:
            m8 = i.find('a')['href']
            m9 = i.find('a').text
            await bot.send_message(message.chat.id, m9, reply_markup=ikm([[ikb(m9, url=m8)]]))
    except:
        m6 = soup2.find('div', class_="dlbtn")
        for i in m6:
            m7 = m6.find_all('a')
            for i in m7:
                mname = i.text
                mlink = i['href']
                await bot.send_message(message.chat.id, mname, reply_markup=ikm([[ikb(mname, url=mlink)]]))
                
            break
        

@bot.on_message(filters.command("start"))
def start(bot, message):
    bot.send_message(message.chat.id,"** Welcome to the MovieSearcher bot **\n **-> Send me the movie name and i will send you the direct download link of the movie 😊** \n Bot made by - @iRoleEx")


@bot.on_message(filters.text & filters.private)
async def movie(bot, message):
    movie = message.text
    url = "https://filmyfly.site/site-search.html?to-search="+movie
    await movies(url,bot,message)
    


bot.run()

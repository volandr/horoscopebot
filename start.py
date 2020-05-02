import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs
import os


headers={'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
base_url = 'https://horoscopes.rambler.ru/'

horoscope=['aries/', 'taurus/', 'gemini/', 'cancer/', 'leo/', 'virgo/', 'libra/',
           'scorpio/', 'sagittarius/', 'capricorn/', 'aquarius/', 'pisces/']
Bot = commands.Bot(command_prefix='!')

def horoscope_parse(base_url, headers):
    session=requests
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('OK')
        soup = bs(request.content, 'html.parser')
        a_name = soup.find('div', attrs={'class': '_1dQ3'}).span.string
        return (a_name)
    else:
            print('Error')

@Bot.event
async def on_ready():
    print("Bot online")



@Bot.command(pass_context=True) #разрешаем передавать агрументы
async def овен(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[0]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def телец(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[1]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def близнецы(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[2]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def рак(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[3]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def лев(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[4]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def дева(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[5]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def весы(ctx): #создаем асинхронную фунцию бота
    urlhoro=base_url+horoscope[6]
    arg = horoscope_parse(urlhoro,headers)
    await ctx.send(arg) #отправляем обратно аргумент

@Bot.command(pass_context=True)
async def скорпион(ctx):  # создаем асинхронную фунцию бота
    urlhoro = base_url + horoscope[7]
    arg = horoscope_parse(urlhoro, headers)
    await ctx.send(arg)  # отправляем обратно аргумент


@Bot.command(pass_context=True)
async def стрелец(ctx):  # создаем асинхронную фунцию бота
    urlhoro = base_url + horoscope[8]
    arg = horoscope_parse(urlhoro, headers)
    await ctx.send(arg)  # отправляем обратно аргумент


@Bot.command(pass_context=True)
async def козерог(ctx):  # создаем асинхронную фунцию бота
    urlhoro = base_url + horoscope[9]
    arg = horoscope_parse(urlhoro, headers)
    await ctx.send(arg)  # отправляем обратно аргумент


@Bot.command(pass_context=True)
async def водолей(ctx):  # создаем асинхронную фунцию бота
    urlhoro = base_url + horoscope[10]
    arg = horoscope_parse(urlhoro, headers)
    await ctx.send(arg)  # отправляем обратно аргумент


@Bot.command(pass_context=True)
async def рыбы(ctx):  # создаем асинхронную фунцию бота
    urlhoro = base_url + horoscope[11]
    arg = horoscope_parse(urlhoro, headers)
    await ctx.send(arg)  # отправляем обратно аргумент

token = os.environ.get('BOT_TOKEN2')
Bot.run(str(token))

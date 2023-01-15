import discord
import random
import string
import asyncio
import datetime
import requests
import time
import os
import json
import pyfiglet
from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")
        
def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()


chat_list = ['i am atomic','hello siir','hello', 'gm','lfg','good morning','lets go','gogogo','where are u from?','good project','want to play with me?','nice','night all','nice to meet you','we can do it','are you watch anime?','i like you all']

os.system('cls')
result = pyfiglet.figlet_format("""Discord Auto Random Chat""", font = "graceful"  )
print (colored(result, 'blue'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now()
print (colored('''Created by: MITYO''', 'cyan', attrs=['bold'])) 
print (colored('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••', 'green', attrs=['bold']))
print (colored(f"Ξ Follow myGithub : https://github.com/mityoe860 \nΞ START           : {x} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• \n', 'green', attrs=['bold']))
print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
while True:
        try:
            setdelay = int(input("Please input delay time chat in seconds = "))
            break
        except:
            print("ONLY USE NUMBER!")
print (colored('\nWrite on discord chat: \n!ikuzo <number of messages>', 'cyan', attrs=['bold']))



@client.command()
async def ikuzo(ctx,amount: int):
    await ctx.message.delete()
    msgsend = amount
    sec = setdelay * msgsend
    convert = str(datetime.timedelta(seconds = sec))
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}messages\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{convert}\n")
    while msgsend > 0:
        try:    
            msgsend -= 1  
            output = random.choice(chat_list)
            await ctx.send(output)  
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Message success sent = {Fore.WHITE}#{msgsend + 1} {output}{Fore.LIGHTBLACK_EX} | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}")                 
        except:
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot send message {Fore.WHITE}#{msgsend + 1}")
            pass
        await asyncio.sleep(1)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == client.user):
            try:
                await message.delete()
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Success delete message = {Fore.WHITE}#{msgsend + 1} {output}")
            except:
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot delete message {Fore.WHITE}#{msgsend + 1} {output}")
                pass
        if msgsend == 0:
            print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All messages was sent")
        await asyncio.sleep(setdelay)
    
    return


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)


Init()

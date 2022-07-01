

import discord
import random

TOKEN = "ENTER TOKEN HERE"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'test_channel':
        if user_message.lower() == 'heyyo':
            await message.channel.send(f'Heyyo {username}!')
            return
        elif user_message.lower() == 'cya':
            await message.channel.send(f'cya later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'Here is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!coinflip':
            flipNum = random.randrange(2)
            coin_side = ''
            if flipNum == 0:
                coin_side = 'Heads'
            elif flipNum == 1:
                coin_side = 'Tails'
            response = f'The coin was flipped and is {coin_side}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!other':
        await message.channel.send('This message can be sent to all \"other\" channels')
        return




client.run(TOKEN)

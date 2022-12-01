Creating Discord bot
====================

.. py:currentmodule:: corkus


Corkus.py was made with asynchronous applications in mind. Perfect examples of these are 
Discord Bots made with `Discord.py <https://discordpy.readthedocs.io/en/stable/index.html>`_. This
guide gives an example how to use Corkus.py with Discord.py and similar libraries.

Let's start from a modified example from `Discord.py Quickstart <https://discordpy.readthedocs.io/en/stable/quickstart.html>`_.
We' have wrapped whole application intro ``DiscordBot`` class. That will simplify our life down the line.

.. code-block:: python

    import discord

    class DiscordBot(discord.Client):
        def __init__(self):
            intents = discord.Intents.default()
            intents.message_content = True
            super().__init__(intents=intents)

        async def on_ready(self):
            print(f'We have logged in as {client.user}')

        async def on_message(self, message):
            if message.author == client.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

    client = DiscordBot()
    client.run('your token here')

Now you need to add Corkus constructor and :py:func:`Corkus.start() <Corkus.start>` function. This is required to
make any requests using Corkus.

.. code-block:: python
    :emphasize-lines: 2,9,11,12

    import discord
    from corkus import Corkus

    class DiscordBot(discord.Client):
        def __init__(self):
            intents = discord.Intents.default()
            intents.message_content = True
            super().__init__(intents=intents)
            self.corkus = Corkus()

        async def setup_hook(self):
           await self.corkus.start()

        async def on_ready(self):
            print(f'We have logged in as {client.user}')

        async def on_message(self, message):
            if message.author == client.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')

        client = DiscordBot()
        client.run('your token here')

This code uses `setup_hook <https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.setup_hook>`_ for
client initialization. Discord.py waits for this function before login to gateway. This way you can start using corkus
even inside ``on_ready`` function. Now, let's add an command to display Wynncraft players count.

.. code-block:: python
    :emphasize-lines: 21,22,23

    import discord
    from corkus import Corkus

    class DiscordBot(discord.Client):
        def __init__(self):
            intents = discord.Intents.default()
            intents.message_content = True
            super().__init__(intents=intents)
            self.corkus = Corkus()

        async def setup_hook(self):
           await self.corkus.start()

        async def on_ready(self):
            print(f'We have logged in as {client.user}')

        async def on_message(self, message):
            if message.author == client.user:
                return

            if message.content.startswith('$online'):
                player_sum = await self.corkus.network.players_sum()
                await message.channel.send(f'There are currently **{player_sum}** players online!')

        client = DiscordBot()
        client.run('your token here')

Congratulations! You can now use ``$online`` command to display sum of online players!
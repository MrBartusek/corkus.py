import asyncio
from corkus import Corkus

async def main():
    async with Corkus() as corkus:
        user = await corkus.player.get('MrBartusekXD')
        print(user.classes)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
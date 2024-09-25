import asyncio

from sqlalchemy import select

from db_api_async.models import Base, Wallet
from db_api_async.db_api import Session, async_engine


async def main():
    # Создание контекста соединения
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        async with Session() as session:
            # получили нужные нам объекты и достали только первый из них
            stmp = select(Wallet).where(Wallet.address == '3333333')
            wallet = (await session.scalars(stmp)).first()
            print('address:', wallet.address)
            # удаляем этот объект
            await session.delete(wallet)


if __name__ == '__main__':
    asyncio.run(main())

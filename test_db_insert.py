import asyncio
from datetime import datetime

from db_api_async.models import Base, Wallet
from db_api_async.db_api import Session, async_engine


async def main():
    # Создание контекста соединения
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        # Создание объекта класса Wallet
        wallet = Wallet(
            name="account1",
            private_key='0x8732y87g23b223y322dsfs',
            address='11111',
            withdraw_address = '1111122222',
            next_action_time=datetime.now(),
            number_of_swaps=5,
            number_of_nft_mints=1,
            number_of_lending=4,
            number_of_liquidity_stake=2,
        )

        async with Session() as session:
        #     # возвращает список объектов, которые уйдут в БД при коммите
        #     print('session.new:', session.new)
        #
        #     # добавление объекта в сессию
            session.add(wallet)
        #     print('session.new:', session.new)

        async with Session() as session:
            # добавление сразу нескольких объектов (списком)
            wallet_2 = Wallet(
                name="account2",
                private_key='0x8732y87g23b23y2222222',
                address='2222222',
                withdraw_address='22222111111',
                next_action_time=datetime.now(),
                number_of_swaps=1,
                number_of_nft_mints=2,
                number_of_lending=3,
                number_of_liquidity_stake=4,
            )
            wallet_3 = Wallet(
                name="account3",
                private_key='0x8732y87g23b23y3333333',
                address='3333333',
                withdraw_address='333333555555',
                next_action_time=datetime.now(),
                number_of_swaps=6,
                number_of_nft_mints=7,
                number_of_lending=8,
                number_of_liquidity_stake=9,
            )
            session.add_all([wallet_2, wallet_3])


if __name__ == '__main__':
    asyncio.run(main())

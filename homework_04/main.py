"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models import (
    async_engine,
    Session,
    Base,
    Post,
    User
)
from jsonplaceholder_requests import (
    fetch_users,
    fetch_posts
)


async def create_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_users_into_db(session: AsyncSession, user_list: List[dict]) -> None:
    user_entries = []
    for user in user_list:
        entry = User(name=user["name"],
                     username=user["username"],
                     email=user["email"])
        user_entries.append(entry)
        session.add_all(user_entries)
        await session.commit()


async def insert_posts_into_db(session: AsyncSession, post_list: List[dict]) -> None:
    post_entries = []
    for post in post_list:
        entry = Post(user_id=post["userId"],
                     title=post["title"],
                     body=post["body"])
        post_entries.append(entry)
        session.add_all(post_entries)
        await session.commit()


async def async_main():
    await create_tables()
    users, posts = await asyncio.gather(fetch_users(), fetch_posts())
    async with Session() as session:
        await insert_users_into_db(session, users)
        await insert_posts_into_db(session, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
from typing import List

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> List[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users() -> List[dict]:
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts() -> List[dict]:
    return await fetch_json(POSTS_DATA_URL)

""" 
Requests lib example 
"""
import asyncio
import aiohttp
import requests
import json
import time
from pathlib import Path

def get_response(url):
    """_summary_

    Args:
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    response = requests.get(url)
    return response
def write_json(file_name, content):
    """_summary_

    Args:
        file_name (_type_): _description_
        content (_type_): _description_
    """
    with open(file_name, mode="w") as file:
        json.dump(content, file)
async def async_fetch(session, url):
    """_summary_

    Args:
        session (_type_): _description_
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    async with session.get(url) as response:
        return await response.json()
async def async_fetch_url(url):
    """_summary_

    Args:
        url (_type_): _description_

    Returns:
        _type_: _description_
    """
    async with aiohttp.ClientSession() as session:
        data = await async_fetch(session, url)
        return data
def main():
    """_summary_
    """
    url = "https://dummyjson.com/products/1"
    images_dir = Path(__file__).parent / "tasks"
    if not Path.exists(images_dir): 
        Path.mkdir(images_dir) 
    file_name_requests = images_dir / "requests_json.json" 
    file_name_aiohttp = images_dir / "aiohttp_json.json"
    start_time = time.time()
    response = get_response(url).json() 
    print(f"Requests time: {time.time() - start_time}") 
    write_json(file_name_requests, response)
    start_time = time.time()
    response = asyncio.run(async_fetch_url(url))
    print(f"Aiohttp time: {time.time() - start_time}")
    write_json(file_name_aiohttp, response)

if __name__ == "__main__": 
    main()
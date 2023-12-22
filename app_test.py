import pytest
from app import get_json
import asyncio
import allure

@allure.feature('API Tests')
@allure.title('Test get_json with valid URL')
@pytest.mark.asyncio
async def test_get_json_valid_url():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    data = await get_json(url)
    assert 'userId' in data
    assert 'title' in data
    assert 'body' in data

@allure.feature('API Tests')
@allure.title('Test get_json with invalid URL')
@pytest.mark.asyncio
async def test_get_json_invalid_url():
    url = 'https://jsonplaceholder.typicode.com/invalid_endpoint'
    with pytest.raises(aiohttp.ClientResponseError):
        await get_json(url)
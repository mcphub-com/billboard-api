import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/LDVIN/api/billboard-api'

mcp = FastMCP('billboard-api')

@mcp.tool()
def billboard_hot100(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                     range: Annotated[str, Field(description='max range(1-100)')]) -> dict: 
    '''Provide the Billboard Hot 100 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/hot-100'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard_artist100(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                        range: Annotated[str, Field(description='max range(1-100)')]) -> dict: 
    '''Provide the Billboard Artist 100 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/artist-100'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard200(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='max range(1-200)')]) -> dict: 
    '''Provide the Billboard 200 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/billboard-200'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard_global200(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                        range: Annotated[str, Field(description='max range(1-200)')]) -> dict: 
    '''Provide the Billboard Global 200 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/billboard-global-200'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard_global_excl_us(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                             range: Annotated[str, Field(description='max range(1-200)')]) -> dict: 
    '''Provide the Billboard Global Excl. US chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/billboard-global-excl-us'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard_usafrobeats_songs(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                                range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Billboard U.S. Afrobeats Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/billboard-us-afrobeats-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def catalog_albums(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                   range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Catalog Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/catalog-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def independent_albums(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                       range: Annotated[str, Field(description='max range(1-25)')]) -> dict: 
    '''Provide the Independent Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/independent-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tik_tok_billboard_top50(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                            range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the TikTok Billboard Top 50 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/tiktok-billboard-top-50'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def streaming_songs(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Streaming Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/streaming-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def radio_songs(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Radio Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/radio-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def digital_song_sales(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                       range: Annotated[str, Field(description='max range(1-25)')]) -> dict: 
    '''Provide the Digital Song Sales chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/digital-song-sales'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_album_sales(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Top Album Sales chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/top-album-sales'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_streaming_albums(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                         range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Top Streaming Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/top-streaming-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_current_album_sales(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                            range: Annotated[str, Field(description='max range(1-50)')]) -> dict: 
    '''Provide the Top Current Album Sales chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/top-current-album-sales'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard_japan_hot100(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                           range: Annotated[str, Field(description='max range(1-100)')]) -> dict: 
    '''Provide the Billboard Japan Hot 100 chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/billboard-japan-hot-100'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot_trending_songs_powered_by_twitter(date: Annotated[Union[str, datetime], Field(description='format(YYYY-MM-DD)')],
                                          range: Annotated[str, Field(description='max range(1-20)')]) -> dict: 
    '''Provide the Hot Trending Songs Powered By Twitter chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/hot-trending-songs-powered-by-twitter'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot100_songs(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Hot 100 Songs chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/hot-100-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_artists(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top Artists chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard200_albums(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Billboard 200 Albums chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-billboard-200-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_artists_duo_group(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top Artists - Duo/Group chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-artists-duo-group'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_artists_male(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top Artists - Male chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-artists-male'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_artists_female(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top Artists - Female chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-artists-female'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_new_artists(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top New Artists chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/top-new-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_labels(year: Annotated[Union[str, None], Field(description='date format(YYYY)')] = None) -> dict: 
    '''Provide the YEAR-END Top Labels chart information If `year` is not supplied, will default to last year.'''
    url = 'https://billboard-api2.p.rapidapi.com/year-end-chart/labels'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'year': year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def artists() -> dict: 
    '''Provide the Greatest of All Time Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot100_artists() -> dict: 
    '''Provide the Greatest of All Time Hot 100 Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-hot-100-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard200_artists() -> dict: 
    '''Provide the Greatest of All Time Billboard 200 Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-billboard-200-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot100_songs_by_women() -> dict: 
    '''Provide the Greatest of All Time Hot 100 Songs by Women chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-hot-100-songs-by-women'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot100_women_artists() -> dict: 
    '''Provide the Greatest of All Time Hot 100 Women Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-hot-100-women-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def billboard200_albums_by_women() -> dict: 
    '''Provide the Greatest of All Time Billboard 200 Albums by Women chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-billboard-200-albums-by-women'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def songs_of_the80s() -> dict: 
    '''Provide the Greatest of All Time Songs of the '80s chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-billboards-top-songs-80s'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def songs_of_the90s() -> dict: 
    '''Provide the Greatest of All Time Songs of the '90s chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-billboards-top-songs-90s'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def songs_of_the_summer() -> dict: 
    '''Provide the Greatest of All Time Songs of the Summer chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-songs-of-the-summer'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def holiday100_songs() -> dict: 
    '''Provide the Greatest of All Time Holiday 100 Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-holiday-100-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_holiday_albums() -> dict: 
    '''Provide the Greatest of All Time Top Holiday Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-top-holiday-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pop_songs() -> dict: 
    '''Provide the Greatest of All Time Pop Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-pop-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pop_songs_artists() -> dict: 
    '''Provide the Greatest of All Time Pop Songs Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-pop-songs-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def adult_pop_songs() -> dict: 
    '''Provide the Greatest of All Time Adult Pop Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-adult-pop-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def adult_pop_songs_artists() -> dict: 
    '''Provide the Greatest of All Time Adult Pop Songs Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-adult-pop-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot_country_songs() -> dict: 
    '''Provide the Greatest of All Time Hot Country Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-country-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_country_albums() -> dict: 
    '''Provide the Greatest of All Time Top Country Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-country-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_country_artists() -> dict: 
    '''Provide the Greatest of All Time Top Country Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-country-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def latin_artists() -> dict: 
    '''Provide the Greatest of All Time Latin Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-latin-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot_latin_songs() -> dict: 
    '''Provide the Greatest of All Time Hot Latin Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-hot-latin-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot_latin_songs_artists() -> dict: 
    '''Provide the Greatest of All Time Hot Latin Songs Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-hot-latin-songs-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_dance_club_artists() -> dict: 
    '''Provide the Greatest of All Time Top Dance Club Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-top-dance-club-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hot_rb_hip_hop_songs() -> dict: 
    '''Provide the Greatest of All Time Hot R&B/Hip-Hop Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-r-b-hip-hop-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_rb_hip_hop_albums() -> dict: 
    '''Provide the Greatest of All Time Top R&B/Hip-Hop Albums chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-r-b-hip-hop-albums'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_rb_hip_hop_artists() -> dict: 
    '''Provide the Greatest of All Time Top R&B/Hip-Hop Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-r-b-hip-hop-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def alternative_songs() -> dict: 
    '''Provide the Greatest of All Time Alternative Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-alternative-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def alternative_artists() -> dict: 
    '''Provide the Greatest of All Time Alternative Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-alternative-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def adult_alternative_songs() -> dict: 
    '''Provide the Greatest of All Time Adult Alternative Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-adult-alternative-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def adult_alternative_artists() -> dict: 
    '''Provide the Greatest of All Time Adult Alternative Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-adult-alternative-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def mainstream_rock_songs() -> dict: 
    '''Provide the Greatest of All Time Mainstream Rock Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-mainstream-rock-songs'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def mainstream_rock_artists() -> dict: 
    '''Provide the Greatest of All Time Mainstream Rock Artists chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/goat-chart/greatest-of-all-time-mainstream-rock-artists'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def australia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Australia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/australia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def austria_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Austria Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/austria'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def belgium_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Belgium Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/belgium'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bolivia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Bolivia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/bolivia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def brazil_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Brazil Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/brazil'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def chile_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Chile Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/chile'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def colombia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                   range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Colombia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/colombia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def croatia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Croatia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/croatia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def czech_republic_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                         range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Czech Republic Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/czech-republic'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def denmark_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Denmark Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/denmark'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ecuador_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Ecuador Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/ecuador'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def finland_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Finland Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/finland'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def france_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the France Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/france'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def germany_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Germany Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/germany'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def greece_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Greece Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/greece'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hong_kong_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Hong Kong Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/hong-kong'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hungary_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Hungary Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/hungary'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def iceland_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Iceland Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/iceland'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def india_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the India Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/india'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def indonesia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Indonesia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/indonesia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ireland_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Ireland Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/ireland'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def luxembourg_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                     range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Luxembourg Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/luxembourg'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def malaysia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                   range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Malaysia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/malaysia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def mexico_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Mexico Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/mexico'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def netherlands_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                      range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Netherlands Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/netherlands'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def new_zealand_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                      range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the New Zealand Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/new-zealand'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def norway_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Norway Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/norway'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def peru_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
               range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Peru Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/peru'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def philippines_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                      range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Philippines Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/philippines'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def poland_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Poland Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/poland'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def portugal_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                   range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Portugal Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/portugal'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def romania_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                  range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Romania Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/romania'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def singapore_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                    range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Singapore Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/singapore'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def slovakia_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                   range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Slovakia Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/slovakia'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def south_africa_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                       range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the South Africa Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/south-africa'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def south_korea_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                      range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the South Korea Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/south-korea'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def spain_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Spain Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/spain'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sweden_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Sweden Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/sweden'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def switzerland_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                      range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Switzerland Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/switzerland'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def taiwan_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Taiwan Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/taiwan'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def turkey_songs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
                 range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the Turkey Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/turkey'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def uksongs(date: Annotated[Union[str, datetime], Field(description='date format(YYYY-MM-DD)')],
            range: Annotated[str, Field(description='')]) -> dict: 
    '''Provide the U.K. Songs chart information'''
    url = 'https://billboard-api2.p.rapidapi.com/country-songs-chart/u-k'
    headers = {'x-rapidapi-host': 'billboard-api2.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'range': range,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")

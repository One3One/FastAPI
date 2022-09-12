from fastapi import FastAPI
from scrapper import Scraper

app = FastAPI()
quotes = Scraper()


@app.get("/{cat}")
async def read_item(cat):
        return quotes.scrapedata(cat)
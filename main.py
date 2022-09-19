from fastapi import FastAPI
import uvicorn
from schemas import NumberRequest
import functions

app = FastAPI()


@app.get("/")
async def about():
    return {"API_name": "API_proxy_NumberToWords"}


@app.get("/about")
async def about():
    return "API_proxy_NumberToWords acts as intermediary between a consumer and Number Conversion Service. " \
           "Returns the word corresponding to the positive number passed as parameter. Limited to quadrillions. " \
           "See Github repo for more detailed information."


@app.post("/number_to_words")
async def number_to_words(data: NumberRequest):
    message = functions.create_number_to_words_soap_message(data.ubiNum)
    response = functions.send_soap_request(message, functions.number_to_words_parser)
    return {"number_in_words": response}


# Запуск API
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)

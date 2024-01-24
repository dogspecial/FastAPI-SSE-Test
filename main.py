from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
import uvicorn
import asyncio
import json

app = FastAPI()


@app.get("/")
def root():
    return {
        "Hello World!"
    }


@app.get("/st")
def streaming():
    # StreamingResponse(streaming_test())
    return StreamingResponse(streaming_test(),media_type="application/x-ndjson")


async def streaming_test():
    for i in range(10):
        yield json.dumps({"event_id": i, "data": f"{i + 1} chunk of data", "is_final_event": i == 9}) + "\n"
        await asyncio.sleep(1)


async def current_datetime_streamer():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M%S").encode('utf-8')
        yield f"data: {current_time}\n\n"
        time.sleep(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8081, workers=1, reload=True)

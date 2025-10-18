from fastapi import FastAPI
import requests
from datetime import datetime, timezone

app = FastAPI(
    title="Ndu's stage 0 api"
)

@app.get('/')
async def index():
    return "welcome, to stage 0's api"

@app.get('/me')
async def me_endpoint():
    time = datetime.now(timezone.utc).isoformat()
    time = time.replace("+00:00", 'Z')
    response = {
        'status': 'success',
        'user': {
            'email': 'davidnduonofit47@gmail.com',
            'name': 'nduonofit davidfortune',
            'stack': 'python/fastapi'
        },
        'timestamp': time,
    }
    cat_api_response = requests.get('https://catfact.ninja/fact').json()
    response['fact'] = cat_api_response['fact']
    return response
    

    
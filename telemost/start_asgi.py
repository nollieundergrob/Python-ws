import uvicorn
from telemost.asgi import application

if __name__ == '__main__':
    uvicorn.run("telemost.asgi:application", host="10.11.228.96", port=5000, workers=3, reload=True)
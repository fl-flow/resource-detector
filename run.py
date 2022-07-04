import uvicorn


def run():
    uvicorn.run('src.main:app', host='0.0.0.0', port=8000, workers=1)


if __name__ == '__main__':
    run()

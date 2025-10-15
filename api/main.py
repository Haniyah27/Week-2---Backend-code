from fastapi import fastapi

app = FastAPI(
    title="FastAPI Example"
    description="This is an example of using FastAPI"
)

@app.get('/')
def default_route():
    """
    This is the default endpoint for this for backend
    """
return { "You have reached the default route. Back-end server is listening..."}
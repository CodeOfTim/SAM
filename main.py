from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI(title="Simple FastAPI App")

# Define a root route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define a parameterized route
@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}

# Run the app (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

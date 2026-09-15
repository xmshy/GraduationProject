from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Smart Gate is Online", "status": "Secure"}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    print(f"Request intercepted: {path} from {request.client.host}")
    return {
        "intercepted_path": path, 
        "method": request.method,
        "action": "Analyzing by Smart Gate AI..."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


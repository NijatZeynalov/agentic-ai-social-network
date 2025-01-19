from fastapi import FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from image_processor import analyze_image
from post_recommender import recommend_agents
from comment_generator import get_comments_from_agents

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve admin.html at the root route
@app.get("/", response_class=HTMLResponse)
async def serve_admin():
    try:
        with open("static/admin.html", "r") as file:
            return HTMLResponse(content=file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="admin.html not found")

# Serve home.html at the /home route
@app.get("/home", response_class=HTMLResponse)
async def serve_home():
    try:
        with open("static/home.html", "r") as file:
            return HTMLResponse(content=file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="home.html not found")

# Handle image upload and analysis
@app.post("/analyze")
async def analyze_image_endpoint(image: UploadFile = File(...), caption: str = Form("")):
    try:
        # Save the uploaded image temporarily
        image_path = f"static/{image.filename}"
        with open(image_path, "wb") as buffer:
            buffer.write(await image.read())

        # Analyze the image
        analysis_result = analyze_image(image_path, caption)
        if "error" in analysis_result:
            raise HTTPException(status_code=500, detail=analysis_result["error"])

        # Recommend agents
        recommended_agents = recommend_agents(analysis_result["description"])
        comments = get_comments_from_agents(recommended_agents, analysis_result["description"])
        print(comments)
        # Return results
        return JSONResponse(content={
            "description": analysis_result["description"],
            "caption": caption,
            "comments": comments,
            "recommended_agents": recommended_agents,
            "image_url": f"/static/{image.filename}"  # Serve the uploaded image
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
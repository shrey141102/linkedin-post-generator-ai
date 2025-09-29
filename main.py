from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv
from agents.news_agent import NewsAgent

load_dotenv()

app = FastAPI(
    title="Demanual AI - LinkedIn Post Generator",
    description="AI-powered API service that generates LinkedIn posts from recent news using Google Gemini API + LangChain",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PostRequest(BaseModel):
    topic: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "Artificial Intelligence"
            }
        }

class PostResponse(BaseModel):
    topic: str
    news_sources: List[str]
    linkedin_post: str
    image_suggestion: Optional[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "Artificial Intelligence",
                "news_sources": [
                    "https://example.com/ai-news-1",
                    "https://example.com/ai-news-2",
                    "https://example.com/ai-news-3"
                ],
                "linkedin_post": "🚀 AI is transforming industries at an unprecedented pace!\n\nRecent developments in artificial intelligence show that companies are increasingly adopting AI solutions to streamline operations and enhance customer experiences. From healthcare diagnostics to financial services, the impact is undeniable.\n\nKey insights from this week:\n✅ 70% of enterprises are planning AI integration by 2025\n✅ New breakthrough in natural language processing\n✅ Ethical AI frameworks gaining industry adoption\n\nThe future of work is evolving rapidly, and staying informed about these trends is crucial for professionals across all sectors.\n\nWhat's your experience with AI in your industry? How do you see it shaping the future of your work?\n\n#ArtificialIntelligence #AI #Innovation #FutureOfWork #Technology #DigitalTransformation",
                "image_suggestion": "Professional infographic about Artificial Intelligence trends"
            }
        }

def get_news_agent():
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise HTTPException(
            status_code=500,
            detail="Google API key not configured. Please set GOOGLE_API_KEY environment variable."
        )
    return NewsAgent(google_api_key)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Demanual AI LinkedIn Post Generator API",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "LinkedIn Post Generator API"}

@app.post("/generate-post", response_model=PostResponse)
async def generate_post(
    request: PostRequest,
    agent: NewsAgent = Depends(get_news_agent)
):
    """
    Generate a LinkedIn-style post based on recent news about the given topic.
    
    - **topic**: The topic to search for recent news and generate a LinkedIn post about
    
    Returns a structured response with:
    - The original topic
    - Sources of news articles found
    - Generated LinkedIn post content
    - Optional image suggestion
    """
    try:
        if not request.topic.strip():
            raise HTTPException(
                status_code=400,
                detail="Topic cannot be empty"
            )
        
        result = agent.generate_linkedin_post(request.topic.strip())
        
        if "Error generating post" in result.get("linkedin_post", ""):
            raise HTTPException(
                status_code=500,
                detail="Failed to generate LinkedIn post. Please try again."
            )
        
        return PostResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
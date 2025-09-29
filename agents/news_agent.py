import os
from typing import List, Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from duckduckgo_search import DDGS
import re


class NewsAgent:
    def __init__(self, google_api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=google_api_key,
            temperature=0.7
        )
        self.search_tool = DuckDuckGoSearchRun()
        
    def generate_linkedin_post(self, topic: str) -> Dict[str, Any]:
        try:
            # Search for recent news
            search_query = f"latest news {topic} recent developments 2024"
            search_results = self.search_tool.run(search_query)
            
            # Extract URLs from search results
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', search_results)
            news_sources = urls[:3] if urls else []
            
            # Create LinkedIn post using direct LLM call
            linkedin_prompt = f"""
            Based on this recent news about {topic}:
            
            {search_results[:2000]}  # Limit text length
            
            Create a professional LinkedIn post that:
            1. Starts with a compelling hook (emoji optional)
            2. Summarizes the key developments in 2-3 sentences
            3. Provides professional insights or implications
            4. Ends with a question to encourage engagement
            5. Uses 3-5 relevant hashtags
            6. Maintains a professional yet engaging tone
            7. Is between 150-250 words
            
            Make it sound natural and avoid overly promotional language.
            Format it properly for LinkedIn with line breaks.
            """
            
            response = self.llm.invoke(linkedin_prompt)
            linkedin_post = response.content if hasattr(response, 'content') else str(response)
            
            # Optional: Suggest an image
            image_suggestion = f"Professional infographic about {topic} trends" if topic else None
            
            return {
                "topic": topic,
                "news_sources": news_sources,
                "linkedin_post": linkedin_post,
                "image_suggestion": image_suggestion
            }
            
        except Exception as e:
            # Fallback response if there's an error
            fallback_post = f"""🚀 Exploring the latest in {topic}!

The field of {topic} continues to evolve rapidly, bringing new opportunities and challenges for professionals across industries. 

Key trends to watch:
✅ Increased adoption and integration
✅ Focus on practical applications  
✅ Growing emphasis on ethical considerations

As we navigate these developments, staying informed and adaptable remains crucial for career growth and industry success.

What's your experience with {topic}? How do you see it impacting your field?

#{topic.replace(' ', '')} #Innovation #Technology #FutureOfWork #ProfessionalDevelopment"""

            return {
                "topic": topic,
                "news_sources": [],
                "linkedin_post": fallback_post,
                "image_suggestion": f"Professional infographic about {topic} trends"
            }
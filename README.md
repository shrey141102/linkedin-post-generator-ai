# Demanual AI - LinkedIn Post Generator 🚀

An AI-powered API service that uses Google Gemini API + LangChain to fetch recent news on a given topic and generate professional LinkedIn-style posts.

## 🌟 Features

- **AI-Powered Content Generation**: Uses Google Gemini Pro model for intelligent content creation
- **Real-time News Search**: Fetches latest news using DuckDuckGo search integration
- **Professional LinkedIn Posts**: Generates engaging, professional posts with proper formatting
- **RESTful API**: FastAPI-based service with automatic Swagger documentation
- **Cloud Ready**: Configured for Vercel deployment
- **Error Handling**: Comprehensive error handling and validation

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI/ML**: Google Gemini API, LangChain
- **Web Search**: DuckDuckGo Search
- **Deployment**: Vercel
- **Documentation**: Automatic Swagger/OpenAPI docs

## 📋 Requirements

- Python 3.8+
- Google Gemini API key (free account available)
- Internet connection for news search

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd demanualai
```

### 2. Set up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` and add your Google API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 5. Get Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

### 6. Run the Application

```bash
# Development server
uvicorn main:app --reload

# Or using Python
python main.py
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

### Interactive Docs
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints

#### `POST /generate-post`

Generate a LinkedIn-style post based on recent news about a given topic.

**Request Body:**
```json
{
  "topic": "Artificial Intelligence"
}
```

**Response:**
```json
{
  "topic": "Artificial Intelligence",
  "news_sources": [
    "https://example.com/ai-news-1",
    "https://example.com/ai-news-2",
    "https://example.com/ai-news-3"
  ],
  "linkedin_post": "🚀 AI is transforming industries at an unprecedented pace!\\n\\nRecent developments in artificial intelligence show that companies are increasingly adopting AI solutions to streamline operations and enhance customer experiences...",
  "image_suggestion": "Professional infographic about Artificial Intelligence trends"
}
```

#### `GET /health`

Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "LinkedIn Post Generator API"
}
```

## 🧪 Testing

### Manual Testing

1. Start the server: `uvicorn main:app --reload`
2. Open `http://localhost:8000/docs`
3. Try the `/generate-post` endpoint with a sample topic

### cURL Example

```bash
curl -X POST "http://localhost:8000/generate-post" \\
     -H "Content-Type: application/json" \\
     -d '{"topic": "Machine Learning"}'
```

### Python Example

```python
import requests

response = requests.post(
    "http://localhost:8000/generate-post",
    json={"topic": "Blockchain Technology"}
)

print(response.json())
```

## 🌐 Deployment

### Vercel Deployment

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy:
   ```bash
   vercel --prod
   ```

4. Set environment variables in Vercel dashboard:
   - `GOOGLE_API_KEY`: Your Google Gemini API key

### Environment Variables

Set the following environment variable in your deployment platform:

- `GOOGLE_API_KEY`: Your Google Gemini API key

## 📁 Project Structure

```
demanualai/
├── agents/
│   ├── __init__.py
│   └── news_agent.py          # LangChain agent for news and post generation
├── api/
│   └── index.py               # Vercel entry point
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── vercel.json               # Vercel configuration
├── .env.example              # Environment template
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes | - |

### FastAPI Settings

- **Host**: `0.0.0.0`
- **Port**: `8000`
- **CORS**: Enabled for all origins (configure for production)

## 🤝 How It Works

1. **Input**: User provides a topic via API
2. **News Search**: Agent searches for recent news using DuckDuckGo
3. **Content Analysis**: LangChain processes the news content
4. **Post Generation**: Gemini AI creates a professional LinkedIn post
5. **Response**: Returns formatted post with source links

## 🔍 Example Output

**Input Topic**: "Artificial Intelligence"

**Generated LinkedIn Post**:
```
🚀 AI is transforming industries at an unprecedented pace!

Recent developments in artificial intelligence show that companies are increasingly adopting AI solutions to streamline operations and enhance customer experiences. From healthcare diagnostics to financial services, the impact is undeniable.

Key insights from this week:
✅ 70% of enterprises are planning AI integration by 2025
✅ New breakthrough in natural language processing  
✅ Ethical AI frameworks gaining industry adoption

The future of work is evolving rapidly, and staying informed about these trends is crucial for professionals across all sectors.

What's your experience with AI in your industry? How do you see it shaping the future of your work?

#ArtificialIntelligence #AI #Innovation #FutureOfWork #Technology #DigitalTransformation
```

## 🚨 Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid or empty topic
- **500 Internal Server Error**: API key issues, service failures
- **Rate Limiting**: Handled by Google Gemini API

## 💡 Future Improvements

If scaling this to production, consider:

### Database & Architecture
- **Database**: PostgreSQL for storing generated posts, user analytics
- **Caching**: Redis for caching news results and generated content
- **Queue System**: Celery with Redis for async post generation
- **Microservices**: Separate services for news fetching, AI generation, and API

### Enhanced Features
- **User Management**: JWT authentication, user profiles
- **Post Templates**: Multiple LinkedIn post styles
- **Image Generation**: AI-generated images using DALL-E
- **Analytics**: Track post performance, user engagement
- **Scheduling**: Schedule posts for optimal posting times

### Infrastructure
- **Container**: Docker containerization
- **Orchestration**: Kubernetes for scalability
- **Monitoring**: Prometheus, Grafana for system monitoring
- **Logging**: Structured logging with ELK stack
- **CI/CD**: GitHub Actions for automated testing and deployment

### Security
- **Rate Limiting**: API rate limiting per user
- **Input Validation**: Enhanced input sanitization
- **API Keys**: Secure key rotation and management
- **CORS**: Restricted CORS policies for production

## 📄 License

This project is created for the Demanual AI assignment.

## 🙋‍♂️ Support

For questions or issues, please contact the development team or create an issue in the repository.

---

Built with ❤️ for Demanual AI Assignment
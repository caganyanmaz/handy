# Handy AI Assistant

A voice-powered AI assistant that can answer questions based on your documents using real-time speech-to-text and text-to-speech capabilities.

## 🚀 Features

- 🎤 **Voice Input**: Speak naturally to ask questions
- 🔊 **Voice Output**: Listen to AI responses through your speakers
- 📚 **Document Retrieval**: AI answers based on your uploaded documents
- 💬 **Real-time Chat**: WebSocket-based communication for instant responses
- 🎨 **Modern UI**: Beautiful React frontend with smooth animations
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Architecture

- **Frontend**: React with TypeScript, WebSocket client, audio recording/playback
- **Backend**: Flask with WebSocket support, ElevenLabs integration, LangChain for document retrieval
- **AI**: OpenAI GPT-4 for question answering
- **Vector Database**: ChromaDB for document storage and retrieval

## 📋 Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- OpenAI API key
- ElevenLabs API key (optional, for voice features)

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd handy
```

### 2. Install all dependencies
```bash
npm run install-all
```

### 3. Set up environment variables
Create a `.env` file in the backend directory:
```bash
cd backend
cp .env.example .env
```

Edit the `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### 4. Install Python dependencies
```bash
cd backend
pip install -r requirements.txt
```

## 🚀 Quick Start

### Option 1: Start both frontend and backend together
```bash
npm start
```

### Option 2: Start them separately

**Backend:**
```bash
npm run backend
```

**Frontend:**
```bash
npm run frontend
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

## 📖 Usage

1. **Start the application** using one of the methods above
2. **Allow microphone permissions** when prompted by your browser
3. **Click the microphone button** to start recording
4. **Speak your question** clearly
5. **Click stop** when you're done speaking
6. **Listen to the AI response** through your speakers

## 🗂️ Project Structure

```
handy/
├── backend/
│   ├── app.py              # Flask application with WebSocket support
│   ├── utils.py            # ElevenLabs integration utilities
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.tsx    # Main chat component
│   │   │   └── ChatInterface.css    # Chat component styles
│   │   ├── App.tsx                  # Main app component
│   │   └── App.css                  # App-level styles
│   ├── package.json                 # Frontend dependencies
│   └── README.md                   # Frontend documentation
├── package.json                    # Root package.json for project management
└── README.md                      # This file
```

## 🔧 Configuration

### Backend Configuration

The backend can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `ELEVENLABS_API_KEY`: Your ElevenLabs API key (optional)
- `FLASK_ENV`: Set to 'development' for debug mode
- `PORT`: Port for the Flask server (default: 5000)

### Frontend Configuration

The frontend can be configured through environment variables:

- `REACT_APP_WS_URL`: WebSocket URL (default: ws://localhost:5000/chat)
- `REACT_APP_API_URL`: Backend API URL (default: http://localhost:5000)

## 🧪 Development

### Backend Development

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

### Frontend Development

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## 🐛 Troubleshooting

### Common Issues

**Connection Issues:**
- Ensure both frontend and backend are running
- Check that the WebSocket URL is correct
- Verify firewall settings

**Audio Issues:**
- Allow microphone permissions in your browser
- Check that your microphone is working
- Ensure speakers/headphones are connected

**API Key Issues:**
- Verify your OpenAI API key is valid
- Check that your ElevenLabs API key is set (if using voice features)
- Ensure environment variables are properly loaded

### Debug Mode

To enable debug mode for the backend:
```bash
export FLASK_ENV=development
python app.py
```

## 📝 API Documentation

### WebSocket Endpoints

- `ws://localhost:5000/chat` - Main chat WebSocket endpoint

### Message Format

**Client to Server:**
- Raw audio bytes (ArrayBuffer)

**Server to Client:**
- JSON messages: `{"type": "answer", "text": "AI response"}`
- Audio chunks: Raw audio bytes (ArrayBuffer)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for GPT-4
- [ElevenLabs](https://elevenlabs.io/) for voice synthesis
- [LangChain](https://langchain.com/) for document retrieval
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [React](https://reactjs.org/) for the frontend framework
- [Flask](https://flask.palletsprojects.com/) for the backend framework 
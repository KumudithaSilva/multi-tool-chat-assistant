# 🛒✨ Multi-Tool Chat Assistant — Agentic Grocery AI System

<p align="center">
  <img src="https://img.shields.io/badge/AI-Agentic%20LLM-6A1B9A" />
  <img src="https://img.shields.io/badge/LLM-OpenAI%20-455A164" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-FF7043" />
  <img src="https://img.shields.io/badge/Design-SOLID%20Principles-17256b" />
  <img src="https://img.shields.io/badge/Code%20Style-PEP8-045E1A" />
  <img src="https://img.shields.io/badge/License-MIT-45a5d7" />
</p>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [📦 The Real-World Problem](#-the-real-world-problem)
- [💡 Our Solution](#-our-solution)
- [✨ Core Features](#-core-features)
- [🧩 Core Functionalities](#-core-functionalities)
- [📸 Chat Assistant App Output (UI Preview)](#-chat-assistant-app-output-ui-preview)
- [🏗️ Architecture](#-architecture)
- [💻 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🔄 How It Works](#-how-it-works)
- [💬 Usage](#-usage)
- [🛠️ Tool System](#️-tool-system)
- [🎨 Design Patterns](#-design-patterns)
- [🔐 Key Concepts](#-key-concepts)
- [📊 Data Flow Example](#-data-flow-example)
- [🤝 Contributing](#-contributing)
- [🔀 Git Flow Workflow](#-git-flow-workflow)


## 🎯 Overview

The **Multi-Tool Chat Assistant** is an AI chatbot system designed specifically for grocery store operations. It uses OpenAI's GPT-4 model with function calling capabilities to intelligently execute tools such as:

- Understanding grocery-related customer queries
- Performing multi-step reasoning
- Automatically selecting and executing tools  
- Retrieving item prices
- Generating customer quotes
- Creating receipt PDFs
- Sending emails to customers

The system is built using **clean architecture principles** with clear separation of concerns, making it maintainable, testable, and extensible and The assistant doesn’t just answer questions —  it **decides what action to take**, executes it, and delivers results.


## 📦 The Real-World Problem

Traditional grocery systems:

- Require manual staff intervention for price checks
- Lack automated quote generation
- Cannot generate structured receipts instantly
- Do not intelligently handle multi-step customer requests
- Have no autonomous decision-making capability

Customers may say:

> “Generate a quote for 1 Oats and 2 milk packs and send it to my email.”

A typical chatbot can respond — but cannot **execute the workflow autonomously**.

We needed:

- Intent understanding  
- Tool orchestration  
- Multi-step execution  
- Structured output generation  
- Professional communication  


## 💡 Our Solution

We built an **Agentic AI Grocery Assistant** that:

- Detects user intent
- Determines if tools are required
- Selects the correct tool(s)
- Executes them
- Feeds tool output back into the LLM
- Generates final professional responses

This creates a **closed-loop reasoning + execution system**.


## ✨ Core Features

### 🧠 Agentic Capabilities

- Intent detection
- Multi-step reasoning
- Autonomous tool selection
- Recursive tool execution
- Context-aware responses

### 🛒 Grocery-Specific Functionalities

- ✅ Item availability check  
- 💲 Price lookup  
- 📦 Inventory quantity retrieval  
- 🧾 Quote generation  
- 📄 Receipt PDF generation  
- 📧 Email delivery  


## 🧩 Core Functionalities

### Core Capabilities
- **AI-Powered Conversations**: Uses OpenAI's GPT-4o-mini model for natural language understanding
- **Automatic Tool Execution**: Intelligently calls tools when needed based on user requests
- **Function Calling**: Leverages OpenAI's function calling feature for reliable tool execution
- **Chat History Management**: Maintains conversation context across sessions

### Grocery-Specific Tools
- **Item Availability Check**: Verify if products are in stock
- **Price Lookup**: Get real-time product pricing
- **Quote Generation**: Create and customize customer quotes
- **PDF Receipts**: Generate professional receipt documents
- **Email Integration**: Send quotes and receipts directly to customers
- **Inventory Management**: Track item counts and availability

### User Interfaces
- **FastAPI Backend**: RESTful API for programmatic access
- **Streamlit Frontend**: Interactive web-based chat interface
- **Session Management**: Persistent chat history and user preferences


## 📸 Chat Assistant App Output (UI Preview)

#### Chat Assistant Chat Output

<img width="500" height="900" alt="image" src="https://github.com/user-attachments/assets/4acfc510-d0e8-48bf-b997-813641f8aae1"/>

#### Chat Assistant Generated Email Output

<img width="500" height="450" alt="image" src="https://github.com/user-attachments/assets/861cca90-9db4-40b2-9e11-0136a619e2c2"/>



## 🏗️ Architecture

The project follows a **layered, interface-based architecture** with clear separation of concerns:

```
┌─────────────────────────────────────┐
│       UI Layer (Streamlit)          │
│       Backend API (FastAPI)         │
├─────────────────────────────────────┤
│    Components (Business Logic)      │
│  ├─ Chat Completion Service         │
│  ├─ Chat Connection Service         │
│  └─ Chat Initialization Service     │
├─────────────────────────────────────┤
│    Infrastructure (Integrations)    │
│  ├─ OpenAI Service                  │
│  ├─ Tool Handler & Executor         │
│  ├─ Chat History                    │
│  ├─ Environment & Configuration     │
│  └─ Custom Tools                    │
├─────────────────────────────────────┤
│    Interfaces (Contracts)           │
│  ├─ Chat Interfaces                 │
│  ├─ Tool Interfaces                 │
│  ├─ Infrastructure Interfaces       │
│  └─ Bot Interfaces                  │
├─────────────────────────────────────┤
│    Container (Dependency Injection) │
│    Dependency Wiring & Factory      │
├─────────────────────────────────────┤
│    Core (Utilities & Patterns)      │
│    Singleton Meta-class             │
└─────────────────────────────────────┘
```

### Layer Explanations

**UI/API Layer**: Handles HTTP requests and provides web interfaces
- `ui/app.py` - Streamlit web interface
- `backend/chatbot_fastapi.py` - FastAPI REST endpoints

**Components Layer**: Business logic orchestration
- `ChatCompletionService` - Generates AI responses with tool calling
- `ChatConnectionService` - Manages OpenAI client connection
- `ChatInitializationService` - Initializes chat sessions

**Infrastructure Layer**: External integrations and utilities
- `OpenAIService` - Communicates with OpenAI API
- `GroceryToolExecutor` - Executes tool calls from AI responses
- `ChatHistory` - Stores and retrieves conversation history
- `PromptProvider` - Manages system prompts

**Interfaces Layer**: Abstract contracts (dependency inversion)
- Defines contracts that implementations must follow
- Enables loose coupling and testability

**Container Layer**: Dependency injection factory
- Wires all dependencies together
- Follows the Factory and Singleton patterns

## 💻 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend API** | FastAPI | High-performance REST API with async support |
| **Frontend** | Streamlit | Interactive web interface for chat |
| **AI Model** | OpenAI GPT-4o-mini | Language understanding & function calling |
| **Data Format** | JSON/Pydantic | Structured data & validation |
| **Logging** | Python logging | Application monitoring & debugging |
| **Environment** | Python-dotenv | Configuration management |
| **PDF Generation** | ReportLab/PyPDF | Receipt document creation |
| **Email** | Python email | SMTP-based email delivery |

**Python Version**: 3.11+ (< 3.12)

## 📁 Project Structure

```
multi-tool-chat-assistant/
├── backend/
│   └── chatbot_fastapi.py          # FastAPI routes & server setup
├── src/
│   ├── components/                 # Business logic orchestration
│   │   ├── chat_completion.py      # Response generation with tools
│   │   ├── chat_connection.py      # OpenAI client management
│   │   └── chat_initialization.py  # Chat session setup
│   │
│   ├── container/
│   │   └── chatbot_container.py    # Dependency injection factory
│   │
│   ├── core/
│   │   └── singleton_meta.py       # Singleton pattern implementation
│   │
│   ├── infrastructure/             # External integrations
│   │   ├── openai_service.py       # OpenAI API client wrapper
│   │   ├── openai_client.py        # Low-level OpenAI integration
│   │   ├── openai_provider.py      # API key management
│   │   ├── tool_handler.py         # Tool execution engine
│   │   ├── tool_schema.py          # Function schema generation
│   │   ├── chat_history.py         # Conversation storage
│   │   ├── prompt.py               # System prompt management
│   │   ├── dotenv.py               # Environment loading
│   │   └── email_provider.py       # Email service setup
│   │
│   ├── interfaces/                 # Abstract contracts
│   │   ├── bot/                    # AI client interfaces
│   │   ├── chat/                   # Chat service interfaces
│   │   ├── infra/                  # Infrastructure interfaces
│   │   ├── logging/                # Logger interface
│   │   └── tools/                  # Tool execution interfaces
│   │
│   ├── logs/
│   │   └── logger_singleton.py     # Singleton logger instance
│   │
│   ├── tools/
│   │   └── grocery/                # Grocery-specific tools
│   │       ├── tool_call_count.py         # Get item count
│   │       ├── tool_call_price.py         # Get item price
│   │       ├── tool_call_availability.py  # Check stock
│   │       ├── tool_call_quote.py         # Generate quote
│   │       ├── too_call_pdf_generator.py  # Create PDF receipts
│   │       ├── tool_call_email.py         # Send emails
│   │       └── grocery_data.py            # Product database
│   │
│   └── utils/                      # Utility functions
│       ├── email_service.py        # Email operations
│       ├── email_template.py       # Email HTML templates
│       ├── pdf_generator.py        # PDF creation
│       ├── item_price.py           # Price lookup utilities
│       ├── item_count.py           # Count utilities
│       ├── item_existence.py       # Availability checks
│       ├── generate_quote.py       # Quote generation
│       └── config_loader.py        # Configuration reading
│
├── ui/
│   └── app.py                      # Streamlit chatbot interface
│
├── config.json                     # Shop configuration (name, contact)
├── setup.py                        # Package configuration
├── requirement.txt                 # Python dependencies
└── README.md                       # This file
```

## 🔄 How It Works

### Request Flow

```
User Input (Streamlit UI)
        │
        ▼
FastAPI Backend (/chat/send_request)
        │
        ▼
ChatCompletionService
        │
        ├─► Tool Schema Generator
        │   (Creates function definitions)
        │
        ├─► OpenAI Service
        │   (Sends messages + tools to GPT-4)
        │
        ▼
AI Model Response
        │
        ├─ If tool call requested:
        │  │
        │  ├─► GroceryToolExecutor
        │  │   (Parses tool call & arguments)
        │  │
        │  ├─► Tool Registry
        │  │   (Gets matching tool)
        │  │
        │  ├─► Execute Tool
        │  │   (Calls tool with arguments)
        │  │
        │  ├─► Add Result to Messages
        │  │   (Send response back to AI)
        │  │
        │  └─► Recursive Call
        │      (AI generates next response)
        │
        └─ If response generated:
           │
           └─► Return to UI
               (Display to user)
```

### Step-by-Step Execution

1. **User sends message** via Streamlit UI to `/chat/send_request` endpoint

2. **Message enrichment**: Tool schema is generated (function definitions)

3. **OpenAI call**: Message + tools sent to GPT-4o-mini model

4. **AI processing**: Model decides if tools are needed

5. **Conditional routing**:
   - If tool call: Execute the tool with provided arguments
   - If direct response: Return answer immediately

6. **Tool execution cycle**:
   - Parse tool call from AI response
   - Look up tool in registry
   - Execute with arguments
   - Add result to message history
   - Send back to AI for continuation

7. **Response generation**: Final answer sent to user

### Chat Initialization Flow

```
Request to /chat/initialize
        │
        ▼
ChatInitializationService
        │
        ├─► PromptProvider
        │   (Gets system prompt)
        │
        ├─► ChatHistory
        │   (Creates initial history with prompt)
        │
        └─► Return to Frontend
            (Display initial messages)
```


## 💬 Usage

### Starting the Application

#### Terminal 1: Start FastAPI Backend
```bash
cd backend
python -m uvicorn chatbot_fastapi:app --reload
```
Backend runs on `http://localhost:8000`

#### Terminal 2: Start Streamlit Frontend
```bash
streamlit run ui/app.py
```
Frontend opens at `http://localhost:8501`

### API Endpoints

#### Initialize Chat
```bash
GET /chat/initialize

Response:
{
  "messages": [
    {
      "role": "assistant",
      "content": "Hello! I'm your grocery assistant..."
    }
  ]
}
```

#### Send Message
```bash
POST /chat/send_request

Request:
{
  "messages": [
    {
      "role": "user",
      "content": "What's the price of Oats?"
    }
  ]
}

Response:
{
  "response": "Oats are $5.99 per unit..."
}
```

### Example Conversations

**Query 1: Price Check**
```
User: "How much do Oats cost?"
AI: [Calls get_item_price tool] → "Oats cost $5.99"
```

**Query 2: Stock Check**
```
User: "Do you have Yogurt in stock?"
AI: [Calls check_item_existence tool] → "Yes, we have Yogurt in stock!"
```

**Query 3: Create Quote**
```
User: "Generate a quote for 1 Oats and 2 Yogurt"
AI: [Calls generate_quote tool] → "Here's your quote..."
```

**Query 4: Send Receipt**
```
User: "Send me a receipt for my order"
AI: [Calls email_tool + pdf_generator] → "Receipt sent to your email!"
```

## 🛠️ Tool System

### Available Tools

| Tool Name | Purpose | Parameters |
|-----------|---------|-----------|
| `get_item_count` | Get inventory quantity | `item_name` (string) |
| `get_item_price` | Get product price | `item_name` (string) |
| `check_item_existence` | Verify product availability | `item_name` (string) |
| `generate_quote` | Create customer quote | `items` (dict of item→qty) |
| `generate_receipt_pdf` | Create PDF receipt | `order_data` (dict), `customer` (string) |
| `send_email` | Email quote/receipt | `recipient email` (string),  `customer` (string), `order_data` (dict) |

### Adding New Tools

#### Step 1: Create Tool Class
Create a new file in `src/tools/grocery/`:

```python
# src/tools/grocery/tool_call_custom.py
from interfaces.tools.i_tool import ITool

class CustomTool(ITool):
    def __init__(self):
        self.name = "custom_tool"
        self.description = "Description of what it does"
        self.parameters = {
            "type": "object",
            "properties": {
                "param1": {"type": "string", "description": "..."},
            },
            "required": ["param1"]
        }
    
    def execute(self, arguments):
        # Implementation
        return "Tool result"
```

#### Step 2: Register in Container
Update `src/container/chatbot_container.py`:

```python
from tools.grocery.tool_call_custom import CustomTool

def create_chat_completion_service(self, ai_client, ...):
    tools = [
        # ... existing tools ...
        CustomTool(),  # Add your tool
    ]
```

#### Step 3: Tool Execution
Your tool will automatically be called by the AI when needed!

### Tool Interface

All tools must implement `ITool`:

```python
class ITool(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Tool's registered name"""
        pass

    @property
    def schema(self) -> Dict:
        """Tool's schema"""
        return {
            "name": self.name,
            "description": getattr(self, "description", "No description provided"),
            "parameters": getattr(self, "parameters", {}),
        }

    @abstractmethod
    def execute(self, arguments: dict) -> str:
        """Execute the tool"""
        pass
```

## 🎨 Design Patterns

### 1. **Dependency Injection**
- Loose coupling through constructor injection
- All dependencies provided by `ChatbotContainer`
- Easy testing with mock dependencies

```python
class ChatCompletionService:
    def __init__(self, openai_service: IOpenAIOperations, 
                 tool_schema: IToolSchema):
        # Dependencies injected
        pass
```

### 2. **Factory Pattern**
- `ChatbotContainer` creates service instances
- Centralized object creation
- Manages complex dependency graphs

```python
container = ChatbotContainer()
service = container.create_chat_completion_service(ai_client)
```

### 3. **Singleton Pattern**
- Logger instantiated once globally
- Ensures single point of logging

```python
logger = Logger(name="app")  # Singleton
```

### 4. **Strategy Pattern**
- Tool executor abstraction
- Different tool implementations
- Swappable tool registry

```python
tool_executor: IToolExecutor = GroceryToolExecutor(tools)
```

### 5. **Registry Pattern**
- Tool registry for dynamic execution
- `{tool_name: tool_instance}` mapping

```python
self._tool_registry = {tool.name: tool for tool in tools}
```

## 🔐 Key Concepts

### Interface-Based Design
Every major component has an interface (`I...`):
- Enables testing with mocks
- Enforces contracts
- Supports polymorphism

### Separation of Concerns
- **Components**: Business orchestration
- **Infrastructure**: External integrations
- **Utils**: Helper functions
- **Interfaces**: Contracts/abstractions

### Dependency Inversion Principle
- High-level modules don't depend on low-level modules
- Both depend on abstractions (interfaces)
- Makes code flexible and testable

### Plugin Architecture
- Tools are plugins registered at startup
- New tools added without modifying existing code
- Tool executor handles all registered tools automatically

## 📊 Data Flow Example

**User asks: "How much are Oats and do you have Yogurt?"**

```
Message: "How much are Oats and do you have Yogurt?"
   │
   ├─► Tool Schema Generated:
   │   [get_item_price, check_item_existence, ...]
   │
   ├─► Sent to GPT-4:
   │   "User asked for Oats price and Yogurt availability"
   │   Tools available: [...]
   │
   ├─► AI Decision:
   │   Tool calls needed:
   │   1. get_item_price(item_name="oats")
   │   2. check_item_existence(item_name="yogurt")
   │
   ├─► Execute Tool Calls:
   │   1. get_item_price → "$5.99"
   │   2. check_item_existence → "In stock"
   │
   ├─► Add Results to Context:
   │   Previous messages + tool results
   │
   ├─► Second GPT-4 Call:
   │   "Here are the results..."
   │   AI generates natural response
   │
   └─► Response: "Oats cost $5.99 and we have Yogurt in stock!"
```


## 🤝 Contributing

We welcome contributions related to:

- ⚙️ Additional grocery tools
- 📊 Database integration for inventory
- 🔉 Additional language support
- 🧠 AI & Prompt Engineering  
- 🧱 Architecture Improvements  
- 🌐 Backend Enhancements  
- 🎨 UI Improvements  
- 🧪 Testing & Quality Assurance  

### Contribution Steps

1. 🍴 Fork the repository  
2. 🌿 Create a `feature/*` branch  
3. 🛠️ Commit changes with clear messages  
4. 📤 Open a Pull Request  


## 🔀 Git Flow Workflow

The project follows a Git Flow–inspired workflow:

- 🌿 `master` — Stable, production-ready releases  
- 🌱 `develop` — Active development branch  
- ✨ `feature/*` — New feature branches  

### Typical Workflow

1. Pull latest changes from `develop`  
2. Create a `feature/*` branch  
3. Implement and test changes  
4. Open PR → Merge into `develop`  
5. Release from `develop` → Merge into `master`  

This ensures stability while enabling safe feature development.

---

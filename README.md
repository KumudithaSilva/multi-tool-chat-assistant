# 🛒✨ Multi-Tool Chat Assistant — Agentic Grocery AI System

<p align="center">
  <img src="https://img.shields.io/badge/AI-Agentic%20LLM-6A1B9A" />
  <img src="https://img.shields.io/badge/LLM-OpenAI%20-455A164" />
    <img src="https://img.shields.io/badge/PDF-FPDF-FF9900" />
  <img src="https://img.shields.io/badge/Email-Mailtrap-00BFFF" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-FF7043" />
  <img src="https://img.shields.io/badge/Design-SOLID%20Principles-17256b" />
  <img src="https://img.shields.io/badge/Code%20Style-PEP8-045E1A" />
  <img src="https://img.shields.io/badge/License-MIT-45a5d7" />
</p>


## 🎯 Overview

The Multi-Tool Chat Assistant is an AI-powered chatbot system built specifically for modern grocery store operations. It goes beyond traditional Q&A chatbots by combining intelligent intent understanding with autonomous tool execution using OpenAI’s GPT-4 function-calling capabilities.

In real-world grocery environments, common operational challenges include:
  - Manual staff intervention for price checks
  - No automated quote generation
  - Inability to instantly create structured receipts
  - Poor handling of multi-step customer requests
  - Lack of autonomous decision-making

For example, when a customer says::

> “Generate a quote for 1 Oats and 2 milk packs and send it to my email.”

A typical chatbot may respond conversationally — but it cannot execute the full workflow.


The Multi-Tool Chat Assistant solves this by:

- Understanding grocery-related customer queries
- Performing multi-step reasoning
- Automatically selecting and executing tools  
- Retrieving item prices
- Generating customer quotes
- Creating receipt PDFs
- Sending emails to customers

The system is built using **clean architecture principles** with clear separation of concerns, making it maintainable, testable, and extensible and The assistant doesn’t just answer questions —  it **decides what action to take**, executes it, and delivers results.


## ✨ Core Features

### 🧠 Agentic Capabilities

- Intent detection
- Multi-step reasoning
- Autonomous tool selection
- Recursive tool execution
- Context-aware responses

### 🛒 Grocery-Specific Functionalities

- Item availability check  
- Price lookup  
- Inventory quantity retrieval  
- Quote generation  
- Receipt PDF generation  
- Email delivery  


## 📸 Chat Assistant App Output (UI Preview)

#### Chat Assistant Chat Output

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/4acfc510-d0e8-48bf-b997-813641f8aae1"/>


#### Chat Assistant Generated Email Output

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/861cca90-9db4-40b2-9e11-0136a619e2c2"/>



## 🏗️ Architecture

The system is follows a layered, interface-driven architecture, designed to ensure modularity, maintainability, and extensibility. Fundamental design principles include dependency injection, interface-based abstraction, separation of concerns, and a plugin-oriented tool architecture.

<b>Key Architectural Highlights:</b>
- Dependencies are injected via a centralized container, promoting loose coupling and easy testing.
- Core components define interfaces to enforcing contracts and enabling polymorphic behavior.
- Tools are treated as modular plugins, supporting dynamic registration and execution without necessitating modifications to existing code.
- Singleton patterns are used for global utilities like logging.
- The architecture defines clear layers: UI/API, Components (business logic), Infrastructure (integrations), Interfaces (contracts), and Container (dependency management).

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

### Layer Responsibilities

- <b>UI/API Layer</b>: Facilitates user interactions and exposes RESTful endpoints.
- <b>Components Layer</b>: Orchestrates business logic and AI-driven chat operations.
- <b>Infrastructure Layer</b>: Manages external integrations, tool execution, and system utilities.
- <b>Interfaces Layer</b>: Defines abstract contracts to ensure modularity and testability.
- <b>Container LayerL</b>: Oversees dependency injection and management of singleton instances.


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

## 🤝 Contributing

We welcome contributions related to:

- Additional grocery tools
- Database integration for inventory
- Additional language support
- AI & Prompt Engineering  
- Architecture Improvements  
- Backend Enhancements  
- UI Improvements  
- Testing & Quality Assurance  

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

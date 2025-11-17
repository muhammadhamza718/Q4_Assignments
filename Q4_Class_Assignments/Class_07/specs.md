# Technical Specifications for GEMINI CLI

## 1. Overview
The GEMINI CLI is a command-line interface tool designed to interact with a large language model (LLM), likely Google's Gemini, with a focus on context management and integration with web development frameworks like FastAPI.

## 2. Core Functionality

The CLI must support the following basic commands:

| Command | Description | Functionality Details |
| :--- | :--- | :--- |
| `/auth` | Authenticate the user. | Must securely handle user credentials and establish a session for API access. |
| `/memory` | Manage conversation memory/context. | Must support sub-commands for: `show` (display current context), `add` (add new context), `refresh` (reload context from file), and `list` (list available context files/levels). |
| `/clear` | Clear the screen and conversation history. | Resets the terminal display and the current session's conversation history, but not the persistent context files. |
| `/model` | Change the underlying LLM model. | Allows the user to select a different model for the current session. |

## 3. Context and Memory Management (`GEMINI.md`)

The CLI's behavior is heavily influenced by a context file named `GEMINI.md`. This file serves as the primary source of memory or context for the LLM.

### 3.1. Context File Hierarchy

The CLI must search for and load context from `GEMINI.md` files at multiple, hierarchical levels. The context should be merged or prioritized based on the following order (from broadest to most specific):

1.  **Root/Home Directory Level:**
    *   **Path Example:** `C:\Users\Ali\.gemini\GEMINI.md` (or equivalent on other OS, e.g., `~/.gemini/GEMINI.md`).
    *   **Purpose:** Defines global rules and settings that apply to **every project** using the GEMINI-CLI.
2.  **Project Level:**
    *   **Path:** Located in the root directory of the current project.
    *   **Purpose:** Defines context specific to the **particular project** (e.g., tech stack, general project rules, main test cases).
3.  **Module Level:**
    *   **Path:** Located within a specific module or feature directory.
    *   **Purpose:** Provides instructions and context relevant to a **specific module/feature** within the project.

### 3.2. Context Content

The `GEMINI.md` file should contain information such as:
*   Tech Stack details.
*   Test cases.
*   Multi-lingual requirements.
*   Specific instructions or rules for the LLM to follow.

## 4. FastAPI Integration (Assignment Component)

The CLI should be capable of generating code and instructions related to a FastAPI project structure.

### 4.1. Project Setup (Assumed)

The project will follow a standard Python/FastAPI setup, including:
*   Project initialization (e.g., via `uv` or similar tool).
*   Virtual environment management (optional).
*   Creation of instances and endpoints based on user prompts.

### 4.2. Server Execution

The standard command for running the FastAPI server is:
`uv run uvicorn main:app --reload`

| Component | Description |
| :--- | :--- |
| `main` | The name of the Python file (e.g., `main.py`). |
| `app` | The variable name of the FastAPI instance within the file. |
| `--reload` | Enables auto-restart on code changes for development. |
| `Uvicorn` | The ASGI server that runs the FastAPI application. |

### 4.3. Access Endpoints

*   **Base URL:** `http://localhost:8000`
*   **Documentation (Swagger UI/ReDoc):** `http://localhost:8000/docs`

## 5. Assignment Requirements (FastAPI Homework)

The CLI must be able to generate the code for a simple banking application with the following endpoints and logic:

1.  **`/authenticate` Endpoint:**
    *   **Input:** Requires `name` and `pin_number` from the user.
    *   **Function:** Authenticates the user.
2.  **`/bank-transfer` Endpoint:**
    *   **Input:** Requires `receipents_name` and the `amount to transfer`.
    *   **Function:**
        *   Deducts the amount from the sender's account.
        *   Adds the amount to the receiver's account.
3.  **Post-Transfer Verification:**
    *   After a bank transfer, the system should be able to re-authenticate with the receiver's name to verify that the transferred amount has been successfully added to their `bank_balance`.

# GEMINI CLI Context: FastAPI Banking Assignment (Updated)

This file serves as the project-level context (`GEMINI.md`) for the Gemini CLI to generate the required code for the FastAPI banking assignment.

## 1. Tech Stack and Project Details

| Component | Detail |
| :--- | :--- |
| **Framework** | FastAPI |
| **Server** | Uvicorn |
| **Language** | Python 3.11+ |
| **Database/Data Structure** | In-memory dictionary for user accounts (for simplicity in this assignment). |
| **Project Goal** | Implement a simple banking API with authentication, balance retrieval, and bank transfer functionality. |

## 2. Data Structure (In-Memory Accounts) - UPDATED

The application must maintain a simple in-memory database of user accounts. The account identifier has been changed from a name to a string-based account number.

The structure for each account should be a dictionary keyed by the **account number** and containing:

*   `pin`: The user's PIN (string, for authentication).
*   `balance`: The current balance (float).

**Example Initial Data:**

```python
ACCOUNTS = {
    "123456789": {"pin": "1234", "balance": 1000.0},
    "987654321": {"pin": "4321", "balance": 1000.0},
    # Add more accounts as needed for testing
}
```

## 3. Required Endpoints and Logic - UPDATED

The Gemini CLI must generate the necessary Python code (`main.py`) to implement the following endpoints:

### 3.1. `/authenticate`

*   **Method:** POST
*   **Request Body:** Must accept `account_number` (string) and `pin` (string).
*   **Logic:**
    1.  Check if the `account_number` exists in the `ACCOUNTS` data structure.
    2.  If the account exists, verify the provided `pin` against the stored PIN.
    3.  **Success Response:** Return a success message.
    4.  **Failure Response:** Raise an `HTTPException` (401 Unauthorized) for invalid credentials.

### 3.2. `/balance/{account_number}`

*   **Method:** GET
*   **Path Parameter:** `account_number` (string).
*   **Logic:**
    1.  Check if the `account_number` exists in the `ACCOUNTS` data structure.
    2.  **Success Response:** Return the `account_number` and the current `balance`.
    3.  **Failure Response:** Raise an `HTTPException` (404 Not Found) if the account does not exist.

### 3.3. `/bank-transfer`

*   **Method:** POST
*   **Request Body:** Must accept `from_account` (string), `to_account` (string), and `amount` (float).
*   **Logic:**
    1.  **Account Check:** Ensure both `from_account` and `to_account` exist.
    2.  **Balance Check:** Ensure the sender's account has sufficient `balance` to cover the `amount`.
    3.  **Transaction:**
        *   Deduct the `amount` from the sender's `balance`.
        *   Add the `amount` to the recipient's `balance`.
    4.  **Success Response:** Return a confirmation message.
    5.  **Failure Response:** Raise an `HTTPException` (404 Not Found or 400 Bad Request for insufficient funds) for transaction failures.

## 4. Test Case Requirement - UPDATED

A successful run of the generated code should demonstrate the following sequence:

1.  **Initial State:** Check the balance for account "123456789" and "987654321" (both should be 1000.0).
2.  **Transfer:** Account "123456789" transfers 100.0 to account "987654321".
3.  **Verification (Sender):** Check the balance for account "123456789" to confirm the deduction (new balance: 900.0).
4.  **Verification (Receiver):** Check the balance for account "987654321" to confirm the addition (new balance: 1100.0).

## 5. Module-Specific Instructions

This `GEMINI.md` is at the project level. No module-specific instructions are required at this time.

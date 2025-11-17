# GEMINI CLI Context: FastAPI Banking Assignment

This file serves as the project-level context (`GEMINI.md`) for the Gemini CLI to generate the required code for the FastAPI banking assignment.

## 1. Tech Stack and Project Details

| Component | Detail |
| :--- | :--- |
| **Framework** | FastAPI |
| **Server** | Uvicorn |
| **Language** | Python 3.11+ |
| **Database/Data Structure** | In-memory dictionary for user accounts (for simplicity in this assignment). |
| **Project Goal** | Implement a simple banking API with authentication and bank transfer functionality. |

## 2. Data Structure (In-Memory Accounts)

The application must maintain a simple in-memory database of user accounts. The structure for each account should include:

*   `name`: The user's name (string, unique identifier).
*   `pin_number`: The user's PIN (integer, for authentication).
*   `bank_balance`: The current balance (float or integer).

**Example Initial Data:**

```python
ACCOUNTS = {
    "Alice": {"pin_number": 1234, "bank_balance": 1000.00},
    "Bob": {"pin_number": 5678, "bank_balance": 500.00},
    # Add more accounts as needed for testing
}
```

## 3. Required Endpoints and Logic

The Gemini CLI must generate the necessary Python code (`main.py`) to implement the following endpoints:

### 3.1. `/authenticate`

*   **Method:** POST
*   **Request Body:** Must accept `name` (string) and `pin_number` (integer).
*   **Logic:**
    1.  Check if the `name` exists in the `ACCOUNTS` data structure.
    2.  If the user exists, verify the provided `pin_number` against the stored PIN.
    3.  **Success Response:** Return a success message and the user's current `bank_balance`.
    4.  **Failure Response:** Return an appropriate error message (e.g., "Invalid credentials" or "User not found").

### 3.2. `/bank-transfer`

*   **Method:** POST
*   **Request Body:** Must accept `sender_name` (string), `sender_pin` (integer), `receipents_name` (string), and `amount` (float/integer).
*   **Logic:**
    1.  **Authentication:** First, authenticate the sender using `sender_name` and `sender_pin`. If authentication fails, stop and return an error.
    2.  **Recipient Check:** Ensure the `receipents_name` exists in the `ACCOUNTS` data structure.
    3.  **Balance Check:** Ensure the `sender_name` has sufficient `bank_balance` to cover the `amount`.
    4.  **Transaction:**
        *   Deduct the `amount` from the sender's `bank_balance`.
        *   Add the `amount` to the recipient's `bank_balance`.
    5.  **Success Response:** Return a confirmation message with the new balances for both the sender and the recipient.
    6.  **Failure Response:** Return an error for insufficient funds, invalid recipient, or other transaction failures.

## 4. Test Case Requirement

A successful run of the generated code should demonstrate the following sequence:

1.  **Initial State:** Authenticate "Alice" and "Bob" to show their initial balances.
2.  **Transfer:** "Alice" transfers 100.00 to "Bob".
3.  **Verification (Sender):** Authenticate "Alice" again to confirm the deduction (new balance: 900.00).
4.  **Verification (Receiver):** Authenticate "Bob" again to confirm the addition (new balance: 600.00).

## 5. Module-Specific Instructions

This `GEMINI.md` is at the project level. No module-specific instructions are required at this time.

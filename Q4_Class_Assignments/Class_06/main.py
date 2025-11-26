
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict

# In-memory data structure for accounts
ACCOUNTS = {
    "123456789": {"pin": "1234", "balance": 1000.0},
    "987654321": {"pin": "4321", "balance": 1000.0},
}

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Banking Application!"}

# Pydantic models for request and response bodies
class AuthRequest(BaseModel):
    account_number: str
    pin: str

class AuthResponse(BaseModel):
    success: bool
    message: str

class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float

class TransferResponse(BaseModel):
    success: bool
    message: str

class BalanceResponse(BaseModel):
    account_number: str
    balance: float

@app.post("/authenticate", response_model=AuthResponse)
def authenticate(request: AuthRequest):
    """
    Authenticates a user based on account number and PIN.
    """
    account = ACCOUNTS.get(request.account_number)
    if account and account["pin"] == request.pin:
        return AuthResponse(success=True, message="Authentication successful.")
    else:
        raise HTTPException(status_code=401, detail="Invalid account number or PIN.")

@app.get("/balance/{account_number}", response_model=BalanceResponse)
def get_balance(account_number: str):
    """
    Retrieves the balance for a given account number.
    """
    account = ACCOUNTS.get(account_number)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")
    return BalanceResponse(account_number=account_number, balance=account["balance"])


@app.post("/bank-transfer", response_model=TransferResponse)
def bank_transfer(request: TransferRequest):
    """
    Transfers funds from one account to another.
    """
    from_account_data = ACCOUNTS.get(request.from_account)
    to_account_data = ACCOUNTS.get(request.to_account)

    if not from_account_data:
        raise HTTPException(status_code=404, detail="Sender's account not found.")
    if not to_account_data:
        raise HTTPException(status_code=404, detail="Recipient's account not found.")

    if from_account_data["balance"] < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds.")

    # Perform the transfer
    from_account_data["balance"] -= request.amount
    to_account_data["balance"] += request.amount

    return TransferResponse(
        success=True,
        message=f"Successfully transferred {request.amount} from {request.from_account} to {request.to_account}.",
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

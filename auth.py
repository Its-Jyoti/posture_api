from fastapi import Header, HTTPException, status

DUMMY_API_KEY = "test-api-key-123"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != DUMMY_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return True
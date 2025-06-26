import pdb
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from typing import List, Callable

# Secret and algorithm should be set securely in production
JWT_SECRET = "a-string-secret-at-least-256-bits-long"
JWT_ALGORITHM = "HS256"

security = HTTPBearer()

def validate_jwt_and_scope(required_scopes: List[str]) -> Callable:
    def dependency(credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )
        scopes = payload.get("scopes", "").split()
        for scope in required_scopes:
            if scope not in scopes:
                model, action = scope.split(":")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"User does not have permission to {action} {model}",
                )
        return payload
    return dependency 
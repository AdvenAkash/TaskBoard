import os
import uvicorn

if __name__ == "__main__":
    environment = os.getenv("ENVIRONMENT", "development")
    is_production = environment == "production"
    
    uvicorn.run(
        'app.main:app',
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=not is_production,
        log_level="info" if is_production else "debug",
        workers=4 if is_production else 1
    )
from app.config.settings import BaseSettings

class Settings(BaseSettings):
    app_name:str = "AI Chat API"
    model_name:str = "gpt-4"

settings = Settings()
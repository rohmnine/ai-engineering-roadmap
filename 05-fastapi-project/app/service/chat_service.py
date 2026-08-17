from app.utils.logger import log

def chat_service(message:str):
    log(message)
    
    return f"AI回答：{message}"
from fastapi import FastAPI
from send_email import send_email_async
import uvicorn
from dto.mail_dto import Mail
from dotenv import load_dotenv
load_dotenv('.env')

app = FastAPI()

@app.post('/mail/api')
def send_email_asynchronous(mail:Mail):
    send_email_async.apply_async([mail.subject, mail.recipient, mail.message], task_id='hi') # ()
    return {'detail':'Mail Transmission is complete!'}

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
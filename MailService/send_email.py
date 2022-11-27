from asgiref.sync import async_to_sync
from fastapi_mail import FastMail, MessageSchema
from settings import conf, celery_task

async def send_email(message):
    fm = FastMail(conf)
    print('=======1=======')
    await fm.send_message(message)
    print('=======2=======')

@celery_task.task
def send_email_async(subject: str, email_list: list, body: str):
    print('=======0=======')
    message = MessageSchema(
        subject= subject,
        recipients= email_list,
        body= body,
        subtype='html',
    )
    async_to_sync(send_email)(message)
    return True


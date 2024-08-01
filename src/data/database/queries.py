# database operations for email and sms verification
from .main import session
from sqlalchemy import text
import datetime

from sqlalchemy.orm import Session
from .schemas import AccountInformationPostgreSQL

# Account information
# (account_id, generated_data_id, verification_data_id)
def generate_account_information_id(session: Session):
    new_account_info = AccountInformationPostgreSQL()
    session.add(new_account_info)
    session.flush()  # Flush to get the generated ID
    account_information_id = new_account_info.account_id
    session.commit()
    return account_information_id

# Generated data

## Insert
from .schemas import GeneratedDataPostgreSQL

def insert_generated_data(session: Session, **kwargs):
    new_generated_data = GeneratedDataPostgreSQL(**kwargs)
    session.add(new_generated_data)
    session.flush()  # Flush to get the generated ID
    
    generated_data_id = new_generated_data.id
    
    session.commit()
    return generated_data_id

## insert generated_data_id into account_information table

from .schemas import AccountInformationPostgreSQL

def generated_data_id_as_foreign_key(session: Session, generated_data_id):
    new_account_info = AccountInformationPostgreSQL(generated_data_id=generated_data_id)
    session.add(new_account_info)
    session.flush()  # Flush to get the generated ID
    
    account_information_id = new_account_info.account_id
    session.commit()
    
    return account_information_id

# Verification data

## Insert
    
from .schemas import EmailVerificationPostgreSQL
from .schemas import SMSVerificationPostgreSQL

def insert_sms_verification_data(session: Session, phone_number: str, verification_code: str, status: str):
    new_sms_verification = SMSVerificationPostgreSQL(phone_number=phone_number, verification_code=verification_code, status=status, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
    session.add(new_sms_verification)
    session.flush()
    
    sms_verification_id = new_sms_verification.id
    
    session.commit()
    return sms_verification_id

## Update

### Email - dont change created_at value

def update_email_verification_status(session: Session, id: int, status: str):
    email_verification = session.query(EmailVerificationPostgreSQL).filter_by(id=id).first()
    if email_verification:
        email_verification.status = status
        email_verification.updated_at = datetime.datetime.now()
        
        session.commit()


def update_email_verification_link(session: Session, id: int, verification_link: str):
    email_verification = session.query(EmailVerificationPostgreSQL).filter_by(id=id).first()
    if email_verification:
        email_verification.verification_link = verification_link
        email_verification.updated_at = datetime.datetime.now()
        
        session.commit()


### SMS

from .schemas import SMSVerificationPostgreSQL


def update_sms_verification_phone_number(session: Session, id: int, phone_number: str):
    sms_verification = session.query(SMSVerificationPostgreSQL).filter_by(id=id).first()
    if sms_verification:
        sms_verification.phone_number = phone_number
        sms_verification.updated_at = datetime.datetime.now()
        
        session.commit()


from .schemas import SMSVerificationPostgreSQL


def update_sms_verification_verification_code(session: Session, id: int, verification_code: str):
    sms_verification = session.query(SMSVerificationPostgreSQL).filter_by(id=id).first()
    if sms_verification:
        sms_verification.verification_code = verification_code
        sms_verification.updated_at = datetime.datetime.now()
        
        session.commit()


from .schemas import SMSVerificationPostgreSQL


def update_sms_verification_status(session: Session, id: int, status: str):
    sms_verification = session.query(SMSVerificationPostgreSQL).filter_by(id=id).first()
    if sms_verification:
        sms_verification.status = status
        sms_verification.updated_at = datetime.datetime.now()
        
        session.commit()
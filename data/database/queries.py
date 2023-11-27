# database operations for email and sms verification
from .main import session
from sqlalchemy import text
import datetime

# Account information
# (account_id, generated_data_id, verification_data_id)
def generate_account_information_id():
    query = text("""
    INSERT INTO account_information (generated_data_id, verification_data_id)
    VALUES (DEFAULT, DEFAULT)
    RETURNING account_id
    """)

    # execute query using plain string
    account_information_id = session.execute(query).scalar()

    session.commit()
    session.close()

    # return id
    return account_information_id


# Generated data

## Insert
def insert_generated_data(first_name, last_name, birthdate, company_name, occupation, phone, street_name, street_number, zip_code, city, email, password, user_agent):

    query = text("""
    INSERT INTO generated_data (first_name, last_name, birthdate, company_name, occupation, phone, street_name, street_number, zip_code, city, email, password, user_agent)
    VALUES (:first_name, :last_name, :birthdate, :company_name, :occupation, :phone, :street_name, :street_number, :zip_code, :city, :email, :password, :user_agent)
    RETURNING id
    """)

    # execute query using plain string
    generated_data_id = session.execute(query, {
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'company_name': company_name,
        'occupation': occupation,
        'phone': phone,
        'street_name': street_name,
        'street_number': street_number,
        'zip_code': zip_code,
        'city': city,
        'email': email,
        'password': password,
        'user_agent': user_agent
    }).scalar()

    session.commit()
    session.close()

    # return id
    return generated_data_id

## insert generated_data_id into account_information table
def generated_data_id_as_foreign_key(generated_data_id):
    query = text("""
    INSERT INTO account_information (generated_data_id)
    VALUES (:generated_data_id)
    RETURNING account_id
    """)

    # execute query using plain string
    account_information_id = session.execute(query, {
        'generated_data_id': generated_data_id
    }).scalar()

    session.commit()
    session.close()

    # return id
    return account_information_id

# Verification data

## Insert
    
def insert_email_verification_data(email, verification_link, status, created_at, updated_at):

    query = text("""
    INSERT INTO email_verification (email, verification_link, status, created_at, updated_at)
    VALUES (:email, :verification_link, :status, :created_at, :updated_at)
    RETURNING id
    """)

    # execute query using plain string
    email_verification_id = session.execute(query, {
        'email': email,
        'verification_link': verification_link,
        'status': status,
        'created_at': created_at,
        'updated_at': updated_at
    }).scalar()

    session.commit()
    session.close()

    # return id
    return email_verification_id

def insert_sms_verification_data(phone_number, verification_code, status):

    
    # query
    query = text("""
    INSERT INTO sms_verification (phone_number, verification_code, status, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id
    """)
    
    # execute query
    sms_verification_id = session.execute(query, {
        'phone_number': phone_number,
        'verification_code': verification_code,
        'status': status,
        'created_at': datetime.datetime.now(), 
        'updated_at': datetime.datetime.now()
    }).scalar()

    session.commit()
    session.close()

    # return id
    return sms_verification_id

## Update

### Email - dont change created_at value
def update_email_verification_status(id, status):
    
    query = text("""
    UPDATE email_verification
    SET status = :status, updated_at = :updated_at
    WHERE id = :id
    """)

    # execute query using plain string
    session.execute(query, {
        'id': id,
        'status': status,
        'updated_at': datetime.datetime.now()
    })

    session.commit()
    session.close()

def update_email_verification_link(id, verification_link):
        
    query = text("""
    UPDATE email_verification
    SET verification_link = :verification_link, updated_at = :updated_at
    WHERE id = :id
    """)

    # execute query using plain string
    session.execute(query, {
        'id': id,
        'verification_link': verification_link,
        'updated_at': datetime.datetime.now()
    })

    session.commit()
    session.close()


### SMS
def update_sms_verification_phone_number(id, phone_number):
    
    query = text("""
    UPDATE sms_verification
    SET phone_number = :phone_number, updated_at = :updated_at
    WHERE id = :id
    """)

    # execute query using plain string
    session.execute(query, {
        'id': id,
        'phone_number': phone_number,
        'updated_at': datetime.datetime.now()
    })

    session.commit()
    session.close()

def update_sms_verification_verification_code(id, verification_code):
    
    query = text("""
    UPDATE sms_verification
    SET verification_code = :verification_code, updated_at = :updated_at
    WHERE id = :id
    """)

    # execute query using plain string
    session.execute(query, {
        'id': id,
        'verification_code': verification_code,
        'updated_at': datetime.datetime.now()
    })

    session.commit()
    session.close()

def update_sms_verification_status(id, status):
    
    query = text("""
    UPDATE sms_verification
    SET status = :status, updated_at = :updated_at
    WHERE id = :id
    """)

    # execute query using plain string
    session.execute(query, {
        'id': id,
        'status': status,
        'updated_at': datetime.datetime.now()
    })

    session.commit()
    session.close()


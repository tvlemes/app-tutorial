import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tutorial.settings import FIREBASE_ADMIN_CERT


collection_database = 'category'
url_file_connetion = FIREBASE_ADMIN_CERT

# Created conection
def connection_database():
    try:
        cred = credentials.Certificate(FIREBASE_ADMIN_CERT)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        colletion_db = db.collection(collection_database)
        return colletion_db
    except Exception as e:
        print('Ocorreu um erro ao conectar no Firebase: ', e)
        
# Insert data
def insert_data(name, description, tags):
    collection = connection_database()
    try:
        doc_ref = collection.document()
        doc_ref.set({
            'id': doc_ref.id,
            'name': name,
            'description': description,
            'tags': tags
        })
        firebase_admin.delete_app(firebase_admin.get_app())
    except Exception as e:
        return print(f'Ocorreu um erro: {e}')


# Update data
def update_data(value_id, name, description, tags):
    collection = connection_database()
    try:
        doc_ref = collection.document(value_id).update({
            'name': name,
            'description': description,
            'tags': tags,
        })
        firebase_admin.delete_app(firebase_admin.get_app())
    except Exception as e:
        return print(f'Ocorreu um erro: {e}')

# Select all data
def list_all_data():
    collection = connection_database()
    try:
        users_ref = collection
        docs = users_ref.stream()
        firebase_admin.delete_app(firebase_admin.get_app())
        return docs
    except Exception as e:
        return print(f'Ocorreu um erro: {e}')
    
# Select ID data
def select_data(value_id):
    collection = connection_database()
    try:
        doc_ref = collection.document(value_id)
        docs = doc_ref.get().to_dict()
        print(f'{docs}')
        firebase_admin.delete_app(firebase_admin.get_app())
    except Exception as e:
        return print(f'Ocorreu um erro: {e}')

# Delete data
def delete_data(value_id):
    collection = connection_database()
    try:
        collection.document(value_id).delete()
        firebase_admin.delete_app(firebase_admin.get_app())
    except Exception as e:
        return print(f'Ocorreu um erro: {e}')


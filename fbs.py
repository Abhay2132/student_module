import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate("secrets/fb-admin.json")
firebase_admin.initialize_app(cred,{'storageBucket': 'frbas-1.appspot.com'})

file_path = "static/bird.jpg"
bucket = storage.bucket() # storage bucket
blob = bucket.blob("image/bird.jpg")
blob.upload_from_filename(file_path)
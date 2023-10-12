from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def saveImg (file, UPLOAD_FOLDER : str) -> dict:
    if not file :
        return {error : "file is false"}

    print("saving : " ,file.filename)

    if file.filename == '':
        print("error : no file selected")
        return {"error" : 'no file selected'}
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return {"status" : 'file saved'}
    else:
        print("error while saving ", file.filename)
        print(file)
        return {"error": "Error while saving flie "+file.filename}
    
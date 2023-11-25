from flask import Flask,request
from flask_restful import Resource,Api,reqparse,abort
import os
from werkzeug.utils import secure_filename
from initialize_gpt_assistant import create_model
import uuid

app = Flask("PaperAPI")
app.secret_key = "hello"
api=Api(app)

#Just dummy shared data, only works locally haha.
cache = {}

parser =reqparse.RequestParser()
parser.add_argument('question',required=True)

dummy_data= {
    'hello':'world'
}


class PaperChatBot(Resource):
    def get(self,model_id):
        args = parser.parse_args()
        question = args['question']
        print(question,model_id,len(cache))
        print(cache.keys())
        if model_id not in cache:
            return "session expired, pls re-upload file.",400
        model =cache[model_id]
        answer = model(question)
        print(answer)
        return f"answer:{answer}",200

class UploadPaper(Resource):
    def post(self):
        f= request.files['file']
        print(f.filename)
        upload_dir = r'user_uploaded_files'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        path = os.path.join(upload_dir,secure_filename(f.filename))
        f.save(path)
        # After uploading file we need to initialize GPT assistant.
        model = create_model(path)
        model_id = str(uuid.uuid4())
        cache[model_id]=model
        print(cache.keys())
        return f"model_id:{model_id}",200


api.add_resource(PaperChatBot,'/paper_api/paper_chat_bot/v1/<model_id>')
api.add_resource(UploadPaper,'/paper_api/upload_paper/v1')

if __name__=='__main__':
    app.run()
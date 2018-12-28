from flask import jsonify, request
from flask_restful import Resource, Api
from sim_controller.flock_controller.api_docs.doc_gen import write_doc_to_file
from sim_controller.flock_controller.api_docs.doc import doc

# This function should ideally update the doc
def update_doc(doc, updated_vocab):
    # updated_vocab_val = updated_vocab.keys()
    # supported_classes = doc["supportedClass"]
    # for vocab in updated_vocab_val:
    #     for cls in supported_classes:
    #         if cls["@id"].strip("vocab:") == vocab:
    #             cls["@id"] = updated_vocab[vocab]
    # write_doc_to_file(doc)
    return doc

class UpdateDocs(Resource):
    def get(self):
        return jsonify({"response": "success"})

    def post(self):
        updated_vocab = request.get_json(force=True)
        update_doc(doc, updated_vocab)
        # Reload the app 

        return jsonify({"response": "success"})

# Patch the Flask app object to include the demo endpoint
def monkey_patch(_app):
    api = Api()
    api.add_resource(UpdateDocs, '/api/demo/')
    api.init_app(_app)

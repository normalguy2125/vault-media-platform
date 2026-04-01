from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route to get all media items
@app.route('/media', methods=['GET'])
def get_media():
    media_items = [
        {'id': 1, 'title': 'Media Item 1', 'description': 'Description for media item 1'},
        {'id': 2, 'title': 'Media Item 2', 'description': 'Description for media item 2'},
    ]
    return jsonify(media_items)

# Sample route to add a media item
@app.route('/media', methods=['POST'])
def add_media():
    new_media = request.get_json()
    return jsonify(new_media), 201

# Sample route to get a specific media item
@app.route('/media/<int:media_id>', methods=['GET'])
def get_single_media(media_id):
    media_item = {'id': media_id, 'title': f'Media Item {media_id}', 'description': f'Description for media item {media_id}'}
    return jsonify(media_item)

if __name__ == '__main__':
    app.run(debug=True)
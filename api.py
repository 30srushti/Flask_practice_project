from flask import Flask, render_template, jsonify,request
app=Flask(__name__)
#demodatabase
data=[
    {'id':1, 'name':'item1','price':10}, 
    {'id':2, 'name':'item2','price':20}, 
]





@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/items', methods=['GET'])
def  get_items():
    return jsonify, 200

@app.route('/api/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in data if item ['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({'message': 'Item not found'}), 404

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item=request.json
    new_item['id']=len(data)+1
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)
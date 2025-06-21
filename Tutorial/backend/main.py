from flask import request, jsonify
from config import app, db
from models import Contact

@app.route('/contacts', methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({'contacts': json_contacts}), 200

@app.route('/contacts', methods=["POST"])
def create_contact():
    data = request.get_json()
    new_contact = Contact(
        first_name=data['firstName'],
        last_name=data['lastName'],
        email=data['email']
    )
    if not new_contact.first_name or not new_contact.last_name or not new_contact.email:
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 403
    return jsonify(new_contact.to_json()), 201

@app.route('/update_contact/<int:user_id>', methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({'error': 'Contact not found'}), 404
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    db.session.commit()
    return jsonify({"message": "User updated."}), 200

@app.route('/delete_contact/<int:user_id>', methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message:": "user not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()


    return jsonify({"message": "user deleted"}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
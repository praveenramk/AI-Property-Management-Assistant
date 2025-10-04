from flask import Blueprint, jsonify, request

properties_bp = Blueprint('properties', __name__)

# Sample data for properties
properties = [
    {"id": 1, "name": "Property A", "location": "Location A", "price": 1000},
    {"id": 2, "name": "Property B", "location": "Location B", "price": 1500},
]

@properties_bp.route('/properties', methods=['GET'])
def get_properties():
    return jsonify(properties)

@properties_bp.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        return jsonify(property)
    return jsonify({"error": "Property not found"}), 404

@properties_bp.route('/properties', methods=['POST'])
def create_property():
    new_property = request.json
    new_property['id'] = len(properties) + 1
    properties.append(new_property)
    return jsonify(new_property), 201

@properties_bp.route('/properties/<int:property_id>', methods=['PUT'])
def update_property(property_id):
    property = next((p for p in properties if p['id'] == property_id), None)
    if property:
        property.update(request.json)
        return jsonify(property)
    return jsonify({"error": "Property not found"}), 404

@properties_bp.route('/properties/<int:property_id>', methods=['DELETE'])
def delete_property(property_id):
    global properties
    properties = [p for p in properties if p['id'] != property_id]
    return jsonify({"message": "Property deleted"}), 204
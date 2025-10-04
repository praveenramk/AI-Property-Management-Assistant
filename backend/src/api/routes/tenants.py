from flask import Blueprint, request, jsonify
from ..services.tenant_service import TenantService

tenants_bp = Blueprint('tenants', __name__)

@tenants_bp.route('/tenants', methods=['GET'])
def get_tenants():
    tenants = TenantService.get_all_tenants()
    return jsonify(tenants), 200

@tenants_bp.route('/tenants/<int:tenant_id>', methods=['GET'])
def get_tenant(tenant_id):
    tenant = TenantService.get_tenant_by_id(tenant_id)
    if tenant:
        return jsonify(tenant), 200
    return jsonify({'message': 'Tenant not found'}), 404

@tenants_bp.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.json
    tenant = TenantService.create_tenant(data)
    return jsonify(tenant), 201

@tenants_bp.route('/tenants/<int:tenant_id>', methods=['PUT'])
def update_tenant(tenant_id):
    data = request.json
    tenant = TenantService.update_tenant(tenant_id, data)
    if tenant:
        return jsonify(tenant), 200
    return jsonify({'message': 'Tenant not found'}), 404

@tenants_bp.route('/tenants/<int:tenant_id>', methods=['DELETE'])
def delete_tenant(tenant_id):
    success = TenantService.delete_tenant(tenant_id)
    if success:
        return jsonify({'message': 'Tenant deleted'}), 204
    return jsonify({'message': 'Tenant not found'}), 404
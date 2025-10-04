import pytest
from backend.services.tenant_service import TenantService
from backend.models.tenant import Tenant

@pytest.fixture
def tenant_service():
    return TenantService()

def test_create_tenant(tenant_service):
    tenant_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890"
    }
    tenant = tenant_service.create_tenant(tenant_data)
    assert tenant.name == tenant_data["name"]
    assert tenant.email == tenant_data["email"]
    assert tenant.phone == tenant_data["phone"]

def test_get_tenant(tenant_service):
    tenant_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "0987654321"
    }
    tenant = tenant_service.create_tenant(tenant_data)
    retrieved_tenant = tenant_service.get_tenant(tenant.id)
    assert retrieved_tenant.id == tenant.id
    assert retrieved_tenant.name == tenant_data["name"]

def test_update_tenant(tenant_service):
    tenant_data = {
        "name": "Alice Smith",
        "email": "alice.smith@example.com",
        "phone": "5555555555"
    }
    tenant = tenant_service.create_tenant(tenant_data)
    updated_data = {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "phone": "5555555556"
    }
    updated_tenant = tenant_service.update_tenant(tenant.id, updated_data)
    assert updated_tenant.name == updated_data["name"]
    assert updated_tenant.email == updated_data["email"]
    assert updated_tenant.phone == updated_data["phone"]

def test_delete_tenant(tenant_service):
    tenant_data = {
        "name": "Bob Brown",
        "email": "bob.brown@example.com",
        "phone": "4444444444"
    }
    tenant = tenant_service.create_tenant(tenant_data)
    tenant_service.delete_tenant(tenant.id)
    with pytest.raises(ValueError):
        tenant_service.get_tenant(tenant.id)
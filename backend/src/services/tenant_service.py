from typing import List, Dict

class TenantService:
    def __init__(self, tenant_repository):
        self.tenant_repository = tenant_repository

    def create_tenant(self, tenant_data: Dict) -> Dict:
        return self.tenant_repository.create(tenant_data)

    def get_tenant(self, tenant_id: str) -> Dict:
        return self.tenant_repository.get(tenant_id)

    def update_tenant(self, tenant_id: str, tenant_data: Dict) -> Dict:
        return self.tenant_repository.update(tenant_id, tenant_data)

    def delete_tenant(self, tenant_id: str) -> bool:
        return self.tenant_repository.delete(tenant_id)

    def list_tenants(self) -> List[Dict]:
        return self.tenant_repository.list_all()
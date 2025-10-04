from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tenant import Tenant

DATABASE_URL = "sqlite:///./test.db"  # Update with your actual database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TenantRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_tenant(self, tenant_id: int) -> Tenant:
        return self.db.query(Tenant).filter(Tenant.id == tenant_id).first()

    def create_tenant(self, tenant: Tenant) -> Tenant:
        self.db.add(tenant)
        self.db.commit()
        self.db.refresh(tenant)
        return tenant

    def update_tenant(self, tenant: Tenant) -> Tenant:
        existing_tenant = self.get_tenant(tenant.id)
        if existing_tenant:
            for key, value in tenant.__dict__.items():
                setattr(existing_tenant, key, value)
            self.db.commit()
            self.db.refresh(existing_tenant)
            return existing_tenant
        return None

    def delete_tenant(self, tenant_id: int) -> bool:
        tenant = self.get_tenant(tenant_id)
        if tenant:
            self.db.delete(tenant)
            self.db.commit()
            return True
        return False

    def close(self):
        self.db.close()
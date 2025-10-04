class Tenant:
    def __init__(self, tenant_id, name, email, phone, lease_start_date, lease_end_date):
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone = phone
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date

    def __repr__(self):
        return f"<Tenant {self.name} (ID: {self.tenant_id})>"

    def is_active(self):
        from datetime import datetime
        today = datetime.now().date()
        return self.lease_start_date <= today <= self.lease_end_date

    def contact_info(self):
        return f"{self.name} - Email: {self.email}, Phone: {self.phone}"
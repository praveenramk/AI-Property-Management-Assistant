class Property:
    def __init__(self, property_id, address, owner_id, rent, status):
        self.property_id = property_id
        self.address = address
        self.owner_id = owner_id
        self.rent = rent
        self.status = status

    def __repr__(self):
        return f"<Property(property_id={self.property_id}, address='{self.address}', owner_id={self.owner_id}, rent={self.rent}, status='{self.status}')>"

    def update_status(self, new_status):
        self.status = new_status

    def to_dict(self):
        return {
            "property_id": self.property_id,
            "address": self.address,
            "owner_id": self.owner_id,
            "rent": self.rent,
            "status": self.status
        }
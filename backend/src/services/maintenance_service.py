# maintenance_service.py

from datetime import datetime
from typing import List, Dict, Any

class MaintenanceService:
    def __init__(self):
        self.maintenance_requests = []

    def create_request(self, tenant_id: str, property_id: str, description: str) -> Dict[str, Any]:
        request = {
            "id": len(self.maintenance_requests) + 1,
            "tenant_id": tenant_id,
            "property_id": property_id,
            "description": description,
            "status": "pending",
            "created_at": datetime.now()
        }
        self.maintenance_requests.append(request)
        return request

    def get_requests(self) -> List[Dict[str, Any]]:
        return self.maintenance_requests

    def update_request_status(self, request_id: int, status: str) -> bool:
        for request in self.maintenance_requests:
            if request["id"] == request_id:
                request["status"] = status
                return True
        return False

    def get_request_by_id(self, request_id: int) -> Dict[str, Any]:
        for request in self.maintenance_requests:
            if request["id"] == request_id:
                return request
        return {}
import React from 'react';

const TenantList: React.FC = () => {
    const [tenants, setTenants] = React.useState([]);

    React.useEffect(() => {
        // Fetch tenants from the API
        const fetchTenants = async () => {
            const response = await fetch('/api/tenants');
            const data = await response.json();
            setTenants(data);
        };

        fetchTenants();
    }, []);

    return (
        <div>
            <h2>Tenant List</h2>
            <ul>
                {tenants.map(tenant => (
                    <li key={tenant.id}>{tenant.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default TenantList;
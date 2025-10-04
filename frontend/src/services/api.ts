import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const fetchProperties = async () => {
    const response = await apiClient.get('/properties');
    return response.data;
};

export const fetchTenants = async () => {
    const response = await apiClient.get('/tenants');
    return response.data;
};

export const createMaintenanceRequest = async (data) => {
    const response = await apiClient.post('/maintenance', data);
    return response.data;
};

export const authenticateUser = async (credentials) => {
    const response = await apiClient.post('/auth/login', credentials);
    return response.data;
};
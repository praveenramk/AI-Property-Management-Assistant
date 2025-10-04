import axios from 'axios';

const API_URL = 'http://localhost:5000/api/auth';

export const login = async (email: string, password: string) => {
    try {
        const response = await axios.post(`${API_URL}/login`, { email, password });
        return response.data;
    } catch (error) {
        throw new Error('Login failed');
    }
};

export const register = async (userData: { name: string; email: string; password: string }) => {
    try {
        const response = await axios.post(`${API_URL}/register`, userData);
        return response.data;
    } catch (error) {
        throw new Error('Registration failed');
    }
};

export const logout = async () => {
    try {
        await axios.post(`${API_URL}/logout`);
    } catch (error) {
        throw new Error('Logout failed');
    }
};
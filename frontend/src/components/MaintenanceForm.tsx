import React, { useState } from 'react';

const MaintenanceForm = () => {
    const [description, setDescription] = useState('');
    const [priority, setPriority] = useState('low');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here
        console.log('Maintenance Request:', { description, priority });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="description">Description:</label>
                <textarea
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    required
                />
            </div>
            <div>
                <label htmlFor="priority">Priority:</label>
                <select
                    id="priority"
                    value={priority}
                    onChange={(e) => setPriority(e.target.value)}
                >
                    <option value="low">Low</option>
                    <option value="medium">Medium</option>
                    <option value="high">High</option>
                </select>
            </div>
            <button type="submit">Submit Maintenance Request</button>
        </form>
    );
};

export default MaintenanceForm;
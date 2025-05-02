import axios from 'axios';

const API_BASE = 'http://localhost:5000'; // Adjust according to Flask API URL

export const getJobs = () => axios.get(`${API_BASE}/jobs`);
export const addJob = (jobData) => axios.post(`${API_BASE}/jobs/add`, jobData);
export const deleteJob = (id) => axios.delete(`${API_BASE}/jobs/${id}`);
    
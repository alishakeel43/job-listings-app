import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE_URL;

export const getJobs = () => axios.get(`${API_BASE}/jobs`);
export const addJob = (jobData) => axios.post(`${API_BASE}/jobs/add`, jobData);
export const deleteJob = (id) => axios.delete(`${API_BASE}/jobs/${id}`);
    
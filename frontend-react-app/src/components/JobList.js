// src/components/JobList.js
import React, { useEffect, useState } from 'react';
import { getJobs, deleteJob } from '../services/api';
import JobItem from './JobItem';

const JobList = () => {
  const [jobs, setJobs] = useState([]);

  const fetchJobs = async () => {
    const res = await getJobs();
    setJobs(res.data);
  };

  const handleDelete = async (id) => {
    await deleteJob(id);
    fetchJobs();
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Job Listings</h1>
      {jobs.map((job) => (
        <JobItem key={job.id} job={job} onDelete={handleDelete} />
      ))}
    </div>
  );
};

export default JobList;

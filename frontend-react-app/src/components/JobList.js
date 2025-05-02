// src/components/JobList.js
import React, { useEffect, useState } from 'react';
import { getJobs, deleteJob } from '../services/api';
import DataTable from 'react-data-table-component';

const JobList = () => {
  const [jobs, setJobs] = useState([]);

  const fetchJobs = async () => {
    try {
      const res = await getJobs();
      setJobs(res.data);
    } catch (err) {
      console.error('Failed to fetch jobs:', err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteJob(id);
      fetchJobs();
    } catch (err) {
      console.error('Failed to delete job:', err);
    }
  };
  
  useEffect(() => {
    fetchJobs(); // Initial fetch

    const interval = setInterval(() => {
      fetchJobs();
    }, 3000); // 3000 ms = 3 seconds

    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, []);

  const columns = [
    {
      name: 'Job ID',
      selector: (row) => row.id,
      sortable: true,
    },
    {
      name: 'Job Title',
      selector: (row) => row.title,
      sortable: true,
    },
    {
      name: 'Company',
      selector: (row) => row.company,
      wrap: true,
    },
    {
      name: 'Location',
      selector: (row) => row.location,
      sortable: true,
    },
    {
      name: 'Actions',
      cell: (row) => (
        <button
          onClick={() => handleDelete(row.id)}
          className="text-red-600 hover:underline"
        >
          Delete
        </button>
      ),
    },
  ];

  return (
    <div className="mt-6">
      <DataTable
        title="Job Listings"
        columns={columns}
        data={jobs}
        pagination
        highlightOnHover
        striped
      />
    </div>
  );
};

export default JobList;

import React from 'react';

const JobItem = ({ job, onDelete }) => {
  return (
    <div className="border p-4 my-2 rounded shadow">
      <h2 className="text-xl font-bold">{job.title}</h2>
      <p>{job.cmopany}</p>
      <button onClick={() => onDelete(job.id)} className="mt-2 bg-red-500 text-white px-4 py-2 rounded">
        Delete
      </button>
    </div>
  );
};

export default JobItem;
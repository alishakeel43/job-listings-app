// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// import React, { useState } from 'react';
// import AddJob from './components/AddJob';
// import JobList from './components/JobList';

// function App() {
//   const [refresh, setRefresh] = useState(false);

//   const handleJobAdded = () => {
//     setRefresh(!refresh);
//   };

//   return (
//     <div className="max-w-xl mx-auto p-4">
//       <AddJob onJobAdded={handleJobAdded} />
//       <JobList key={refresh} />
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';
import AddJob from './components/AddJob';
import JobList from './components/JobList';

function App() {
  const [refresh, setRefresh] = useState(false);

  const handleJobAdded = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">Job Portal</h1>
      <div className="max-w-5xl mx-auto bg-white shadow-md rounded-lg p-6">
        <AddJob onJobAdded={handleJobAdded} />
        <JobList key={refresh} />
      </div>
    </div>
  );
}

export default App;


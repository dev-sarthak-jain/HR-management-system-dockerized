import React, { useState } from 'react';
import { AiOutlineCloudUpload } from "react-icons/ai";
import Papa from 'papaparse';

function Dashboard() {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [showToast, setShowToast] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    event.stopPropagation();
    setIsDragging(false);
    if (event.dataTransfer.files && event.dataTransfer.files.length > 0) {
      setFile(event.dataTransfer.files[0]);
      event.dataTransfer.clearData();
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    event.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    event.stopPropagation();
    setIsDragging(false);
  };

  const handleClick = () => {
    const fileUpload = document.getElementById('fileupload');
    fileUpload.value = null; // Reset file input
    fileUpload.click();
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file before submitting.');
      return;
    }

    const reader = new FileReader();
    reader.onload = () => {
      Papa.parse(reader.result, {
        header: true,
        skipEmptyLines: true,
        complete: (results) => {
          const jsonData = JSON.stringify(results.data);
          console.log("Sending JSON:", jsonData);
          fetch('http://127.0.0.1:8000/api/employee_create/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: jsonData
          })
          .then(response => {
            if (response.status === 201) {
              setFile(null); // Clear the file state after submission
              setShowToast(true);
              setTimeout(() => setShowToast(false), 3000);
            } else {
              console.error('Failed to submit file:', response.status);
            }
            return response.json();
          })
          .then(data => console.log("Response data:", data))
          .catch(error => console.error('Error:', error));
        }
      });
    };
    reader.readAsText(file);
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <form onSubmit={handleSubmit} className="flex flex-col items-center space-y-4 bg-slate-100 shadow p-6 rounded-lg" onDrop={handleDrop} onDragOver={handleDragOver} onDragLeave={handleDragLeave}>
        <h2 className="text-xl font-bold text-black mb-4">Add New User Data</h2> {/* Heading added here */}
        <div
          className={`transition duration-300 bg-silver-100 ease-in-out border-2 ${isDragging ? 'border-green-500 bg-green-50' : 'border-blue-500 bg-blue-50'} rounded-lg p-4 w-full text-center cursor-pointer`}
          onClick={handleClick}
          >
          <div className="flex flex-col items-center justify-center space-y-2">
            <AiOutlineCloudUpload size={36} className="text-green-500" />
            <p className="font-bold">Drag and drop your files here or click to browse</p>
            <p> Supported files: .CSV </p>
          </div>
          <input type="file" name="fileupload" id="fileupload" onChange={handleFileChange} className="hidden"/>
          {!file && <span className="block text-sm text-gray-600 mt-2">No file selected</span>}
          {file && <span className="block text-sm text-gray-600 mt-2">File selected: {file.name}</span>}
        </div>
        <input type="submit" value="Submit" className="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer"/>
      </form>
      {showToast && (
        <div className="fixed top-4 left-4 bg-green-500 text-white p-4 rounded shadow-lg transition-opacity duration-700 opacity-100">
          <p>File submitted successfully!</p>
        </div>
      )}
    </div>
  );
}

export default Dashboard;

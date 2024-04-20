import React, { useState, useEffect } from 'react';
import 'tailwindcss/tailwind.css';
import { TextField, Button } from '@mui/material';

export default function Page() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [modifiedValue, setModifiedValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSearchClick = () => {
    fetch('/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ keywords: inputValue })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      setMessage(data.message);  // Display the response message
      setModifiedValue(data.modified);  // Set and display the modified value
    })
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="h-screen flex flex-col justify-center items-center px-6 py-12 lg:px-8 bg-black">
      <div className="max-w-lg w-full space-y-4">
        <TextField
          value={inputValue}
          onChange={handleInputChange}
          label="Enter Keywords"
          variant="outlined"
          InputLabelProps={{
            style: { color: '#fff' }, // Label text color
          }}
          InputProps={{
            className: "text-white bg-gray-800", // Input text color
          }}
          className="w-full"
        />
        <Button 
          variant="contained" 
          className="bg-gray-800 hover:bg-gray-700 text-white" 
          onClick={handleSearchClick}
        >
          Search
        </Button>
        {message && <p className="text-white">{message}</p>}  // Ensure message text is white
        {modifiedValue && <p className="text-white">Modified: {modifiedValue}</p>}  // Ensure modified value text is white
      </div>
    </div>
  );
}

import React, { useState, useEffect } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield'; // Changed import statement
import LanguageSelector from '@/components/language-select'; // Import the LanguageSelector component
import Button from '@mui/material/Button';

export default function Page() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/healthchecker')
      .then(response => response.json())
      .then(data => setMessage(data.message));
  }, []);

  return (
    <div className="h-screen flex flex-col justify-center items-center px-6 py-12 lg:px-8 bg-black text-white">
      <div className="max-w-lg w-full">
        <Textfield />
        <Button variant="contained" className="mt-4 bg-gray-800 hover:bg-gray-700 text-white">Search</Button>
      </div>
    </div>
  );
}


import React, { useState, useEffect } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield'; // Changed import statement
import LanguageSelector from '@/components/language-select'; // Import the LanguageSelector component
import DateSelector from '@/components/date-select'; // Import the DateSelector component
import Button from '@mui/material/Button';

export default function Page() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/healthchecker')
      .then(response => response.json())
      .then(data => setMessage(data.message));
  }, []);

  return (
    <div className="h-screen flex flex-col justify-center items-center bg-cover bg-center bg-no-repeat" style={{ backgroundImage: 'url(/images/bg-1.png)' }}>
      <div className="max-w-3xl w-full">
        <div className="flex flex-col md:flex-row md:space-x-4">
          <div className="w-full md:w-5/9">
            <Textfield />
          </div>
          <div className="w-full md:w-4/9">
            <div className="w-full mb-4">
              <LanguageSelector />
            </div>
            <div className="w-full">
              <DateSelector />
            </div>
          </div>
        </div>
        <Button variant="contained" className="mt-4 bg-gray-800 hover:bg-gray-700 text-white">Search</Button>
      </div>
    </div>
  );
}

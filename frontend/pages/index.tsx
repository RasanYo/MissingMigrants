import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield';
import LanguageSelector from '@/components/language-select';
import DateSelector from '@/components/date-select';
import Button from '@mui/material/Button';
import Progress from '@/components/progress';

export default function Page() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [modifiedValue, setModifiedValue] = useState('');
  const [language, setLanguage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  const handleSearchClick = () => {
    console.log('data');
    fetch('/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        keywords: inputValue,
        language: language,
        startDate: startDate,
        endDate: endDate
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      setMessage(data.message);
      setModifiedValue(data.modified);
    })
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="h-screen bg-cover bg-center bg-no-repeat" style={{ backgroundImage: 'url(/images/bg-1.png)' }}>
      <div className="flex flex-col justify-center items-center ">
          <div className="max-w-3xl w-full">
            <Progress className="h-1/6"/>
            <div className="h-5/6 flex flex-col md:flex-row md:space-x-4">
              <div className="w-full md:w-5/9">
                <Textfield value={inputValue} onChange={handleInputChange}/>
              </div>
              <div className="w-full md:w-4/9">
                <div className="w-full mb-4">
                  <LanguageSelector value={language} onChange={handleLanguageChange}/>
                </div>
                <div className="w-full">
                  <DateSelector
                    startValue={startDate}
                    onChangeStartValue={setStartDate}
                    endValue={endDate}
                    onChangeEndValue={setEndDate}
                  />
                </div>
              </div>
            </div>
            <Button variant="contained" className="mt-4 bg-gray-800 hover:bg-gray-700 text-white opacity-90" onClick={handleSearchClick}>Search</Button>
            {message && <p className="text-dark">{message}</p>}
            {modifiedValue && <p className="text-dark">Modified: {modifiedValue}</p>}
          </div>
      </div>
    </div>
  );
}
import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield';
import LanguageSelector from '@/components/language-select';
import DateSelector from '@/components/date-select';
import Button from '@mui/material/Button';
import Progress from '@/components/progress';
import ListContainer from '@/components/list-container'

export default function Page() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [modifiedValue, setModifiedValue] = useState('');
  const [language, setLanguage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [items, setItems] = useState('');
  const [buttonClicked, setButtonClicked] = useState(false); // State to track button click
  const [progressState, setProgressState] = useState('0'); // Initialize progress state

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  const handleSearchClick = () => {
    console.log('data');
    setButtonClicked(true); // Set button clicked to true
    setProgressState('1'); // Set progress state to 1

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
      setProgressState('2');
      setItems([{
              'id' : '2'
      }]);

    })
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="h-screen bg-cover bg-center bg-no-repeat" style={{ backgroundImage: 'url(/images/bg-1.png)' }}>
      <div className="flex flex-col justify-center items-center ">
          <div className="max-w-3xl w-full">
            <Progress state={progressState} />
            <div className="flex flex-col md:flex-row md:space-x-4">
              <div className="w-full md:w-5/9">
                <Textfield value={inputValue} onChange={handleInputChange} disabled={buttonClicked} />
              </div>
              <div className="w-full md:w-4/9">
                <div className="w-full mb-4">
                  <LanguageSelector value={language} onChange={handleLanguageChange} disabled={buttonClicked} />
                </div>
                <div className="w-full">
                  <DateSelector
                    startValue={startDate}
                    onChangeStartValue={setStartDate}
                    endValue={endDate}
                    onChangeEndValue={setEndDate}
                    disabled={buttonClicked}
                  />
                </div>
              </div>
            </div>
            {!buttonClicked && ( // Render button only if it's not clicked
              <Button variant="contained" className="mt-4 bg-gray-800 hover:bg-gray-700 text-white opacity-90" onClick={handleSearchClick}>Search</Button>
            )}
            {message && <p className="text-dark">{message}</p>}
            {modifiedValue && <p className="text-dark">Modified: {modifiedValue}</p>}

            <div>
                <ListContainer
                    items={items}
                    searchPressed={buttonClicked}
                />
            </div>
          </div>
      </div>
    </div>
  );
}
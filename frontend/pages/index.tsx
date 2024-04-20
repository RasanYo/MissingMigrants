import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield';
import LanguageSelector from '@/components/language-select';
import DateSelector from '@/components/date-select';
import Button from '@mui/material/Button';
import Progress from '@/components/progress';
import ListContainer from '@/components/list-container'
import CircularProgress from '@mui/material/CircularProgress'; // Import CircularProgress

export default function Page() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [modifiedValue, setModifiedValue] = useState('');
  const [language, setLanguage] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [opacity, setOpacity] = useState('0.9');
  const [items, setItems] = useState('');
  const [buttonClicked, setButtonClicked] = useState(false); // State to track button click
  const [progressState, setProgressState] = useState('0'); // Initialize progress state
  const [loading, setLoading] = useState(false); // State to track loading state


  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleLanguageChange = (event) => {
    setLanguage(event.target.value);
  };

  const transformData = (data) => {
    const transformedItems = [];
    Object.keys(data).forEach(language => {
      Object.keys(data[language]).forEach(category => {
        data[language][category].forEach(item => {
          transformedItems.push({
            title: item.title,
            description: item.description,
            publishedDate: item['published date'],
            url: item.url,
            language,
            publisher: {
              href: item.publisher.href,
              title: item.publisher.title
            },
            article: {
              title: item.article.title,
              text: item.article.text
            }
          });
        });
      });
    });
    return transformedItems;
  };


  const handleSearchClick = () => {
    console.log('data');
    setProgressState('1'); // Set progress state to 1
    setOpacity('0.6');
    setLoading(true); // Set loading to true

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
      setButtonClicked(true); // Set button clicked to true
      setProgressState('2');
      setItems([{
              'id' : '2'
      }]);
      setLoading(false); // Set loading to false
    })
   .catch((error) => {
     console.error('Error:', error);
     setLoading(false); // Set loading to false even in case of error
   });
  };

  return (
    <div className="h-screen bg-cover bg-center bg-no-repeat" style={{ backgroundImage: 'url(/images/bg-1.png)' }}>
      <div className="flex flex-col justify-center items-center ">
          <div className="max-w-3xl w-full">
            <Progress state={progressState} />
            <div className="flex flex-col md:flex-row md:space-x-4">
              <div className="w-full md:w-5/9">
                <Textfield value={inputValue} onChange={handleInputChange} disabled={buttonClicked} opacity={opacity}/>
              </div>
              <div className="w-full md:w-4/9">
                <div className="w-full mb-4">
                  <LanguageSelector value={language} onChange={handleLanguageChange} disabled={buttonClicked} opacity={opacity}/>
                </div>
                <div className="w-full">
                  <DateSelector
                    startValue={startDate}
                    onChangeStartValue={setStartDate}
                    endValue={endDate}
                    onChangeEndValue={setEndDate}
                    disabled={buttonClicked}
                    opacity={opacity}
                  />
                </div>
              </div>
            </div>
            {!buttonClicked && (
              loading ? ( // Render loading indicator if loading is true
                <div className="p-3 mt-4 bg-gray-800 text-white opacity-90 inline-block rounded-2xl">
                    <CircularProgress size={12} />
                </div>
              ) : (
                // Render button only if it's not clicked and not loading
                <Button variant="contained" className="mt-4 bg-gray-800 hover:bg-gray-700 text-white opacity-90" onClick={handleSearchClick} disabled={buttonClicked || loading}>
                  Search
                </Button>
              )
            )}
            <div className="mt-5">
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
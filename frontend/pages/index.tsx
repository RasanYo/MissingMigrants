import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';
import Textfield from '@/components/textfield';
import LanguageSelector from '@/components/language-select';
import DateSelector from '@/components/date-select';
import Button from '@mui/material/Button';
import Progress from '@/components/progress';
import ListContainer from '@/components/list-container'
import CircularProgress from '@mui/material/CircularProgress'; // Import CircularProgress
import Head from 'next/head'
import { TextField } from '@mui/material';
import { set } from 'react-hook-form';


export default function Page() {
  const [message, setMessage] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [openAIkeyInput, setOpenAIkeyInput] = useState(''); // State to store OpenAI key input
  const [modifiedValue, setModifiedValue] = useState('');
  const [language, setLanguage] = useState<string[]>([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [opacity, setOpacity] = useState('0.9');
  const [items, setItems] = useState([]);
  const [buttonClicked, setButtonClicked] = useState(false); // State to track button click
  const [progressState, setProgressState] = useState('0'); // Initialize progress state
  const [loading, setLoading] = useState(false); // State to track loading state
  const [warning, setWarning] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleOpenAIKeyChange = (event) => {
    setOpenAIkeyInput(event.target.value);
  }

  const handleLanguageChange = (event) => {
    const value = event.target.value;
    setLanguage(typeof value === 'string' ? value.split(',') : value);
  };

  const transformDataToItems = (data) => {
    let items = [];  // This will hold arrays of items from each category.

    for (let category in data) {
      let categoryItems = [];  // Array to store items for the current category.

      for (let article in data[category]) {
        let item = data[category][article];  // Reference the article item directly.

        categoryItems.push({  // Push each item object into the current category's array.
          title: item.title,
          description: item.description,
          publishedDate: item["published date"],  // Make sure keys match JSON structure.
          url: item.url,
          publisher: {
            href: item.publisher.href,
            title: item.publisher.title
          },
          article: {
            title: item.article.title,
            text: item.article.text
          },
          country: item.vector["Country of Incident"],
          deads:item.vector["Number of Dead"],
          missing: item.vector["Minimum Estimated Number of Missing"],
          cause_death: item.vector["Cause of Death"],
          country_origin: item.vector["Country of Origin"]
        });
      }

      items.push(categoryItems);  // Add the current category's items array to the main items array.
    }

    return items;
  };

  const handleSearchClick = () => {
    setProgressState('1'); // Set progress state to 1
    setOpacity('0.6');
    setLoading(true); // Set loading to true
    setProgressState('1');
    setWarning(''); // Clear any previous warning messages
    console.log('keywords', inputValue)
    console.log('language', language)
    console.log('startDate', startDate)
    console.log('endDate', endDate)
    console.log('openAIkey', openAIkeyInput)


    fetch('/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        keywords: inputValue,
        language: language,
        startDate: startDate,
        endDate: endDate,
        openAIkey: openAIkeyInput
      })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setProgressState('2');
      setButtonClicked(true); // Set button clicked to true
      setItems(transformDataToItems(data));
      setLoading(false); // Set loading to false
      setProgressState('3');
    })
    .catch((error) => {
      console.error('Error:', error);
      setProgressState('0');
      setLoading(false); // Set loading to false even in case of error
      setOpacity('0.9');
      setWarning(`There was an error: ${error.message}`);
    });
  };

  return (
    <div>
      <Head>
        <link rel="icon" href="/images/logo.ico" />
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet" />
      </Head>
      <div className="min-h-screen bg-cover bg-center bg-no-repeat" style={{ backgroundImage: 'url(/images/bg-1.png)' }}>
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
            <div className="w-full md:w-2/9 pt-4">
              <TextField
                required
                fullWidth
                id="outlined-required"
                label="OpenAI Key"
                multiline
                rows={1}
                placeholder="Your Open AI key here"
                variant="outlined"
                value={openAIkeyInput}
                onChange={handleOpenAIKeyChange}
                disabled={buttonClicked} // Pass the disabled prop to TextField
                sx={{
                  '& .MuiTextField-root': {
                    width: '100%',
                    backgroundColor: `rgba(31, 41, 55, ${opacity})`, // Use template literal for dynamic opacity
                    color: '#fff',
                    borderRadius: 2
                  },
                  '& .MuiFilledInput-underline:before': { borderBottom: 'none' },
                  '& .MuiFilledInput-input': { padding: '14px 18px', color: '#fff' },
                  '& .MuiFormLabel-root': {
                    color: buttonClicked ? 'rgb(31 41 55)' : '#fff' // Adjust label color based on disabled prop
                  }
                }}
              />
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
            <div className="my-5">
              <ListContainer
                items={items}
                searchPressed={buttonClicked}
              />
            </div>
            <div className="my-5">
              <p className="text-center text-red-500">{warning}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

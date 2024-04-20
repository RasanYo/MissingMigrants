import * as React from 'react';
import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material';
import { languages } from './languages'; // Import the languages array

const LanguageSelector = () => {
  const [language, setLanguage] = React.useState('');

  const handleChange = (event) => {
    setLanguage(event.target.value);
  };

  return (
    <Box>
      <FormControl fullWidth>
        <InputLabel id="language-label" style={{ color: '#fff' }}>Select Language</InputLabel>
        <Select
          labelId="language-label"
          id="language-select"
          value={language}
          label="Select Language"
          onChange={handleChange}
          style={{ backgroundColor: '#1f2937', color: '#fff' }} // Adjust background and text color
          MenuProps={{
            PaperProps: {
              style: {
                backgroundColor: '#374151', // Background color of the dropdown list
              },
            },
            MenuListProps: {
              style: {
                '&::-webkit-scrollbar': {
                  width: '0.5em', // Width of the scrollbar
                },
                '&::-webkit-scrollbar-thumb': {
                  backgroundColor: '#1f2937', // Color of the scrollbar thumb
                },
              },
            },
          }}
        >
          {languages.map((lang) => (
            <MenuItem key={lang.value} value={lang.value} style={{ backgroundColor: '#374151', color: '#fff' }}>
              {lang.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}

export default LanguageSelector;

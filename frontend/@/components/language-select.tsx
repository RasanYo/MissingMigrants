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
      <FormControl>
        <InputLabel id="language-label" style={{ color: '#fff' }}>Select Language</InputLabel>
        <Select
          labelId="language-label"
          id="language-select"
          value={language}
          label="Select Language"
          onChange={handleChange}
          sx={{
            '& .MuiSelect-icon': { color: '#fff' }, // Set color of the select icon
            '& .MuiListItem-root': { color: '#1f2937' }, // Set color of the list items
            '& .MuiList-root': { backgroundColor: '#1f2937' }, // Set background color of the dropdown menu
          }}
        >
          {languages.map((lang) => (
            <MenuItem key={lang.value} value={lang.value}>
              {lang.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}

export default LanguageSelector;

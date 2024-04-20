import * as React from 'react';
import { Box, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent } from '@mui/material';
import { languages } from './languages'; // Import the languages array

interface LanguageSelectorProps {
  value: string; // Current value for the select
  onChange: (event: SelectChangeEvent) => void; // Function to call on value change
}

class LanguageSelector extends React.Component<LanguageSelectorProps> {
  render() {
    const { value, onChange } = this.props;

    return (
      <Box>
        <FormControl fullWidth>
          <InputLabel id="language-label" style={{ color: '#fff' }}>Select Language</InputLabel>
          <Select
            labelId="language-label"
            id="language-select"
            value={value}
            onChange={onChange}
            label="Select Language"
            style={{ backgroundColor: '#1f2937', color: '#fff' }}
            MenuProps={{
              PaperProps: {
                style: {
                  backgroundColor: '#374151',
                },
              },
              MenuListProps: {
                style: {
                  '&::-webkit-scrollbar': {
                    width: '0.5em',
                  },
                  '&::-webkit-scrollbar-thumb': {
                    backgroundColor: '#1f2937',
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
}

export default LanguageSelector;

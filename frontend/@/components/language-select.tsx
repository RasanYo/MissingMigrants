import * as React from 'react';
import { Box, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent } from '@mui/material';
import { languages } from './languages'; // Import the languages array

interface LanguageSelectorProps {
  value: string; // Current value for the select
  onChange: (event: SelectChangeEvent) => void; // Function to call on value change
  opacity: number; // Add opacity prop
  disabled?: boolean; // Add disabled prop
}

class LanguageSelector extends React.Component<LanguageSelectorProps> {
  render() {
    const { value, onChange, opacity, disabled, ...otherProps } = this.props;
    const labelColor = disabled ? 'rgb(31 41 55)' : '#fff'; // Adjust label color based on disabled prop

    return (
      <Box>
        <FormControl fullWidth>
          <InputLabel id="language-label" style={{ color: labelColor }}>Select Language</InputLabel>
          <Select
            labelId="language-label"
            id="language-select"
            value={value}
            onChange={onChange}
            label="Select Language"
            style={{ backgroundColor: `rgba(31, 41, 55, ${opacity})`, color: '#fff' }} // Use template literal for dynamic opacity
            {...otherProps}
            disabled={disabled} // Pass disabled prop to Select component
            MenuProps={{
              PaperProps: {
                style: {
                  backgroundColor: '#374151',
                },
              },
              MenuListProps: {
                style: {
                  '::WebkitScrollbarThumb': {
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

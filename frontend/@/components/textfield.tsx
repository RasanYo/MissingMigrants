import * as React from 'react';
import { Box, TextField } from '@mui/material';

interface TextfieldProps extends React.ComponentPropsWithoutRef<typeof TextField> {
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  opacity: number;
  disabled?: boolean; // Add disabled prop
}

const Textfield: React.FC<TextfieldProps> = ({ value, onChange, opacity, disabled, ...otherProps }) => {
  return (
    <Box
      component="form"
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
          color: disabled ? 'rgb(31 41 55)' : '#fff' // Adjust label color based on disabled prop
        }
      }}
      noValidate
      autoComplete="on"
      {...otherProps}
    >
      <div>
        <TextField
          fullWidth
          id="filled-multiline-static"
          label="Keywords"
          multiline
          rows={3}
          placeholder="Give in the keywords you want to search on"
          variant="filled"
          value={value}
          onChange={onChange}
          disabled={disabled} // Pass the disabled prop to TextField
          {...otherProps}
        />
      </div>
    </Box>
  );
}

export default Textfield;

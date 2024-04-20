import * as React from 'react';
import { Box, TextField } from '@mui/material';

interface TextfieldProps extends React.ComponentPropsWithoutRef<typeof TextField> {
  // Explicitly declare the types for value and onChange to override any from TextField if needed
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  opacity: number; // Add opacity prop
}

const Textfield: React.FC<TextfieldProps> = ({ value, onChange, opacity, ...otherProps }) => {
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
        '& .MuiFormLabel-root': { color: '#fff' }
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
          {...otherProps}
        />
      </div>
    </Box>
  );
}

export default Textfield;

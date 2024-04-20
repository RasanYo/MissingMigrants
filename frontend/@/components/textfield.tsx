import * as React from 'react';
import { Box, TextField } from '@mui/material';

interface TextfieldProps extends React.ComponentPropsWithoutRef<typeof TextField> {
  // Explicitly declare the types for value and onChange to override any from TextField if needed
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

const Textfield: React.FC<TextfieldProps> = ({ value, onChange, ...otherProps }) => {
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { width: '100%', backgroundColor: 'rgba(31, 41, 55, 0.9)', color: '#fff', borderRadius: 2}, // Set width to 100% and adjust colors
        '& .MuiFilledInput-underline:before': { borderBottom: 'none' }, // Remove underline
        '& .MuiFilledInput-input': { padding: '14px 18px', color: '#fff' }, // Adjust input padding and set text color to white
        '& .MuiFormLabel-root': { color: '#fff' } // Set label color to white
      }}
      noValidate
      autoComplete="on"
      {...otherProps} // Spread additional props to the Box component
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
          {...otherProps} // Spread otherProps to the TextField if needed
        />
      </div>
    </Box>
  );
}

export default Textfield;

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
        '& .MuiTextField-root': { width: '100%', backgroundColor: '#1f2937', color: '#fff', borderRadius: 2},
        '& .MuiFilledInput-underline:before': { borderBottom: 'none' },
        '& .MuiFilledInput-input': { padding: '14px 18px', color: '#fff' },
        '& .MuiFormLabel-root': { color: '#fff' }
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
          rows={4}
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

import * as React from 'react';
import { Box, TextField } from '@mui/material';

const Textfield = () => {
  return (
    <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { width: '100%', backgroundColor: '#1f2937', color: '#fff', borderRadius: 2}, // Set width to 100% and adjust colors
        '& .MuiFilledInput-underline:before': { borderBottom: 'none' }, // Remove underline
        '& .MuiFilledInput-input': { padding: '14px 18px', color: '#fff' }, // Adjust input padding and set text color to white
        '& .MuiFormLabel-root': { color: '#fff' } // Set label color to white
      }}
      noValidate
      autoComplete="on"
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
        />
      </div>
    </Box>
  );
}

export default Textfield;

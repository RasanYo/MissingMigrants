import React from 'react';
import { TextField } from '@mui/material';

const DateSelector = ({
  startValue,
  onChangeStartValue,
  endValue,
  onChangeEndValue
}) => {
  return (
    <div>
      <TextField
        id="start-date"
        label="Select Start Date"
        type="date"
        value={startValue}  // Use startValue passed from the parent
        onChange={(e) => onChangeStartValue(e.target.value)}  // Use onChangeStartValue passed from the parent
        InputProps={{
          style: {
            backgroundColor: '#1f2937',
            color: '#fff',
            borderRadius: '8px',
            marginRight: '10px', // Margin to the right
          },
        }}
        InputLabelProps={{
          style: {
            color: '#fff',
          },
          shrink: true,
        }}
      />
      <TextField
        id="end-date"
        label="Select End Date"
        type="date"
        value={endValue}  // Use endValue passed from the parent
        onChange={(e) => onChangeEndValue(e.target.value)}  // Use onChangeEndValue passed from the parent
        InputProps={{
          style: {
            backgroundColor: '#1f2937',
            color: '#fff',
            borderRadius: '8px',
            textAlign: 'right',
            marginLeft: '10px', // Margin to the left
          },
        }}
        InputLabelProps={{
          style: {
            color: '#fff',
          },
          shrink: true,
        }}
      />
    </div>
  );
};

export default DateSelector;

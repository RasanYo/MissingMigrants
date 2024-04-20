import React from 'react';
import { TextField } from '@mui/material';

const DateSelector = ({
  startValue,
  onChangeStartValue,
  endValue,
  onChangeEndValue,
  opacity,
  ...otherProps
}) => {
    const inputStyle = {
      backgroundColor: `rgba(31, 41, 55, ${opacity})`, // Use template literals for dynamic opacity
      color: '#fff',
      borderRadius: '8px',
      marginRight: '10px',
    };

  return (
    <div>
      <TextField
        id="start-date"
        label="Select Start Date"
        type="date"
        value={startValue}
        onChange={(e) => onChangeStartValue(e.target.value)}
        InputProps={{
          style: inputStyle,
        }}
        {...otherProps}
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
        value={endValue}
        onChange={(e) => onChangeEndValue(e.target.value)}
        InputProps={{
          style: {
            ...inputStyle,
            textAlign: 'right',
            marginLeft: '10px',
          },
        }}
        {...otherProps}
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

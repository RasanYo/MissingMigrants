import React from 'react';
import { TextField } from '@mui/material';

const DateSelector = ({
  startValue,
  onChangeStartValue,
  endValue,
  onChangeEndValue,
  opacity,
  disabled, // Add disabled prop
  ...otherProps
}) => {
    const inputStyle = {
      backgroundColor: `rgba(31, 41, 55, ${opacity})`, // Use template literals for dynamic opacity
      color: '#fff',
      borderRadius: '8px',
      marginRight: '10px',
    };
    const labelColor = disabled ? 'rgb(31 41 55)' : '#fff'; // Adjust label color based on disabled prop

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
        disabled={disabled}
        {...otherProps}
        InputLabelProps={{
          style: {
            color: labelColor, // Apply label color
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
        disabled={disabled}
        {...otherProps}
        InputLabelProps={{
          style: {
            color: labelColor, // Apply label color
          },
          shrink: true,
        }}
      />
    </div>
  );
};

export default DateSelector;

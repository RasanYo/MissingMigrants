import React, { useState } from 'react';
import { TextField } from '@mui/material';

const DateSelector = () => {
  const [selectedStartDate, setSelectedStartDate] = useState(null);
  const [selectedEndDate, setSelectedEndDate] = useState(null);

  const handleStartDateChange = (date) => {
    setSelectedStartDate(date);
  };

  const handleEndDateChange = (date) => {
    setSelectedEndDate(date);
  };

  return (
    <div>
        <TextField
          id="start-date"
          label="Select Start Date"
          type="date"
          defaultValue={selectedStartDate}
          onChange={(e) => handleStartDateChange(e.target.value)}
          InputProps={{
            style: {
              backgroundColor: '#1f2937',
              color: '#fff',
              borderRadius: '8px',
              marginRight: '10px', // Add margin to the right
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
          defaultValue={selectedEndDate}
          onChange={(e) => handleEndDateChange(e.target.value)}
          InputProps={{
            style: {
              backgroundColor: '#1f2937',
              color: '#fff',
              borderRadius: '8px',
              textAlign: 'right',
              marginLeft: '10px', // Add margin to the left
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

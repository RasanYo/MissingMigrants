import React from 'react';

export default function Progress({
    state
}) {
  const egyptianBlue = '#0035A0ff';

  // Define mapping of percentages and text colors based on state
  const progressMap = {
    '0': { percentage: '10', textColors: [egyptianBlue] },
    '1': { percentage: '35', textColors: [egyptianBlue, egyptianBlue] },
    '2': { percentage: '65', textColors: [egyptianBlue, egyptianBlue, egyptianBlue] },
    '3': { percentage: '100', textColors: [egyptianBlue, egyptianBlue, egyptianBlue, egyptianBlue] },
    default: { percentage: '10', textColors: [egyptianBlue] } // Default percentage and text color
  };

  // Get the progress and text colors based on the state
  const { percentage, textColors } = progressMap[state] || progressMap.default;

  return (
    <div className="mb-10">
      <h4 className="sr-only">Status</h4>
      <div className="mt-6" aria-hidden="true">
        <div className="overflow-hidden rounded-full bg-gray-800">
          <div className="h-2 rounded-full" style={{ backgroundColor: egyptianBlue, width: `${percentage}%` }} />
        </div>
        <div className="mt-2 hidden grid-cols-4 text-sm font-medium sm:grid">
          {textColors.map((color, index) => (
            <div key={index} style={{ color }}>{getTextByIndex(index)}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

// Helper function to get text by index
function getTextByIndex(index) {
  switch (index) {
    case 0:
      return 'Make query';
    case 1:
      return 'Search articles';
    case 2:
      return 'Compare articles';
    case 3:
      return 'Done';
    default:
      return 'Make query';
  }
}

import React from 'react';

export default function Progress() {
  const egyptianBlue = '#0035A0ff';

  return (
    <div className="mb-10">
      <h4 className="sr-only">Status</h4>
      <div className="mt-6" aria-hidden="true">
        <div className="overflow-hidden rounded-full bg-gray-800"> {/* Updated background color */}
          <div className="h-2 rounded-full" style={{ backgroundColor: egyptianBlue, width: '10%' }} /> {/* Updated progress bar color */}
        </div>
        <div className="mt-2 hidden grid-cols-4 text-sm font-medium text-gray-800 sm:grid"> {/* Updated text color */}
          <div style={{ color: egyptianBlue }}>Make query</div> {/* Updated text color */}
          <div className="text-center">Search articles</div> {/* Updated text color */}
          <div className="text-center">Compare articles</div>
          <div className="text-right">Done</div>
        </div>
      </div>
    </div>
  );
}

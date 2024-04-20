import React from 'react';
import AccordionArticle from '@/components/accordion';

export default function ListContainer({ items, searchPressed }) {
  // Return null if search is not pressed or items are not provided
  if (!searchPressed || !items || items.length === 0) {
    return null;
  }

  return (
    <ul role="list" className="space-y-3">
      {items.map((item, index) => {
        // Generate overview for each item
        const overview =
          item.length > 0
            ? item[0].country == null ? `${new Date(item[0].publishedDate).toLocaleDateString()} - Uncertain`:
            `${new Date(item[0].publishedDate).toLocaleDateString()} - ${item[0].country}`
            : "No Data Available";

        return (
          <li key={index} className="overflow-hidden rounded-xl bg-gray-900 px-6 py-4 shadow-md">
            {/* Updated h1 styling */}
            <h1 className="text-white text-lg font-semibold mb-2">{overview}</h1>
            <AccordionArticle articles={item} />
          </li>
        );
      })}
    </ul>
  );
}

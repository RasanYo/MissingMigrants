import React from 'react';
import AccordionArticle from '@/components/accordion';

export default function ListContainer({ items, searchPressed }) {
  // Return null if search is not pressed or items are not provided
  if (!searchPressed || !items || items.length === 0) {
    return null;
  }

  return (
    <ul role="list" className="space-y-3">
      {items.map((item) => (
        <li key={item.id} className="overflow-hidden rounded-xl bg-gray-900 px-6 py-4 shadow-md">
          <AccordionArticle
            item={item}
          />
        </li>
      ))}
    </ul>
  );
}
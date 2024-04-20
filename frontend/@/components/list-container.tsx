import React from 'react';
import Link from 'next/link';  // Import Link from Next.js for navigation

export default function ListContainer({ items, searchPressed }) {
  // Return null if search is not pressed or items are not provided
  if (!searchPressed || !items || items.length === 0) {
    return null;
  }

  return (
    <div className="space-y-3">
      {items.map((item, index) => (
        <div key={index} className="overflow-hidden rounded-md bg-white p-4 shadow-sm">
          <h3 className="text-lg font-semibold">{item.title}</h3>
          <p className="text-gray-600">{item.description}</p>
          <Link href={item.url} passHref>
            <a target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
              Read more
            </a>
          </Link>
          {item.publisher && (
            <div className="text-sm text-gray-500 mt-2">
              <a href={item.publisher.href} target="_blank" rel="noopener noreferrer" className="hover:underline">
                Source: {item.publisher.title}
              </a>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

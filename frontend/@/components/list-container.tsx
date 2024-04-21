import React, { useState, useRef, useEffect } from 'react';
import AccordionArticle from '@/components/accordion';
import InfoIcon from '@mui/icons-material/Info'; // Import the Info icon from Material-UI
import LocationOnIcon from '@mui/icons-material/LocationOn';
import WhatshotIcon from '@mui/icons-material/Whatshot'; // Import the Whatshot icon as an alternative to a skull
import ReportIcon from '@mui/icons-material/Report';
import MedicalServicesIcon from '@mui/icons-material/MedicalServices';
import PublicIcon from '@mui/icons-material/Public';

export default function ListContainer({ items, searchPressed }) {
  // State to control the visibility of the popup
  const [isPopupOpen, setPopupOpen] = useState(false);
  // State to store the currently selected item
  const [articles, setArticles] = useState(null);

  // Function to open the popup
  const openPopup = (item) => {
    setArticles(item);
    setPopupOpen(true);
  };

  // Function to close the popup
  const closePopup = () => {
    setArticles(null);
    setPopupOpen(false);
  };

  // Reference to the popup div
  const popupRef = useRef(null);

  // Event listener to close popup when clicking outside of it
  useEffect(() => {
    function handleClickOutside(event) {
      if (popupRef.current && !popupRef.current.contains(event.target)) {
        closePopup();
      }
    }
    // Bind the event listener
    document.addEventListener("mousedown", handleClickOutside);
    // Unbind the event listener on cleanup
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [popupRef]);

  // Return null if search is not pressed or items are not provided
  if (!searchPressed || !items || items.length === 0) {
    return null;
  }

  return (
    <>
      {/* Check if the popup should be displayed */}
      {isPopupOpen && articles && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
          <div ref={popupRef} className="bg-gray-800 p-8 rounded-xl shadow-lg w-1/2">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-semibold text-white flex items-center">
                <span>Incident Details</span>
                <InfoIcon style={{ color: 'white', marginLeft: '0.5rem', cursor: 'pointer' }} onClick={closePopup} />
              </h2>
            </div>
            <table className="table-auto text-sm text-gray-300 w-full">
              <thead>
                <tr>
                  <th className="w-1/5 text-left py-2"><LocationOnIcon /> Region</th>
                  <th className="w-1/5 text-left py-2"><WhatshotIcon /> Dead</th>
                  <th className="w-1/5 text-left py-2"><ReportIcon /> Missing</th>
                  <th className="w-1/5 text-left py-2"><MedicalServicesIcon /> Cause of Death</th>
                  <th className="w-1/5 text-left py-2 px-4"><PublicIcon /> Origin</th>
                </tr>
              </thead>
              <tbody>
                {articles.map((article, index) => (
                  <tr key={index}>
                    <td className="w-1/5 py-2 px-8">{article.country || 'N/A'}</td>
                    <td className="w-1/5 py-2 px-8">{article.deads || 'N/A'}</td>
                    <td className="w-1/5 py-2 px-8">{article.missing || 'N/A'}</td>
                    <td className="w-1/5 py-2 px-8">{article.cause_death || 'N/A'}</td>
                    <td className="w-1/5 py-2 px-12">{article.country_origin || 'N/A'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
            <button className="mt-6 px-3 py-1 text-sm font-medium text-gray-900 bg-gray-200 rounded-xl shadow-sm hover:bg-gray-300" onClick={closePopup}>
              Close
            </button>
          </div>
        </div>
      )}

      <ul role="list" className="space-y-3">
        {items.map((item, index) => {
          // Generate overview for each item
          const overview = item.length > 0
            ? (item[0].country === null ? `${new Date(item[0].publishedDate).toLocaleDateString()} - <Uncertain>` : `${new Date(item[0].publishedDate).toLocaleDateString()} - ${item[0].country}`)
            : "No Data Available";

          return (
            <li key={index} className="overflow-hidden rounded-xl bg-gray-900 px-6 py-4 shadow-md">
              <div className="flex items-center justify-between">
                <h1 className="text-white text-lg font-semibold mb-2">{overview}</h1>
                {/* Add onClick event to open the popup */}
                <InfoIcon style={{ color: 'white', cursor: 'pointer' }} onClick={() => openPopup(item)} />
              </div>
              <AccordionArticle articles={item} />
            </li>
          );
        })}
      </ul>
    </>
  );
}

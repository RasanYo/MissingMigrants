import React, { useState } from 'react';

const Article = ({ article }) => {
  return (
    <div className="mb-4">
      <h3>{article.title}</h3>
      <p>{article.description}</p>
      <a href={article.url} target="_blank" rel="noopener noreferrer">Read more</a>
    </div>
  );
};

const ArticlesList = ({ articles, language }) => {
  return (
    <div>
      <h2>Articles in {language}</h2>
      {articles.map((article, index) => (
        <Article key={index} article={article} />
      ))}
    </div>
  );
};


const LanguageArticles = ({ data }) => {
    const [selectedLanguage, setSelectedLanguage] = useState('english');
  
    const handleLanguageChange = (event) => {
      setSelectedLanguage(event.target.value);
    };
  
    return (
      <div>
        <select value={selectedLanguage} onChange={handleLanguageChange}>
          {Object.keys(data).map((lang) => (
            <option key={lang} value={lang}>{lang}</option>
          ))}
        </select>
        <div>
          {Object.entries(data[selectedLanguage]).map(([category, articles], index) => (
            <ArticlesList key={index} articles={articles} language={category} />
          ))}
        </div>
      </div>
    );
  };
  
  export default LanguageArticles;
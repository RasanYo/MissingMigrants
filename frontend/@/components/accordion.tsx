import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

export default function AccordionArticle({ articles }) {
  // Assuming all articles have the same date and country for simplicity
  const overview = articles.length > 0 ? `${new Date(articles[0].publishedDate).toLocaleDateString()} - ${articles[0].country}` : "No Data Available";

  return (
    <div>
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel-content"
          id="panel-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          <Typography>{overview}</Typography>
        </AccordionSummary>
        <AccordionDetails sx={{ flexDirection: 'column' }}>
          {articles.map((article, index) => (
            <div key={index}>
              <Typography variant="h6" color="#E5E7EB" sx={{ mt: 2 }}>
                {article.title}
              </Typography>
              <Typography variant="subtitle1" color="#E5E7EB">
                {article.description}
              </Typography>
              <Typography variant="body2" color="#E5E7EB" sx={{ mt: 1 }}>
                Published: {new Date(article.publishedDate).toLocaleDateString()}
              </Typography>
              <Link href={article.url} color="secondary" target="_blank" rel="noopener" sx={{ mb: 2 }}>
                Read more
              </Link>
            </div>
          ))}
        </AccordionDetails>
      </Accordion>
    </div>
  );
}

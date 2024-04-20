import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

export default function AccordionArticle({ articles }) {
  // Assuming all articles have the same date and country for simplicity

  return (
    <div>
      {articles.map((article, index) => (
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel-content"
          id="panel-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          <Typography>{article.title}</Typography>
        </AccordionSummary>
        <AccordionDetails sx={{ flexDirection: 'column' }}>
            <div key={index}>
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

        </AccordionDetails>
      </Accordion>
      ))}
    </div>
  );
}

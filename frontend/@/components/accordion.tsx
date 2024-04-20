import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionActions from '@mui/material/AccordionActions';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';

export default function AccordionArticle({
    item
}) {
  return (
    <div>
      {/* Article Overview */}
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel1-content"
          id="panel1-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          <Typography>{item.title} - Overview</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography variant="subtitle1" color="#E5E7EB">
            {item.description}
          </Typography>
          <Typography variant="body2" color="#E5E7EB" sx={{ mt: 1 }}>
            Published: {new Date(item.publishedDate).toLocaleDateString()}
          </Typography>
          <Link href={item.url} color="secondary" target="_blank" rel="noopener">
            Read more
          </Link>
        </AccordionDetails>
      </Accordion>
    </div>
  );
}

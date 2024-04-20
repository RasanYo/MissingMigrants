import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionActions from '@mui/material/AccordionActions';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Button from '@mui/material/Button';

export default function AccordionArticle({
    item
}) {
  return (
    <div>
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel1-content"
          id="panel1-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          Accordion 1
        </AccordionSummary>
        <AccordionDetails>
          <p style={{ color: '#fff' }}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </p>
        </AccordionDetails>
      </Accordion>
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel2-content"
          id="panel2-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          Accordion 2
        </AccordionSummary>
        <AccordionDetails>
          <p style={{ color: '#fff' }}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </p>
        </AccordionDetails>
      </Accordion>
      <Accordion sx={{ backgroundColor: '#374151', color: '#fff' }} defaultExpanded>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
          aria-controls="panel3-content"
          id="panel3-header"
          sx={{ backgroundColor: '#4b5563' }}
        >
          Accordion Actions
        </AccordionSummary>
        <AccordionDetails>
          <p style={{ color: '#fff' }}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
            malesuada lacus ex, sit amet blandit leo lobortis eget.
          </p>
        </AccordionDetails>
        <AccordionActions>
          <Button style={{ color: '#fff' }}>Cancel</Button>
          <Button style={{ color: '#fff' }}>Agree</Button>
        </AccordionActions>
      </Accordion>
    </div>
  );
}

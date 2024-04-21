import React, { useState } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';
import Divider from '@mui/material/Divider';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import DeathIcon from '@mui/icons-material/PersonOutline'; // Assuming custom icons for illustrative purposes
import MissingIcon from '@mui/icons-material/HelpOutline';
import CauseIcon from '@mui/icons-material/ReportProblem';
import OriginIcon from '@mui/icons-material/Flag';

export default function AccordionArticle({ articles }) {
  const [open, setOpen] = useState(false);
  const [selectedArticle, setSelectedArticle] = useState(null);

  const handleClickOpen = (article) => {
    setSelectedArticle(article);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      {articles.map((article, index) => (
        <Accordion key={index} sx={{ backgroundColor: '#374151', color: '#fff' }}>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
            aria-controls="panel-content"
            id={`panel-header-${index}`}
            sx={{ backgroundColor: '#4b5563' }}
          >
            <Typography>{article.title}</Typography>
            <IconButton
              onClick={() => handleClickOpen(article)}
              color="inherit"
              edge="end"
              size="small"
              sx={{ marginLeft: 'auto' }}
            >
              <InfoIcon />
            </IconButton>
          </AccordionSummary>
          <AccordionDetails sx={{ flexDirection: 'column', color: '#E5E7EB' }}>
            <Typography variant="subtitle1">{article.description}</Typography>
            <Typography variant="body2" sx={{ mt: 1 }}>
              Published: {new Date(article.publishedDate).toLocaleDateString()}
            </Typography>
            <Link href={article.url} color="secondary" target="_blank" rel="noopener" sx={{ mt: 1 }}>
              Read more
            </Link>
          </AccordionDetails>
        </Accordion>
      ))}
      {selectedArticle && (
        <Dialog open={open} onClose={handleClose} aria-labelledby="dialog-title" aria-describedby="dialog-description">
          <DialogTitle id="dialog-title" sx={{ backgroundColor: '#374151', color: '#fff' }}>Detailed Information</DialogTitle>
          <DialogContent sx={{ backgroundColor: '#4b5563', color: '#E5E7EB' }}>
            <Divider sx={{ my: 2 }} />
            <List dense>
              <ListItem>
                <ListItemIcon>
                  <DeathIcon />
                </ListItemIcon>
                <ListItemText primary="Deaths" secondary={selectedArticle.deads || "N/A"} />
              </ListItem>
              <ListItem>
                <ListItemIcon>
                  <MissingIcon />
                </ListItemIcon>
                <ListItemText primary="Missing" secondary={selectedArticle.missing || "N/A"} />
              </ListItem>
              <ListItem>
                <ListItemIcon>
                  <CauseIcon />
                </ListItemIcon>
                <ListItemText primary="Cause of Death" secondary={selectedArticle.cause_death || "N/A"} />
              </ListItem>
              <ListItem>
                <ListItemIcon>
                  <OriginIcon />
                </ListItemIcon>
                <ListItemText primary="Country of Origin" secondary={selectedArticle.country_origin || "N/A"} />
              </ListItem>
            </List>
          </DialogContent>
          <DialogActions sx={{ backgroundColor: '#374151' }}>
            <Button onClick={handleClose} color="primary">
              Close
            </Button>
          </DialogActions>
        </Dialog>
      )}
    </div>
  );
}

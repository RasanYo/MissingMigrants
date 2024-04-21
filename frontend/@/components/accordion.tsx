import React, { useState } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';
import DeleteIcon from '@mui/icons-material/Delete'; // Import the delete icon
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
import DeathIcon from '@mui/icons-material/PersonOutline';
import MissingIcon from '@mui/icons-material/HelpOutline';
import CauseIcon from '@mui/icons-material/ReportProblem';
import OriginIcon from '@mui/icons-material/Flag';

export default function AccordionArticle({ articles }) {
  const [open, setOpen] = useState(false);
  const [deletedArticles, setDeletedArticles] = useState([]);

  const handleDelete = () => {
    setOpen(false);
  };

    const handleDeleteArticle = (article) => {
      setDeletedArticles((prevDeletedArticles) => [...prevDeletedArticles, article]);
    };


  return (
    <>
      {articles.map((article, index) => {
        if (!deletedArticles.includes(article)) {
          return (
            <Accordion key={index} sx={{ backgroundColor: '#374151', color: '#fff' }}>
              <AccordionSummary
                expandIcon={<ExpandMoreIcon style={{ color: '#fff' }} />}
                aria-controls={`panel-content-${index}`}
                id={`panel-header-${index}`}
                sx={{ backgroundColor: '#4b5563' }}
              >
                <Typography>{article.title}</Typography>
                {/* Add delete button */}
                <IconButton
                  onClick={(e) => {
                    e.stopPropagation(); // Prevent the click event from propagating to the AccordionSummary
                    handleDeleteArticle(article); // Call the handleDeleteArticle function to remove the article from selectedArticles
                  }}
                  color="inherit"
                  edge="end"
                  size="small"
                  sx={{ marginLeft: 'auto' }}
                >
                  <DeleteIcon />
                </IconButton>
              </AccordionSummary>
              <AccordionDetails sx={{ flexDirection: 'column', color: '#E5E7EB' }}>
                <Typography variant="subtitle1">
                  Description: {article.description}
                </Typography>
                <Typography variant="body2" sx={{ mt: 1 }}>
                  Published: {new Date(article.publishedDate).toLocaleDateString()}
                </Typography>
                <Link href={article.url} color="secondary" target="_blank" rel="noopener" sx={{ mt: 1 }}>
                  Read more
                </Link>
              </AccordionDetails>
            </Accordion>
          );
        } else {
          return null; // Don't render the article if it's in the deletedArticles array
        }
      })}
    </>
  );
}

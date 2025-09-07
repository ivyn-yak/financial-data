import React from "react";
import { Box, Typography, Divider } from "@mui/material";

function SectionBox({ title, children }) {
  return (
    <Box
      sx={{
        padding: 2,
        border: "1px solid #e0e0e0",
        boxShadow: "0 2px 6px rgba(0,0,0,0.05)", 
        backgroundColor: "background.paper", 
      }}
    >
      <Typography variant="h6" sx={{fontWeight: "bold"}} gutterBottom>
        {title}
      </Typography>
      <Divider sx={{ mb: 2, borderBottomWidth: 2, borderColor: "#bdbdbd" }}/> 
      {children}
    </Box>
  );
}

export default SectionBox;

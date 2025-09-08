import React from "react";
import { Box, Chip, Typography } from "@mui/material";

export default function Transcript({ data }) {
  // Fallback to empty array if data is invalid
  const segments = Array.isArray(data) ? data : [];

  const sentimentColor = (score) => {
    if (score > 0.05) {
      return { backgroundColor: "#d0f5d0", color: "#1b5e20" }; // light green
    }
    if (score < -0.05) {
      return { backgroundColor: "#fddede", color: "#b71c1c" }; // light red
    }
    return { backgroundColor: "#e0e0e0", color: "#000" }; // neutral gray
  };

  if (segments.length === 0)
    return <Typography>No transcript available</Typography>;

  return (
    <Box sx={{ display: "flex", flexDirection: "column", gap: 1.5, p: 2 }}>
      {segments.map((segment) => (
        <Box
          key={segment.id}
          sx={{
            display: "flex",
            flexDirection: "column",
            padding: 1.5,
            borderBottom: "1px solid #e0e0e0",
            gap: 0.5,
          }}
        >
          {/* Speaker + Title + Sentiment */}
          <Box sx={{ display: "flex", alignItems: "center", gap: 1 }}>
            <Typography
              variant="subtitle2"
              sx={{ fontWeight: 600, color: "#424242" }}
            >
              {segment.speaker} {segment.title ? `• ${segment.title}` : ""}
            </Typography>
            {typeof segment.sentiment === "number" && (
              <Chip
                label={`Sentiment: ${segment.sentiment.toFixed(2)}`}
                size="small"
                sx={{
                  ...sentimentColor(segment.sentiment),
                  fontWeight: 600,
                }}
              />
            )}
          </Box>

          {/* Transcript content */}
          <Typography
            variant="body2"
            sx={{ color: "#212121", lineHeight: 1.6 }}
          >
            {segment.content ?? "-"}
          </Typography>
        </Box>
      ))}
    </Box>
  );
}

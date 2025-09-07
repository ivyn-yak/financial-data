import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Box, Paper, Typography } from "@mui/material";
import useFetch from "../hooks/useFetch";

export default function TranscriptPage() {
  const { _, earnings_call_id, quarter } = useParams();
  const url = `/earnings/transcript/${earnings_call_id}`;
  const { data, loading, error } = useFetch(url);
  console.log("Transcript data:", data);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <Box sx={{ width: "90%" }}>
      <Box sx={{ display: "flex", flexDirection: "column", gap: 1.5, p: 2 }}>
        <Typography
          variant="h6"
          sx={{ fontWeight: 600, color: "#424242", mb: 0.5 }}
        >
          Transcript for {quarter} Earnings Call
        </Typography>
        {data.map((segment) => (
          <Box
            key={segment.id}
            sx={{
              display: "flex",
              flexDirection: "column",
              padding: 1.5,
              borderBottom: "1px solid #e0e0e0",
            }}
          >
            <Typography
              variant="subtitle2"
              sx={{ fontWeight: 600, color: "#424242", mb: 0.5 }}
            >
              {segment.speaker} {segment.title ? `• ${segment.title}` : ""}
            </Typography>
            <Typography
              variant="body2"
              sx={{ color: "#212121", lineHeight: 1.6 }}
            >
              {segment.content}
            </Typography>
          </Box>
        ))}
      </Box>
    </Box>
  );
}

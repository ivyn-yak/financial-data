import React from "react";
import { useParams, useLocation } from "react-router-dom";
import useFetch from "../hooks/useFetch.jsx";
import Transcript from "../components/Transcript.jsx";
import TranscriptSidebar from "../components/TranscriptSidebar.jsx";
import { Grid, Box } from "@mui/material";
import SectionBox from "../components/SectionBox.jsx";

export default function TranscriptPage() {
  const { symbol, earnings_call_id } = useParams();
  const url = `/earnings/transcript/${earnings_call_id}`;
  const { data, loading, error } = useFetch(url);
  console.log("Transcript data:", data);

  const location = useLocation();
  const { quarter } = location.state || {};

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <Box sx={{ p: 4 }}>
      <Grid container spacing={1}>
        {/* Main content: Key Stats */}
        <Grid item size={{ xs: 12, md: 8 }}>
          <SectionBox
            title={`Transcript for ${quarter} Earnings Call`}
            children={<Transcript data={data} />}
          />
        </Grid>

        {/* Sidebar: Company Profile */}
        <Grid item size={{ xs: 12, md: 4 }}>
          <SectionBox
            title="Transcript Overview"
            children={<TranscriptSidebar data={data} />}
          />
        </Grid>
      </Grid>
    </Box>
  );
}

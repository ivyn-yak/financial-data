import React from "react";
import StockChart from "../components/StockChart";
import KeyStats from "../components/KeyStats";
import CompanyProfile from "../components/CompanyProfile";
import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";
import { Grid, Box, Stack } from "@mui/material";
import SectionBox from "../components/SectionBox";
import NewsSidebar from "../components/NewsSidebar";

function HomePage() {
  const { symbol } = useParams();
  const url = `/company/${symbol}`;
  const { data, loading, error } = useFetch(url);

  return (
    <Box sx={{ p: 4 }}>
      <Grid container spacing={1}>
        {/* Main content: Key Stats */}
        <Grid item size={{ xs: 12, md: 8 }}>
          <Stack spacing={1}>
            <SectionBox
              title={`${symbol} Stock Chart`}
              children={
                <StockChart />
              }
            />
            <SectionBox
              title="Key Statistics"
              children={
                <KeyStats data={data} loading={loading} error={error} />
              }
            />
          </Stack>
        </Grid>

        {/* Sidebar: Company Profile */}
        <Grid item size={{ xs: 12, md: 4 }}>
          <Stack spacing={1}>
            <SectionBox
              title="Company Profile"
              children={
                <CompanyProfile data={data} loading={loading} error={error} />
              }
            />
            <SectionBox
              title="Recent News"
              children={
                <NewsSidebar />
              }
            />
          </Stack>
        </Grid>
      </Grid>
    </Box>
  );
}

export default HomePage;

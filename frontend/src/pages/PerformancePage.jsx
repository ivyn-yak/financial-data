import React from "react";
import CompanyProfile from "../components/CompanyProfile.jsx";
import useFetch from "../hooks/useFetch.jsx";
import { useParams } from "react-router-dom";
import { Grid, Box, Stack } from "@mui/material";
import SectionBox from "../components/SectionBox.jsx";
import NewsSidebar from "../components/NewsSidebar.jsx";
import PerformanceChart from "../components/PerformanceChart.jsx";
import StockChartYF from "../components/StockChartYF.jsx";

function PerformancePage() {
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
              title={`${symbol} Performance Overview`}
              children={
                <PerformanceChart />
              }
            />
            <SectionBox
              title={`${symbol} Stock Chart`}
              children={
                <StockChartYF data={data} loading={loading} error={error} />
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

export default PerformancePage;

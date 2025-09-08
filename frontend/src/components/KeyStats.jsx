import React from "react";
import {
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableRow,
  Paper,
  Typography,
} from "@mui/material";

function KeyStats({ data, loading, error }) {
  const symbol = data?.Symbol || "N/A";

  const formatNumber = (num) => {
    if (num === null || num === undefined) return "-";
    if (num >= 1e12) return (num / 1e12).toFixed(2) + "T";
    if (num >= 1e9) return (num / 1e9).toFixed(2) + "B";
    if (num >= 1e6) return (num / 1e6).toFixed(2) + "M";
    return num.toLocaleString();
  };

  const formatPercentage = (num) => {
    if (num === null || num === undefined) return "-";
    return (num * 100).toFixed(2) + "%";
  };

  if (loading) return <Typography>Loading stock data...</Typography>;
  if (error) return <Typography color="error">Error: {error}</Typography>;
  if (!data || typeof data !== "object") return <Typography>No data available for {symbol}</Typography>;

  const groupedStats = {
    "Price & Performance": [
      { label: "Symbol", value: data.Symbol ?? "-" },
      { label: "Exchange", value: data.Exchange ?? "-" },
      { label: "Beta", value: data.Beta ?? "-" },
    ],
    Financials: [
      { label: "Revenue (TTM)", value: formatNumber(data.RevenueTTM) },
      { label: "Quarterly Revenue Growth YOY", value: formatPercentage(data.QuarterlyRevenueGrowthYOY) },
      { label: "EPS", value: data.EPS ?? "-" },
      { label: "Sector", value: data.Sector ?? "-" },
      { label: "Industry", value: data.Industry ?? "-" },
    ],
    Dividend: [
      { label: "Dividend per Share", value: data.DividendPerShare ?? "-" },
      { label: "Dividend Yield", value: formatPercentage(data.DividendYield) },
      { label: "Dividend Date", value: data.DividendDate ?? "-" },
      { label: "Ex-Dividend Date", value: data.ExDividendDate ?? "-" },
    ],
    Valuation: [
      { label: "Market Cap", value: formatNumber(data.MarketCapitalization) },
      { label: "P/E Ratio", value: data.PERatio ?? "-" },
      { label: "Forward P/E", value: data.ForwardPE ?? "-" },
      { label: "Price to Book", value: data.PriceToBookRatio ?? "-" },
      { label: "Analyst Target Price", value: data.AnalystTargetPrice ?? "-" },
    ],
  };

  return (
    <>
      {Object.entries(groupedStats).map(([group, stats], idx) => (
        <Box key={idx} sx={{ marginBottom: 3 }}>
          <Typography variant="subtitle1" gutterBottom>
            {group}
          </Typography>
          <TableContainer component={Paper} elevation={0}>
            <Table size="small">
              <TableBody>
                {Array.isArray(stats) ? (
                  stats.map((stat, i) => (
                    <TableRow key={i}>
                      <TableCell sx={{ fontWeight: "bold", width: "40%" }}>
                        {stat.label}
                      </TableCell>
                      <TableCell>{stat.value}</TableCell>
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell colSpan={2}>No stats available</TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </TableContainer>
        </Box>
      ))}
    </>
  );
}

export default KeyStats;

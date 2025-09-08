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

function CompanyProfile({ data, loading, error }) {
  if (loading) return <p>Loading stock data...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!data || typeof data !== "object") return <Typography>No data available</Typography>;

  const profiles = [
    { label: "Symbol", value: data.Symbol },
    { label: "Name", value: data.Name },
    { label: "Asset Type", value: data.AssetType ?? "-" },
    { label: "Description", value: data.Description ?? "-" },
    { label: "Exchange", value: data.Exchange },
    { label: "Currency", value: data.Currency },
    { label: "Sector", value: data.Sector ?? "-" },
    { label: "Industry", value: data.Industry ?? "-" },
    { label: "Official Site", value: data.OfficialSite ?? "-" },
  ];

  return (
    <Box sx={{ marginBottom: 3 }}>
      <TableContainer component={Paper} elevation={0}>
        <Table size="small">
          <TableBody>
            {profiles.map((profile, i) => (
              <TableRow key={i}>
                <TableCell sx={{ fontWeight: "bold", width: "40%" }}>
                  {profile.label}
                </TableCell>
                <TableCell>{profile.value}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default CompanyProfile;

import * as React from "react";
import { Typography, Box } from "@mui/material";
import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";

const Header = () => {
  const { symbol } = useParams();
  const url = `/tickers/${symbol}`;
  const { data, loading, error } = useFetch(url);

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography>Error fetching data</Typography>;

  const entity = data ?? {};
  const isPositive = entity.change >= 0;

  return (
    <Box
      sx={{
        top: 16,
        left: 16,
        display: "flex",
        alignItems: "baseline",
        p: 2,
        zIndex: 1000,
        bgcolor: "white",
        gap: 2,
      }}
    >
      {/* Symbol */}
      <Typography variant="h4" sx={{ fontWeight: 700 }}>
        {entity.symbol ?? "N/A"}
      </Typography>

      {/* Price + currency */}

      <Box sx={{ display: "flex", alignItems: "baseline", gap: 0.5 }}>
        <Typography variant="h5" sx={{ fontWeight: 700 }}>
          {entity.last_price?.toFixed(2) ?? "--"}
        </Typography>
        <Typography variant="subtitle1" sx={{ color: "text.secondary" }}>
          {entity.currency ?? ""}
        </Typography>
      </Box>

      {/* Change + percentage */}
      <Typography
        variant="h6"
        sx={{ color: isPositive ? "green" : "red", fontWeight: "bold" }}
      >
        {entity.change != null ? (entity.change >= 0 ? "+" : "") : ""}
        {entity.change?.toFixed(2) ?? "--"} (
        {entity.percent_change != null
          ? entity.percent_change >= 0
            ? "+"
            : ""
          : ""}
        {entity.percent_change?.toFixed(2) ?? "--"}%)
      </Typography>
    </Box>
  );
};

export default Header;

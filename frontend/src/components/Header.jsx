import * as React from "react";
import { Typography, Box, Divider } from "@mui/material";
import useFetch from "../hooks/useFetch.jsx";
import { useParams } from "react-router-dom";

const Header = () => {
  const { symbol } = useParams();
  const url = `/stock-price/yf/${symbol}`;
  const { data, loading, error } = useFetch(url);
  console.log("Fetched header data:", data);

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
        gap: 3,
      }}
    >
      {/* Symbol */}
      <Typography variant="h5" sx={{ fontWeight: 600 }}>
        {entity.symbol ?? "N/A"}
      </Typography>

      {/* Vertical Divider */}
      <Divider orientation="vertical" flexItem sx={{ mx: 1 }} />

      <Box sx={{ display: "flex", alignItems: "baseline", gap: 1 }}>
        {/* Price */}
        <Typography
          variant="h5"
          sx={{ fontWeight: 700 }}
        >
          {entity.last_price != null ? entity.last_price.toFixed(2) : "--"}
        </Typography>

        {/* Currency */}
        <Typography
          variant="subtitle1"
          sx={{ fontWeight: 500, color: "text.secondary" }}
        >
          {entity.currency ?? "USD"}
        </Typography>

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
    </Box>
  );
};

export default Header;

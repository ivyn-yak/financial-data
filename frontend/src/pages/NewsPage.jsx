import React from "react";
import { useParams } from "react-router-dom";
import { Box } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import useNewsData from "../hooks/useNewsData.jsx";

function NewsPage() {
  const { symbol } = useParams();
  const url = `/news/${symbol}`;
  const { rows, columns, loading, error } = useNewsData(url);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <Box sx={{  width: "100%" }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={10}
        disableSelectionOnClick
        onRowClick={(params) => window.open(params.row.url, "_blank")}
        hideFooter={true}
        rowHeight={80}
      />
    </Box>
  );
}

export default NewsPage;

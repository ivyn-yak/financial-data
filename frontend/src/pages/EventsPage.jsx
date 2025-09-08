import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Box } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import useFetch from "../hooks/useFetch";

export default function EventsPage() {
  const { symbol } = useParams();
  const navigate = useNavigate();
  const url = `/earnings/${symbol}`;
  const { data, loading, error } = useFetch(url);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  const dataRows = (data || []).map((event, index) => ({
    id: index + 1,
    earnings_call_id: event.id,
    quarter: event.quarter.replace(/(....)(Q\d)/, "$1 $2"),
    eventType: "Earnings Call",
  }));

  const columns = [
    { field: "id", headerName: "No.", width: 100 },
    { field: "quarter", headerName: "Quarter", width: 200 },
    { field: "eventType", headerName: "Event Type", flex: 2 },  
  ];

  return (
    <Box sx={{ width: "90%" }}>
      <DataGrid
        rows={dataRows || []}
        columns={columns}
        getRowId={(row) => row.id}
        pageSize={10}
        onRowClick={(params) => {
          navigate(`/${symbol}/events/${params.row.earnings_call_id}`, {
            state: { earnings_call_id: params.row.earnings_call_id, quarter: params.row.quarter },
          });
        }}
        disableSelectionOnClick
        hideFooter={true}
      />
    </Box>
  );
}

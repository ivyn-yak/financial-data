import React, { useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import { ToggleButton, ToggleButtonGroup } from "@mui/material";

function FinancialDataGrid({ period, onPeriodChange, rows, columns }) {
  const handlePeriodChange = (event, newPeriod) => {
    if (newPeriod !== null) onPeriodChange(newPeriod); 
  };

  return (
    <div>
      {/* Toggle buttons for period */}
      <ToggleButtonGroup
        value={period}
        exclusive
        onChange={handlePeriodChange}
        sx={{ mb: 2 }}
      >
        <ToggleButton value="Quarterly">Quarterly</ToggleButton>
        <ToggleButton value="Annual">Annual</ToggleButton>
      </ToggleButtonGroup>

      {/* DataGrid */}
      <div style={{ height: "auto", width: "90%" }}>
        <DataGrid
          rows={rows}
          columns={columns}
          pageSize={20}
          disableSelectionOnClick
          hideFooter={true}
        />
      </div>
    </div>
  );
}

export default FinancialDataGrid;

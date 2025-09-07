import React, { useState } from "react";
import useFinancialData from "../hooks/useFinancialData";
import BalanceSheetFields from "../consts/BalanceSheetFields.jsx";
import FinancialDataGrid from "./FinancialDataGrid";
import { useParams } from "react-router-dom";

function BalanceSheetGrid() {
  const { symbol } = useParams(); 
  const [period, setPeriod] = useState("Quarterly");
  const url = `/balance_sheet/${symbol}?period=${period}&k=5`;
  const { rows, columns, loading, error } = useFinancialData(url, BalanceSheetFields);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <FinancialDataGrid
      period={period}
      onPeriodChange={setPeriod}
      rows={rows}
      columns={columns}
    />
  );
}

export default BalanceSheetGrid;

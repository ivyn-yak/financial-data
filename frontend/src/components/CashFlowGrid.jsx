import React, { useState } from "react";
import useFinancialData from "../hooks/useFinancialData";
import CashFlowStatementFields from "../consts/CashFlowStatementFields.jsx";
import FinancialDataGrid from "./FinancialDataGrid";

function CashFlowGrid({ symbol }) {
  const [period, setPeriod] = useState("Quarterly");
  const url = `/cash_flow/${symbol}?period=${period}&k=5`;
  const { rows, columns, loading, error } = useFinancialData(url, CashFlowStatementFields);

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

export default CashFlowGrid;

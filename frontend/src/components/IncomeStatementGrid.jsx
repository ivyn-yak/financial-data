import React, { useState } from "react";
import useFinancialData from "../hooks/useFinancialData.jsx";
import IncomeStatementFields from "../consts/IncomeStatementFields.jsx";
import FinancialDataGrid from "./FinancialDataGrid.jsx";
import { useParams } from "react-router-dom";

function IncomeStatementGrid() {
  const { symbol } = useParams();
  const [period, setPeriod] = useState("Quarterly");
  const url = `/income_statement/${symbol}?period=${period}&k=5`;
  const { rows, columns, loading, error } = useFinancialData(url, IncomeStatementFields);

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

export default IncomeStatementGrid;

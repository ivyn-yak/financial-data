import { useState, useEffect } from "react";
import useFetch from "./useFetch.jsx";

export default function useFinancialData(url, fieldMap) {
  const [rows, setRows] = useState([]);
  const [columns, setColumns] = useState([]);
  const { data, loading, error } = useFetch(url);

  useEffect(() => {
    if (!data) return;

    // Ensure data is an array
    const arrayData = Array.isArray(data) ? data : [data];

    // Step 1: Clean each object
    const cleanedData = arrayData.map((item) =>
      Object.entries(item)
        .filter(([key]) => fieldMap[key])
        .reduce((acc, [key, value]) => {
          acc[fieldMap[key]] = value !== null ? value.toLocaleString() : "—";
          return acc;
        }, {})
    );

    // Step 2: Prepare rows (one row per field)
    const fields = Object.values(fieldMap);
    const dataRows = fields.map((field, index) => {
      const row = { id: index, field };
      cleanedData.forEach((sheet) => {
        row[sheet["Fiscal Date Ending"]] = sheet[field] || "—";
      });
      return row;
    });

    // Step 3: Prepare columns (first = field, then one per fiscalDateEnding)
    const dataColumns = [
      {
        field: "field",
        headerName: "",
        flex: 2,
        renderCell: (params) => (
          <span style={{ fontWeight: "bold" }}>{params.value}</span>
        ),
      },
      ...cleanedData.map((sheet) => ({
        field: sheet["Fiscal Date Ending"],
        headerName: sheet["Fiscal Date Ending"],
        flex: 1,
      })),
    ];

    setRows(dataRows);
    setColumns(dataColumns);
  }, [data, fieldMap]);

  return { rows, columns, loading, error };
}

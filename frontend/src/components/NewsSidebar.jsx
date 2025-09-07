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
import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";

function NewsSidebar() {
  const { symbol } = useParams();
  const url = `/news/recent/${symbol}`;
  const { data, loading, error } = useFetch(url);
  console.log("NewsSidebar data:", data);

  if (loading) return <Typography>Loading...</Typography>;
  if (error) return <Typography>Error fetching data</Typography>;
  if (!data) return <Typography>No data available</Typography>;

  return (
    <Box sx={{ marginBottom: 3 }}>
      <TableContainer component={Paper} elevation={0}>
        <Table size="small">
          <TableBody>
            {data.map((article) => (
              <TableRow
                key={article.id}
                sx={{
                  cursor: "pointer",
                  "&:hover": { backgroundColor: "#f5f5f5" },
                  height: 80, 
                }}
                onClick={() => window.open(article.url, "_blank")}
              >
                <TableCell sx={{ width: 100 }}>
                  {article.banner_image ? (
                    <img
                      src={article.banner_image}
                      alt={article.title}
                      style={{
                        width: 80, 
                        height: 60, 
                        objectFit: "cover",
                        borderRadius: 2,
                        display: "block",
                        margin: "auto",
                      }}
                    />
                  ) : (
                    <Box
                      sx={{
                        width: 80,
                        height: 60,
                        bgcolor: "#eee",
                        borderRadius: 1,
                        margin: "auto",
                      }}
                    />
                  )}
                </TableCell>

                <TableCell>
                  <Box
                    sx={{
                      display: "flex",
                      flexDirection: "column",
                      justifyContent: "center",
                      height: "100%",
                    }}
                  >
                    <Typography variant="subtitle2" fontWeight="bold">
                      {article.title}
                    </Typography>
                    <Typography variant="caption" color="textSecondary">
                      {article.source} |{" "}
                      {new Date(article.time_published).toLocaleDateString()}
                    </Typography>
                  </Box>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default NewsSidebar;

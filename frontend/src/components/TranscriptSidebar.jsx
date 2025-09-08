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
  LinearProgress,
} from "@mui/material";
import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";

function TranscriptSidebar({ data }) {
  if (!data) return <Typography>No data available</Typography>;

  const sentiments = data.map((seg) => seg.sentiment);

  // Overall metrics
  const avgSentiment =
    sentiments.reduce((sum, s) => sum + s, 0) / sentiments.length;

  const minSentiment = Math.min(...sentiments);
  const maxSentiment = Math.max(...sentiments);

  // Distribution
  const distribution = {
    positive: sentiments.filter((s) => s > 0).length,
    negative: sentiments.filter((s) => s < 0).length,
    neutral: sentiments.filter((s) => s === 0).length,
  };

  const metrics = {
    avgSentiment,
    minSentiment,
    maxSentiment,
    distribution,
  };

  const totalSegments =
    metrics.distribution.positive +
    metrics.distribution.negative +
    metrics.distribution.neutral;

  const distPercent = {
    positive: (metrics.distribution.positive / totalSegments) * 100,
    negative: (metrics.distribution.negative / totalSegments) * 100,
    neutral: (metrics.distribution.neutral / totalSegments) * 100,
  };

  const sectionGroups = data.reduce((acc, seg) => {
    if (!acc[seg.title]) {
      acc[seg.title] = [];
    }
    acc[seg.title].push(seg.sentiment);
    return acc;
  }, {});

  // Compute average per section
  const sectionAverages = Object.fromEntries(
    Object.entries(sectionGroups).map(([title, sentiments]) => [
      title,
      sentiments.reduce((sum, s) => sum + s, 0) / sentiments.length,
    ])
  );

  const sentimentColor = (score) => {
    if (score > 0) {
      return { color: "green" };
    }
    if (score < 0) {
      return { color: "red" };
    }
    return { color: "black" };
  };

  console.log("Transcript metrics:", metrics);

  return (
    <Box sx={{ marginBottom: 3 }}>
      <TableContainer component={Paper} elevation={0}>
        <Table size="small">
          <TableBody>
            {/* Section Header */}
            <TableRow>
              <TableCell colSpan={2} sx={{ bgcolor: "#fafafa" }}>
                <Typography variant="subtitle2" fontWeight="bold">
                  Overall Metrics
                </Typography>
              </TableCell>
            </TableRow>

            {/* Overall Avg */}
            <TableRow>
              <TableCell sx={{ width: 150 }}>
                <Typography variant="subtitle2" fontWeight="bold">
                  Average Sentiment
                </Typography>
              </TableCell>
              <TableCell>
                <Typography
                  variant="body2"
                  sx={{
                    ...sentimentColor(metrics.avgSentiment),
                    fontWeight: 600,
                  }}
                >
                  {metrics.avgSentiment.toFixed(2)}
                </Typography>
              </TableCell>
            </TableRow>

            {/* Min / Max */}
            <TableRow>
              <TableCell>
                <Typography variant="subtitle2" fontWeight="bold">
                  Minimum Sentiment
                </Typography>
              </TableCell>
              <TableCell>
                <Typography
                  variant="body2"
                  sx={{
                    ...sentimentColor(metrics.minSentiment),
                    fontWeight: 600,
                  }}
                >
                  {metrics.minSentiment}
                </Typography>
              </TableCell>
            </TableRow>

            {/* Min / Max */}
            <TableRow>
              <TableCell>
                <Typography variant="subtitle2" fontWeight="bold">
                  Maximum Sentiment
                </Typography>
              </TableCell>
              <TableCell>
                <Typography
                  variant="body2"
                  sx={{
                    ...sentimentColor(metrics.maxSentiment),
                    fontWeight: 600,
                  }}
                >
                  {metrics.maxSentiment}
                </Typography>
              </TableCell>
            </TableRow>

            {/* Distribution */}
            <TableRow>
              <TableCell>
                <Typography variant="subtitle2" fontWeight="bold">
                  Distribution
                </Typography>
              </TableCell>
              <TableCell>
                <Box sx={{ display: "flex", flexDirection: "column", gap: 1 }}>
                  <Box>
                    <Typography variant="caption" color="textSecondary">
                      Positive ({metrics.distribution.positive})
                    </Typography>
                    <LinearProgress
                      variant="determinate"
                      value={distPercent.positive}
                      sx={{ height: 6, borderRadius: 1, mt: 0.5 }}
                      color="success"
                    />
                  </Box>
                  <Box>
                    <Typography variant="caption" color="textSecondary">
                      Negative ({metrics.distribution.negative})
                    </Typography>
                    <LinearProgress
                      variant="determinate"
                      value={distPercent.negative}
                      sx={{ height: 6, borderRadius: 1, mt: 0.5 }}
                      color="error"
                    />
                  </Box>
                  <Box>
                    <Typography variant="caption" color="textSecondary">
                      Neutral ({metrics.distribution.neutral})
                    </Typography>
                    <LinearProgress
                      variant="determinate"
                      value={distPercent.neutral}
                      sx={{ height: 6, borderRadius: 1, mt: 0.5 }}
                      color="info"
                    />
                  </Box>
                </Box>
              </TableCell>
            </TableRow>

            {/* Section Header */}
            <TableRow>
              <TableCell colSpan={2} sx={{ bgcolor: "#fafafa" }}>
                <Typography variant="subtitle2" fontWeight="bold">
                  Section Averages
                </Typography>
              </TableCell>
            </TableRow>

            {/* Section Averages */}
            {Object.entries(sectionAverages).map(([section, avg]) => (
              <TableRow
                key={section}
                sx={{
                  cursor: "pointer",
                  "&:hover": { backgroundColor: "#f5f5f5" },
                }}
              >
                <TableCell>
                  <Typography variant="body2">{section}</Typography>
                </TableCell>
                <TableCell>
                  <Typography
                    variant="body2"
                    sx={{
                      ...sentimentColor(avg),
                      fontWeight: 600,
                    }}
                  >
                    {avg.toFixed(2)}
                  </Typography>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default TranscriptSidebar;

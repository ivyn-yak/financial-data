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

export default function TranscriptSidebar({ data }) {
  // Ensure data is an array
  const segments = Array.isArray(data) ? data : [];
  if (segments.length === 0)
    return <Typography>No transcript data available</Typography>;

  // Sentiments array (default 0)
  const sentiments = segments.map((seg) => seg.sentiment ?? 0);

  // Overall metrics
  const avgSentiment =
    sentiments.length > 0
      ? sentiments.reduce((sum, s) => sum + s, 0) / sentiments.length
      : 0;
  const minSentiment = Math.min(...sentiments);
  const maxSentiment = Math.max(...sentiments);

  // Distribution counts
  const distribution = {
    positive: sentiments.filter((s) => s > 0).length,
    negative: sentiments.filter((s) => s < 0).length,
    neutral: sentiments.filter((s) => s === 0).length,
  };

  const totalSegments =
    distribution.positive + distribution.negative + distribution.neutral;

  const distPercent = {
    positive: (distribution.positive / totalSegments) * 100,
    negative: (distribution.negative / totalSegments) * 100,
    neutral: (distribution.neutral / totalSegments) * 100,
  };

  // Group segments by section/title
  const sectionGroups = segments.reduce((acc, seg) => {
    const title = seg.title ?? "No Section";
    if (!acc[title]) acc[title] = [];
    acc[title].push(seg.sentiment ?? 0);
    return acc;
  }, {});

  // Compute section averages
  const sectionAverages = Object.fromEntries(
    Object.entries(sectionGroups).map(([title, segSentiments]) => [
      title,
      segSentiments.length
        ? segSentiments.reduce((sum, s) => sum + s, 0) / segSentiments.length
        : 0,
    ])
  );

  // Sentiment text color
  const sentimentColor = (score) => {
    if (score > 0) return { color: "green" };
    if (score < 0) return { color: "red" };
    return { color: "gray" };
  };

  return (
    <Box sx={{ marginBottom: 3 }}>
      <TableContainer component={Paper} elevation={0}>
        <Table size="small">
          <TableBody>
            {/* Overall Metrics Header */}
            <TableRow>
              <TableCell colSpan={2} sx={{ bgcolor: "#fafafa" }}>
                <Typography variant="subtitle2" fontWeight="bold">
                  Overall Metrics
                </Typography>
              </TableCell>
            </TableRow>

            {/* Average Sentiment */}
            <TableRow>
              <TableCell sx={{ width: 150 }}>
                <Typography variant="subtitle2" fontWeight="bold">
                  Average Sentiment
                </Typography>
              </TableCell>
              <TableCell>
                <Typography
                  variant="body2"
                  sx={{ ...sentimentColor(avgSentiment), fontWeight: 600 }}
                >
                  {avgSentiment.toFixed(2)}
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
                  sx={{ ...sentimentColor(minSentiment), fontWeight: 600 }}
                >
                  {minSentiment.toFixed(2)}
                </Typography>
              </TableCell>
            </TableRow>
            <TableRow>
              <TableCell>
                <Typography variant="subtitle2" fontWeight="bold">
                  Maximum Sentiment
                </Typography>
              </TableCell>
              <TableCell>
                <Typography
                  variant="body2"
                  sx={{ ...sentimentColor(maxSentiment), fontWeight: 600 }}
                >
                  {maxSentiment.toFixed(2)}
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
                  {["positive", "negative", "neutral"].map((key) => (
                    <Box key={key}>
                      <Typography variant="caption" color="textSecondary">
                        {key.charAt(0).toUpperCase() + key.slice(1)} (
                        {distribution[key]})
                      </Typography>
                      <LinearProgress
                        variant="determinate"
                        value={distPercent[key]}
                        sx={{ height: 6, borderRadius: 1, mt: 0.5 }}
                        color={
                          key === "positive"
                            ? "success"
                            : key === "negative"
                            ? "error"
                            : "info"
                        }
                      />
                    </Box>
                  ))}
                </Box>
              </TableCell>
            </TableRow>

            {/* Section Averages Header */}
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
                sx={{ "&:hover": { backgroundColor: "#f5f5f5" } }}
              >
                <TableCell>
                  <Typography variant="body2">{section}</Typography>
                </TableCell>
                <TableCell>
                  <Typography
                    variant="body2"
                    sx={{ ...sentimentColor(avg), fontWeight: 600 }}
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

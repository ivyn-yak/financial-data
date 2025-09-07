import { useState, useEffect } from "react";
import { Box, Typography, Chip } from "@mui/material";
import useFetch from "./useFetch";

export default function useNewsData(url) {
  const [rows, setRows] = useState([]);
  const [columns, setColumns] = useState([]);
  const { data, loading, error } = useFetch(url);

  useEffect(() => {
    if (!data) return;

    const arrayData = Array.isArray(data) ? data : [data];

    const dataRows = arrayData.map((article, index) => ({
      id: index,
      image: article.banner_image,
      title: article.title,
      timePublished: new Date(article.time_published).toLocaleString(),
      source: `${article.source || "Unknown"}`,
      sentiment: article.overall_sentiment_label || "Neutral",
      sentimentScore: article.overall_sentiment_score ?? 0,
      tickerSentiment: (article.ticker_sentiment?.length > 8
        ? [
            // sort descending, take top 4
            ...[...article.ticker_sentiment]
              .sort(
                (a, b) => b.ticker_sentiment_score - a.ticker_sentiment_score
              )
              .slice(0, 4),
            // sort ascending, take worst 4
            ...[...article.ticker_sentiment]
              .sort(
                (a, b) => a.ticker_sentiment_score - b.ticker_sentiment_score
              )
              .slice(0, 4),
          ]
        : article.ticker_sentiment || []
      ).map((ts) => ({
        ticker: ts.ticker,
        label: ts.ticker_sentiment_label,
        score: ts.ticker_sentiment_score,
      })),
      url: article.url,
    }));

    const dataColumns = [
      {
        field: "timePublished",
        headerName: "Time",
        width: 200,
        sortable: false,
      },
      {
        field: "title",
        headerName: "Headline",
        flex: 3,
      },
      {
        field: "source",
        headerName: "Source",
        flex: 1,
      },
      {
        field: "tickerSentiment",
        headerName: "Ticker Sentiment",
        flex: 2,
        renderCell: (params) => {
          const sentiments = params.value || [];
          return (
            <Box
              sx={{
                display: "flex",
                flexWrap: "wrap",
                gap: 0.5,
                alignItems: "center",
                mt: 2,
              }}
            >
              {sentiments.map((ts) => {
                let bgColor = "#e0e0e0"; // default light gray
                let textColor = "#000"; // default black

                if (ts.score > 0) {
                  bgColor = "#d0f5d0"; // light green
                  textColor = "#1b5e20";
                } else if (ts.score < 0) {
                  bgColor = "#fddede"; // light red
                  textColor = "#b71c1c";
                }

                return (
                  <Chip
                    key={ts.ticker}
                    label={`${ts.ticker}: ${ts.score.toFixed(
                      2
                    )}`}
                    size="small"
                    sx={{
                      backgroundColor: bgColor,
                      color: textColor,
                      fontWeight: "bold",
                    }}
                  />
                );
              })}
            </Box>
          );
        },
      },
    ];

    setRows(dataRows);
    setColumns(dataColumns);
  }, [data]);

  return { rows, columns, loading, error };
}

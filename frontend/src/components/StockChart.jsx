import React, { useState, useEffect } from "react";
import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  Tooltip,
  Title,
  Legend,
  TimeScale,
  LineElement,
  PointElement,
} from "chart.js";
import {
  CandlestickController,
  CandlestickElement,
} from "chartjs-chart-financial";
import "chartjs-adapter-luxon";
import { Chart } from "react-chartjs-2";
import { DateTime } from "luxon";

ChartJS.register(
  CategoryScale,
  LinearScale,
  TimeScale,
  LineElement,
  PointElement,
  CandlestickController,
  CandlestickElement,
  Tooltip,
  Title,
  Legend
);

function StockChart() {
  const { symbol } = useParams();
  const [barData, setBarData] = useState([]);
  const [lineData, setLineData] = useState([]);

  const url = `/stock-price/${encodeURIComponent(symbol)}/history`;
  const { data, loading, error } = useFetch(url);
  console.log("Fetched stock data:", data);

  const loadChart = () => {
    let bars = [];
    let line = [];
    Object.entries(data)
      .sort(([a], [b]) => new Date(a) - new Date(b))
      .forEach(([date, values]) => {
        const dt = DateTime.fromISO(date); // parse ISO string to Luxon DateTime
        const millis = dt.toMillis(); // numerical timestamp for Chart.js
        bars.push({
          x: millis, // or use date.toISOString() / date.getTime() for Chart.js
          o: parseFloat(values["1. open"]),
          h: parseFloat(values["2. high"]),
          l: parseFloat(values["3. low"]),
          c: parseFloat(values["4. close"]),
        });
        line.push({ x: millis, y: parseFloat(values["4. close"]) });
      });
    setBarData(bars);
    setLineData(line);
  };

  useEffect(() => {
    if (data) {
      loadChart();
    }
  }, [data]);

  const stockData = {
    datasets: [
      {
        label: `${symbol} OHLC`,
        data: barData,
        borderColor: "#26a69a",
        borderWidth: 1,
        barThickness: 5,
        maxBarThickness: 10,
      },
      {
        label: "Close Price",
        type: "line",
        data: lineData,
        hidden: true,
        borderColor: "#ff0000",
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: `${symbol} Stock Candlestick Chart` },
      tooltip: { enabled: true, mode: "index" },
    },
    scales: {
      x: {
        type: "time",
        time: {
          unit: "day",
          tooltipFormat: "DD MMM yyyy",
          displayFormats: {
            day: "dd LLL",
          },
        },
        title: {
          display: true,
          text: "Date",
        },
      },
      y: {
        beginAtZero: false,
        title: {
          display: true,
          text: "Price",
        },
      },
    },
  };

  return (
    <div>
      {loading && <p>Loading stock data...</p>}
      {error && <p>Error: {error}</p>}
      {!loading && !error && data && (
        <Chart type="candlestick" data={stockData} options={options} />
      )}
    </div>
  );
}

export default StockChart;

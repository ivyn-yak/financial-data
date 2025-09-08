import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const PerformanceChart = () => {
  const { symbol } = useParams();
  const url = `/performance/${encodeURIComponent(symbol)}/chart`;
  const { data, loading, error } = useFetch(url);
  console.log("Fetched performance data:", data);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading data: {error.message}</p>;
  if (!data) return <p>No data available</p>;

  const performanceData = {
    labels: data.dates, // array of dates
    datasets: [
      {
        label: data.stock.symbol,
        data: data.stock.cumulative_returns, // array of cumulative returns
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        tension: 0.2,
      },
      {
        label: data.baseline.symbol,
        data: data.baseline.cumulative_returns, // array of cumulative returns for benchmark
        borderColor: "rgba(255,99,132,1)",
        backgroundColor: "rgba(255,99,132,0.2)",
        tension: 0.2,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: `Cumulative Returns: ${data.stock.symbol} vs ${data.baseline.symbol}`,
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        ticks: {
          callback: function (value) {
            return (value * 100).toFixed(2) + "%"; // show percentages
          },
        },
      },
    },
  };

  return <Line data={performanceData} options={options} />;
};

export default PerformanceChart;

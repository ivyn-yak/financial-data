import { Routes, Route, useParams } from "react-router-dom";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage";
// import PerformancePage from "./PerformancePage";
import FinancialsPage from "./pages/FinancialsPage";
import NewsPage from "./pages/NewsPage";
// import EventsPage from "./EventsPage";
// import NewsDataGrid from "./components/NewsDataGrid";

function App() {
  const { symbol } = useParams(); 

  return (
    <div className="App">
      <Navbar symbol={symbol} />
      <main className="App-content">
        <Routes>
          <Route path="" element={<HomePage />} />
          <Route path="performance" element={<HomePage />} />
          <Route path="financial" element={<FinancialsPage symbol={symbol}/>} />
          <Route path="news" element={<NewsPage />} />
          <Route path="events" element={<HomePage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

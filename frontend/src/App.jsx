import { Routes, Route, useParams } from "react-router-dom";
import Navbar from "./components/Navbar";
import HomePage from "./pages/HomePage.jsx";
import PerformancePage from "./pages/PerformancePage.jsx";
import FinancialsPage from "./pages/FinancialsPage.jsx";
import NewsPage from "./pages/NewsPage.jsx";
import EventsPage from "./pages/EventsPage.jsx";
import TranscriptPage from "./pages/TranscriptPage.jsx";

function App() {
  const { symbol } = useParams(); 

  return (
    <div className="App">
      <Navbar symbol={symbol} />
      <main className="App-content">
        <Routes>
          <Route path="" element={<HomePage />} />
          <Route path="performance" element={<PerformancePage />} />
          <Route path="financial" element={<FinancialsPage />} />
          <Route path="news" element={<NewsPage />} />
          <Route path="events" element={<EventsPage />} />
          <Route path="events/:earnings_call_id" element={<TranscriptPage/>} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

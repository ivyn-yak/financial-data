import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        {/* Here App is wrapped in a route that provides :symbol */}
        <Route path="/:symbol/*" element={<App />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
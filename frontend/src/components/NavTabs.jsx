import { useLocation, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Box, Tabs, Tab } from "@mui/material";

export default function NavTabs({ symbol }) {
  const location = useLocation();
  const [value, setValue] = useState("/");

  // Normalize the selected tab value from pathname
  useEffect(() => {
    const parts = location.pathname.split("/"); // e.g. ["", "NVDA", "news"]
    const tab = parts[2] ? `/${parts[2]}` : "/";
    setValue(tab);
  }, [location.pathname]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%", bgcolor: "grey.200" }}>
      <Tabs value={value} onChange={handleChange} role="navigation">
        <Tab label="Home" value="/" component={Link} to={`/${symbol}`} />
        <Tab label="Performance" value="/performance" component={Link} to={`/${symbol}/performance`} />
        <Tab label="Financial" value="/financial" component={Link} to={`/${symbol}/financial`} />
        <Tab label="News" value="/news" component={Link} to={`/${symbol}/news`} />
        <Tab label="Events" value="/events" component={Link} to={`/${symbol}/events`} />
      </Tabs>
    </Box>
  );
}

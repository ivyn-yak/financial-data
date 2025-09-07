import * as React from "react";
import AppBar from "@mui/material/AppBar";
import NavTabs from "./Navtabs";
import Header from "./Header";

const NavBar = ({ elevation = 0, sticky = true, symbol }) => {
  return (
    <AppBar
      position={sticky ? "sticky" : "static"}
      color="transparent"
      elevation={elevation}
      sx={{
        zIndex: (t) => t.zIndex.modal + 1,
        borderBottom: 1.5,
        borderColor: "divider",
        boxShadow: (theme) => `0 1px 4px ${theme.palette.grey[400]}33`,
      }}
    >
      <Header symbol={symbol}/>
      <NavTabs symbol={symbol}/>
    </AppBar>
  );
};

export default NavBar;

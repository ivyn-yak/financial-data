import { Box, Tabs, Tab } from "@mui/material";
import React from "react";
import PropTypes from "prop-types";
import BalanceSheetGrid from "../components/BalanceSheetGrid.jsx";
import IncomeStatementGrid from "../components/IncomeStatementGrid.jsx";
import CashFlowGrid from "../components/CashFlowGrid.jsx";

function CustomTabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

CustomTabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

export default function FinancialsPage() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%", bgcolor: "white" }}>
      <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
        >
          <Tab label="Balance Sheet" {...a11yProps(0)} />
          <Tab label="Income Statement" {...a11yProps(1)} />
          <Tab label="Cash Flow" {...a11yProps(2)} />
        </Tabs>
      </Box>
      <CustomTabPanel value={value} index={0}>
        <BalanceSheetGrid />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <IncomeStatementGrid />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={2}>
        <CashFlowGrid />
      </CustomTabPanel>
    </Box>
  );
}

import React, { useState } from "react";
import { Paper, Tab, Tabs } from "@material-ui/core";
import { Link, useLocation } from "react-router-dom";

import styles from "./Nav.module.scss";

const NavBar = (props) => {
  const [value, setValue] = useState(useLocation().pathname.toUpperCase());

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  return (
    <div className={styles.container}>
      <Paper className={styles.navContainer}>
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="primary"
          textColor="primary"
          centered
        >
          <Tab component={Link} to="/" value="/" label="About"></Tab>
          <Tab component={Link} to="/PFT" value="/PFT" label="PFT"></Tab>
          <Tab component={Link} to="/CFT" value="/CFT" label="CFT"></Tab>
        </Tabs>
      </Paper>
    </div>
  );
};

export default NavBar;

import React, { Component } from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { About, CFT, NavBar, PFT } from "./components";

import styles from "./App.module.scss";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <NavBar />
        <div className={styles.container}>
          <Route exact path="/" component={About} />
          <Route path="/pft" component={PFT} />
          <Route path="/cft" component={CFT} />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;

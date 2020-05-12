import React, { Component } from "react";
import { Route, HashRouter } from "react-router-dom";
import { About, CFT, NavBar, PFT } from "./components";

import styles from "./App.module.scss";

class App extends Component {
  render() {
    return (
      <HashRouter>
        <NavBar />
        <div className={styles.container}>
          <Route exact path="/" component={About} />
          <Route path="/pft" component={PFT} />
          <Route path="/cft" component={CFT} />
        </div>
      </HashRouter>
    );
  }
}

export default App;

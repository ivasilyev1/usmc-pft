import React, { useState } from "react";

import styles from "./ScoreDisplay.module.scss";

const eventLookup = {
  run: "Three Mile Run",
  row: "Five Km Row",
  pullups: "Pullups",
  pushups: "Pushups",
  crunches: "Crunches",
  plank: "Plank",
};

const ScoreDisplay = (props) => {
  return <div className={styles.container}></div>;
};

export default ScoreDisplay;

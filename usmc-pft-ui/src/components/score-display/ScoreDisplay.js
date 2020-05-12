import React, { useState, useEffect } from "react";
import { getTestScores } from "../../util/API";
import { Typography } from "@material-ui/core";

import styles from "./ScoreDisplay.module.scss";

const eventLookup = {
  pft: {
    run: "Three Mile Run",
    row: "Five Km Row",
    pullups: "Pullups",
    pushups: "Pushups",
    crunches: "Crunches",
    plank: "Plank",
  },
  cft: {},
};

const ScoreDisplay = ({ eventData, type }, props) => {
  const [scores, setScores] = useState({});
  const eventTitles = eventLookup[type];
  const cardio = eventTitles[eventData.cardio];
  const upperBody = eventTitles[eventData.upperBody];
  const abdominal = eventTitles[eventData.abdominal];

  useEffect(() => {
    const getScores = async (type, eventData) => {
      const scoreResponse = await getTestScores(type, eventData);
      setScores(scoreResponse);
    };
    getScores(type, eventData);
  }, [type, eventData]);

  if (!scores.score) {
    return (
      <div className={styles.container}>
        <Typography variant="h4">Loading Score</Typography>
      </div>
    );
  }
  const { score } = scores;
  return (
    <div className={styles.container}>
      <div className={styles.scoreRow}>
        <Typography>{cardio}</Typography>
        <Typography id={styles.score}>
          {`${score[eventData.cardio].score}
          / ${score[eventData.cardio].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{upperBody}</Typography>
        <Typography id={styles.score}>
          {`${score[eventData.upperBody].score}
          / ${score[eventData.upperBody].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{abdominal}</Typography>
        <Typography id={styles.score}>
          {`${score[eventData.abdominal].score}
          / ${score[eventData.abdominal].max}`}
        </Typography>
      </div>
      <div className={styles.totalScore}>
        <Typography variant="h4">Total</Typography>
        <Typography variant="h4">{`${score.total.score}`}</Typography>
      </div>
      <div className={styles.classDisplay}>
        <Typography variant="h6">Class</Typography>
      </div>
    </div>
  );
};

export default ScoreDisplay;

import React, { useState, useEffect } from "react";
import EventTotalClass from "./EventTotalClass";
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

const ScoreDisplay = ({
  eventData: { cardio, upperBody, abdominal },
  eventData,
  type,
}) => {
  const [scores, setScores] = useState({});

  useEffect(() => {
    const getScores = async (type, eventData) => {
      const scoreResponse = await getTestScores(type, eventData);
      setScores(scoreResponse);
    };
    getScores(type, eventData);
  }, [type, eventData]);

  const { score } = scores;
  if (!score || !score[cardio] || !score[upperBody] || !score[abdominal]) {
    return (
      <div className={styles.container}>
        <Typography variant="h4">Loading Score</Typography>
      </div>
    );
  }

  const eventTitles = eventLookup[type];
  const cardioTitle = eventTitles[cardio];
  const upperBodyTitle = eventTitles[upperBody];
  const abdominalTitle = eventTitles[abdominal];
  const { total } = score;
  return (
    <div className={styles.container}>
      <div className={styles.scoreRow}>
        <Typography>{cardioTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[cardio].score}
            / ${score[cardio].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{upperBodyTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[upperBody].score}
            / ${score[upperBody].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{abdominalTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[abdominal].score}
            / ${score[abdominal].max}`}
        </Typography>
      </div>
      <EventTotalClass total={total} />
    </div>
  );
};

export default ScoreDisplay;

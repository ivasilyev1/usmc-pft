import React, { useEffect, useState } from "react";
import EventTotalClass from "./EventTotalClass";
import { getCFTScores, getPFTScores } from "../../util/API";
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
  cft: {
    mtc: "Movement to Contact",
    muf: "Maneuver Under Fire",
    ammo: "Ammo-can Lift",
  },
};

const ScoreDisplay = ({
  eventData: { firstEvent, secondEvent, thirdEvent },
  eventData,
  type,
}) => {
  const [scores, setScores] = useState({});

  useEffect(() => {
    const getScores = async (type, eventData) => {
      const scoreResponse =
        type === "pft"
          ? await getPFTScores(eventData)
          : await getCFTScores(eventData);
      setScores(scoreResponse);
    };
    getScores(type, eventData);
  }, [type, eventData]);

  const { score } = scores;
  if (score && score.error) {
    return (
      <div className={styles.errorContainer}>
        <Typography variant="body2">
          {score.error}
          <a href="mailto: admin@usmcpft.com">admin@usmcpft.com.</a>
        </Typography>
      </div>
    );
  }

  if (
    !score ||
    !score[firstEvent] ||
    !score[secondEvent] ||
    !score[thirdEvent]
  ) {
    return (
      <div className={styles.container}>
        <Typography variant="h4">Loading Score</Typography>
      </div>
    );
  }

  const eventTitles = eventLookup[type];
  const firstEventTitle = eventTitles[firstEvent];
  const secondEventTitle = eventTitles[secondEvent];
  const thirdEventTitle = eventTitles[thirdEvent];
  const { total } = score;
  return (
    <div className={styles.container}>
      <div className={styles.scoreRow}>
        <Typography>{firstEventTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[firstEvent].score}
            / ${score[firstEvent].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{secondEventTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[secondEvent].score}
            / ${score[secondEvent].max}`}
        </Typography>
      </div>
      <div className={styles.scoreRow}>
        <Typography>{thirdEventTitle}</Typography>
        <Typography id={styles.score}>
          {`${score[thirdEvent].score}
            / ${score[thirdEvent].max}`}
        </Typography>
      </div>
      <EventTotalClass total={total} />
    </div>
  );
};

export default ScoreDisplay;

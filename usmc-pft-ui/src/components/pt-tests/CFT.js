import React, { useState } from "react";
import { Button, Paper, TextField, Typography } from "@material-ui/core";
import { AgeGender, ScoreDisplay } from "../";
import { EventTime, ExerciseReps } from "../../util/formatters";

import styles from "./Common.module.scss";

const CFT = (props) => {
  const [eventData, setEventData] = useState({});
  const [showScore, setShowScore] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    // Appending additional entries to match the expected format of ScoreDisplay.js
    formData.append("firstEvent", "mtc");
    formData.append("secondEvent", "muf");
    formData.append("thirdEvent", "ammo");
    setEventData(Object.fromEntries(formData));
    setShowScore(true);
  };

  return (
    <div className={styles.container}>
      <Paper elevation={3}>
        <form onSubmit={handleSubmit}>
          <div className={styles.formContainer}>
            <AgeGender />
            <div className={styles.formRow}>
              <label id={styles.noDropDown}>
                <Typography>Movement to Contact</Typography>
              </label>
              <TextField
                id="mtc"
                name="mtc"
                type="text"
                placeholder="m:ss"
                required
                inputProps={{ maxLength: 4, inputMode: "numeric" }}
                InputProps={{
                  inputComponent: EventTime,
                }}
              />
            </div>
            <div className={styles.formRow}>
              <label id={styles.noDropDown}>
                <Typography>Maneuver Under Fire</Typography>
              </label>
              <TextField
                id="muf"
                name="muf"
                placeholder="m:ss"
                type="text"
                required
                inputProps={{ maxLength: 4, inputMode: "numeric" }}
                InputProps={{
                  inputComponent: EventTime,
                }}
              />
            </div>
            <div className={styles.formRow}>
              <label id={styles.noDropDown}>
                <Typography>Ammo-can Lifts</Typography>
              </label>
              <TextField
                id="ammo"
                name="ammo"
                type="text"
                placeholder="reps"
                required
                inputProps={{ maxLength: 3, inputMode: "numeric" }}
                InputProps={{ inputComponent: ExerciseReps }}
              />
            </div>
            <div className={styles.submitButton}>
              <Button type="submit" variant="contained" color="primary">
                Calculate Score
              </Button>
            </div>

            {showScore ? (
              <ScoreDisplay eventData={eventData} type="cft" />
            ) : null}
          </div>
        </form>
      </Paper>
    </div>
  );
};

export default CFT;

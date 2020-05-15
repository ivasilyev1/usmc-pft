import React, { useState } from "react";
import {
  Button,
  TextField,
  Select,
  Paper,
  Typography,
} from "@material-ui/core";
import { ExerciseReps, EventTime } from "../../util/formatters";
import { AgeGender, ScoreDisplay } from "../";

import styles from "./Common.module.scss";
const CFT = (props) => {
  const [eventData, setEventData] = useState({});
  const [showScore, setShowScore] = useState(false);
  return (
    <div className={styles.container}>
      <Paper elevation={3}>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            console.log(Object.fromEntries(new FormData(e.target)));
            setEventData(Object.fromEntries(new FormData(e.target)));
            setShowScore(true);
          }}
        >
          <div className={styles.formContainer}>
            <AgeGender />
            <div className={styles.formRow}>
              <label id={styles.noDropDown}>
                <Typography>Movement to Contact</Typography>
              </label>
              <TextField
                id="mtcTime"
                name="mtcTime"
                type="text"
                placeholder="m:ss"
                required
                inputProps={{ maxLength: 4 }}
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
                id="mufTime"
                name="mufTime"
                placeholder="m:ss"
                type="text"
                required
                inputProps={{ maxLength: 4 }}
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
                id="ammoReps"
                name="ammoReps"
                type="text"
                required
                inputProps={{ maxLength: 3 }}
                InputProps={{ inputComponent: ExerciseReps }}
              />
            </div>
            <div className={styles.submitButton}>
              <Button type="submit" variant="contained" color="primary">
                Calculate Score
              </Button>
            </div>
            <div>
              {showScore ? (
                <ScoreDisplay eventData={eventData} type="pft" />
              ) : null}
            </div>
          </div>
        </form>
      </Paper>
    </div>
  );
};

export default CFT;

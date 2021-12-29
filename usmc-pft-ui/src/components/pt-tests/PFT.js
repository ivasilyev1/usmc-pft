import React, { useState } from "react";
import { Button, Paper, Select, TextField } from "@material-ui/core";
import { AgeGender, ScoreDisplay } from "../";
import { EventTime, ExerciseReps, RunRowTime } from "../../util/formatters";

import styles from "./Common.module.scss";

const PlankWarning = () => {
  return (
    <blockquote className={styles.plankWarningContainer}>
      <strong>Note: </strong>
      <a
        style={{ color: "red" }}
        target="_blank"
        rel="noopener noreferrer"
        href="https://www.marines.mil/News/Messages/Messages-Display/Article/2719680/forthcoming-changes-to-the-physical-fitness-test/"
      >
        MARADMIN 404/21
      </a>{" "}
      announced upcoming changes to the min/max time(s) for the plank event to
      take effect Jan 1st 2022. The updated scoring table has not yet been
      released and these changes are not yet incorporated.
    </blockquote>
  );
};

const PFT = (props) => {
  const [eventData, setEventData] = useState({});
  const [showScore, setShowScore] = useState(false);
  const [plankSelect, setPlankSelect] = useState(false);

  const handleChange = (e) => {
    e.preventDefault();
    setPlankSelect(e.target.value === "plank");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setEventData(Object.fromEntries(new FormData(e.target)));
    setShowScore(true);
  };

  return (
    <div className={styles.container}>
      <Paper elevation={3}>
        <form onSubmit={handleSubmit}>
          <div className={styles.formContainer}>
            <AgeGender />
            <div className={styles.formRow}>
              <label>
                <Select
                  name="firstEvent"
                  defaultValue={"run"}
                  disableUnderline
                  native
                >
                  <option value={"run"}>Three Mile Run</option>
                  <option value={"row"}>Five Km Row</option>
                </Select>
              </label>
              <TextField
                id="firstEventCount"
                name="firstEventCount"
                type="text"
                placeholder="mm:ss"
                required
                inputProps={{ maxLength: 5, inputMode: "numeric" }}
                InputProps={{
                  inputComponent: RunRowTime,
                }}
              />
            </div>
            <div className={styles.formRow}>
              <label>
                <Select
                  name="secondEvent"
                  defaultValue={"pullups"}
                  disableUnderline
                  native
                >
                  <option value={"pullups"}>Pullups</option>
                  <option value={"pushups"}>Pushups</option>
                </Select>
              </label>
              <TextField
                id="secondEventCount"
                name="secondEventCount"
                type="text"
                placeholder="reps"
                required
                inputProps={{ maxLength: 2, inputMode: "numeric" }}
                InputProps={{
                  inputComponent: ExerciseReps,
                }}
              />
            </div>
            <div className={styles.formRow}>
              <label>
                <Select
                  name="thirdEvent"
                  defaultValue={"crunches"}
                  onChange={handleChange}
                  disableUnderline
                  native
                >
                  <option value={"crunches"}>Crunches</option>
                  <option value={"plank"}>Plank</option>
                </Select>
              </label>
              <TextField
                id="thirdEventCount"
                name="thirdEventCount"
                type="text"
                placeholder={plankSelect ? "m:ss" : "reps"}
                required
                inputProps={{
                  maxLength: plankSelect ? 4 : 3,
                  inputMode: "numeric",
                }}
                InputProps={
                  plankSelect
                    ? {
                        inputComponent: EventTime,
                      }
                    : { inputComponent: ExerciseReps }
                }
              />
            </div>
            <React.Fragment>
              {plankSelect ? <PlankWarning /> : null}
            </React.Fragment>
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

export default PFT;

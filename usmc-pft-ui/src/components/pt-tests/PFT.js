import React from "react";
import { Button, TextField, Select, Paper } from "@material-ui/core";
import { RunRowTime } from "../../util/time-formatter";
import { AgeGender } from "../";

import styles from "./Common.module.scss";

const PFT = (props) => {
  return (
    <Paper elevation={3}>
      <form>
        <AgeGender />
        <div className={styles.container}>
          <div className={styles.formRow}>
            <label>
              <Select
                name="cardio"
                defaultValue={"run"}
                disableUnderline
                native
              >
                <option value={"run"}>Three Mile Run</option>
                <option value={"row"}>Five Km Row</option>
              </Select>
            </label>
            <TextField
              id="cardioTime"
              name="cardioTime"
              type="text"
              inputProps={{ maxLength: 5 }}
              InputProps={{
                inputComponent: RunRowTime,
              }}
            />
          </div>
          <div className={styles.formRow}>
            <label>
              <Select
                name="upperBody"
                defaultValue={"pullups"}
                disableUnderline
                native
              >
                <option value={"pullups"}>Pullups</option>
                <option value={"pushups"}>Pushups</option>
              </Select>
            </label>
            <TextField id="upperBodyReps" name="upperBodyReps" type="text" />
          </div>
          <div className={styles.formRow}>
            <label>
              <Select
                name="abdominal"
                defaultValue={"crunches"}
                disableUnderline
                native
              >
                <option value={"crunches"}>Crunches</option>
                <option value={"plank"}>Plank</option>
              </Select>
            </label>
            <TextField id="abReps" name="abReps" type="text" />
          </div>
          <div className={styles.submitButton}>
            <Button type="submit" variant="contained" color="primary">
              Calculate Score
            </Button>
          </div>
        </div>
      </form>
    </Paper>
  );
};

export default PFT;
